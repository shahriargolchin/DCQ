import re
import time

import pandas as pd
from tqdm import tqdm

from helpers.experiment_result_saver import ExperimentResultSaver
from helpers.logging_config import configure_logger
from prompts.option_generation import OptionGeneration
from services.openai_api import OpenAIClient

logger = configure_logger(__name__)


class QuizGeneration(ExperimentResultSaver):
    def __init__(self, df, args):
        super().__init__(df, args.filepath, args.processed_dir)
        self.df = df
        self.args = args
        self.option_generation = OptionGeneration()
        self.openai_client = OpenAIClient()

    def process(self):
        logger.info("Starting Generating Quiz Options ...")
        self.form_instance_column()
        self.generate_all_quiz_options()
        self.concat_generated_options_to_df()
        self.check_empty_cells()
        self.save_to_csv()

    def _prepare_prompt(self, instance):
        prompt = self.option_generation.get_prompt("option_generation_prompt")
        return prompt.format(original_instance=instance)

    def _generate_quiz_options(self, index, row):
        formatted_prompt = self._prepare_prompt(row["instance"])
        if index == 0:
            logger.info(f"Input prompt:\n\n{formatted_prompt}")
        self.df.at[index, "generated_options"] = self.openai_client.get_text(
            text=formatted_prompt, model="gpt-4-0613", max_tokens=4000, temperature=1.0
        )

    def generate_all_quiz_options(self):
        pbar = tqdm(total=len(self.df), desc="Generating Quiz Options")
        for index, row in self.df.iterrows():
            self._generate_quiz_options(index, row)
            pbar.update(1)
            time.sleep(3)
        pbar.close()

    def parse_generated_options(self, text, option_columns):
        pattern = re.compile(r"(?<!\w)([A-D])\)\s*\n")
        chunks = pattern.split(text)
        options = {col: "" for col in option_columns}
        option_map = {letter: col for letter, col in zip("ABCD", option_columns)}

        for i in range(1, len(chunks), 2):
            letter, content = chunks[i], chunks[i + 1].strip()
            if letter in option_map:
                options[option_map[letter]] = content
        return options

    def concat_generated_options_to_df(self):
        parsed_data = self.df["generated_options"].apply(
            lambda text: self.parse_generated_options(
                text, self.args.quiz_options_column_names
            )
        )
        parsed_df = pd.DataFrame(parsed_data.tolist())
        self.df = pd.concat([self.df, parsed_df], axis=1)

    def check_empty_cells(self):
        logger.info("Checking for any potential missing options ...")
        any_empty_cells = False

        for column in self.args.quiz_options_column_names:
            if column in self.df.columns:
                empty_indices = self.df[column].apply(self._is_empty)
                if empty_indices.any():
                    logger.info(
                        f"Empty cells found in column '{column}' at rows: {empty_indices.index[empty_indices].tolist()}"
                    )
                    self.df.loc[empty_indices, column] = pd.NA
                    any_empty_cells = True

        if not any_empty_cells:
            logger.info("There are no missing options.")

    @staticmethod
    def _is_empty(cell):
        return pd.isna(cell) or (isinstance(cell, str) and not cell.strip())

    def form_instance_column(self):
        invalid_columns = [
            col
            for col in self.args.columns_to_form_instances
            if col not in self.df.columns
        ]
        if invalid_columns:
            raise ValueError(
                f"The following column(s) are invalid: {', '.join(invalid_columns)}"
            )

        self.df["instance"] = self.df[self.args.columns_to_form_instances].apply(
            lambda row: "\n".join([f"{col}: {row[col]}" for col in row.index]), axis=1
        )
