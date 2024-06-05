import time

from tqdm import tqdm

from helpers.experiment_result_saver import ExperimentResultSaver
from helpers.logging_config import configure_logger
from helpers.option_counter import QuizPerformance
from prompts.quiz_question import QuizQuestion
from services.openai_api import OpenAIClient

logger = configure_logger(__name__)


class BiasCompensatorQuiz(ExperimentResultSaver):
    def __init__(self, df, args, non_preferred_options, bdq_results):
        super().__init__(df, args.filepath, args.experiment)
        self.df = df
        self.args = args
        self.non_preferred_options = non_preferred_options
        self.bdq_results = bdq_results
        self.openai_client = OpenAIClient()
        self.quiz_question = QuizQuestion()
        self.quiz_performance = QuizPerformance(
            df=df,
            non_preferred_options=non_preferred_options,
            bdq_results=bdq_results,
        )
        self.option_mapping = self._create_option_mapping(args)

    @staticmethod
    def _create_option_mapping(args):
        return {
            "a": (
                args.dataset_instances_column_name,
                args.quiz_options_column_names[1],
                args.quiz_options_column_names[2],
                args.quiz_options_column_names[3],
            ),
            "b": (
                args.quiz_options_column_names[0],
                args.dataset_instances_column_name,
                args.quiz_options_column_names[2],
                args.quiz_options_column_names[3],
            ),
            "c": (
                args.quiz_options_column_names[0],
                args.quiz_options_column_names[1],
                args.dataset_instances_column_name,
                args.quiz_options_column_names[3],
            ),
            "d": (
                args.quiz_options_column_names[0],
                args.quiz_options_column_names[1],
                args.quiz_options_column_names[2],
                args.dataset_instances_column_name,
            ),
        }

    def _prepare_prompt(self, row, non_preferred_option):
        prompt_template = self.quiz_question.get_prompt("quiz_question_prompt")
        option_a, option_b, option_c, option_d = self.option_mapping[
            non_preferred_option
        ]

        formatted_prompt = prompt_template.format(
            split_name=self.args.split,
            dataset_name=self.args.dataset,
            option_a=row[option_a],
            option_b=row[option_b],
            option_c=row[option_c],
            option_d=row[option_d],
        )
        return formatted_prompt

    def _take_quiz(self, index, row, non_preferred_option):
        formatted_prompt = self._prepare_prompt(row, non_preferred_option)

        if index == 0:
            logger.info(f"Input prompt:\n\n{formatted_prompt}")

        result_key = f"bcq_results_for_position_{non_preferred_option.lower()}"
        self.df.at[index, result_key] = self.openai_client.get_text(
            text=formatted_prompt, model=self.args.model, max_tokens=1, temperature=0.0
        )

    def process(self):
        logger.info("Starting Bias Compensator Quizzes (BCQs) ...")

        for non_preferred_option in self.non_preferred_options:
            desc = f"Taking BCQ with correct answers in position {non_preferred_option.upper()}"

            with tqdm(total=len(self.df), desc=desc) as pbar:
                for index, row in self.df.iterrows():
                    self._take_quiz(index, row, non_preferred_option)
                    pbar.update(1)
                    time.sleep(3)

                pbar.close()
                self.save_to_csv()

        self._log_and_save_contamination_levels()

    def _log_and_save_contamination_levels(self):
        (
            max_cont_level,
            min_cont_level,
            bcqs_results,
        ) = self.quiz_performance.calculate_best_quiz_performance()

        logger.info(
            f"Detected Contamination Level: [{min_cont_level * 100}%, {max_cont_level * 100}%]"
        )

        self.prepare_contamination_report(
            max_cont_level=max_cont_level,
            min_cont_level=min_cont_level,
            bcqs_results=bcqs_results,
            non_preferred_options=self.non_preferred_options,
            bdq_results=self.bdq_results,
        )
