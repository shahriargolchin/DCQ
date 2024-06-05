import time

from tqdm import tqdm

from helpers.experiment_result_saver import ExperimentResultSaver
from helpers.logging_config import configure_logger
from helpers.option_counter import calculate_non_preferred_options
from prompts.quiz_question import QuizQuestion
from services.openai_api import OpenAIClient

logger = configure_logger(__name__)


class BiasDetectorQuiz(ExperimentResultSaver):
    def __init__(self, df, args):
        super().__init__(df, args.filepath, args.experiment)
        self.df = df
        self.args = args
        self.openai_client = OpenAIClient()
        self.quiz_question = QuizQuestion()

    def _prepare_prompt(self, row):
        prompt_template = self.quiz_question.get_prompt("quiz_question_prompt")
        formatted_prompt = prompt_template.format(
            split_name=self.args.split,
            dataset_name=self.args.dataset,
            option_a=row[self.args.quiz_options_column_names[0]],
            option_b=row[self.args.quiz_options_column_names[1]],
            option_c=row[self.args.quiz_options_column_names[2]],
            option_d=row[self.args.quiz_options_column_names[3]],
        )
        return formatted_prompt

    def _take_quiz(self, index, row):
        formatted_prompt = self._prepare_prompt(row)
        if index == 0:
            logger.info(f"Input prompt:\n\n{formatted_prompt}")

        result = self.openai_client.get_text(
            text=formatted_prompt, model=self.args.model, max_tokens=1, temperature=0.0
        )
        self.df.at[index, "bdq_results"] = result

    def _log_non_preferred_options(self):
        non_preferred_options, bdq_results = calculate_non_preferred_options(self.df)
        logger.info(
            f"Non-preferred options: {', '.join(non_preferred_options).upper()}"
        )
        return non_preferred_options, bdq_results

    def process(self):
        logger.info("Starting Bias Detector Quiz (BDQ) ...")

        with tqdm(total=len(self.df), desc="Taking BDQ") as pbar:
            for index, row in self.df.iterrows():
                self._take_quiz(index, row)
                pbar.update(1)
                time.sleep(3)

        self.save_to_csv()

        return self._log_non_preferred_options()
