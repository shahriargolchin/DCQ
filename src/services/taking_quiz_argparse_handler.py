import argparse


class TakingQuizArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
        self.initialize_parser()

    def initialize_parser(self):
        self.parser.add_argument(
            "--filepath",
            required=True,
            type=str,
            help="The filepath to the CSV file containing the original dataset instances "
            "and the generated quiz options.",
        )

        self.parser.add_argument(
            "--dataset",
            required=True,
            type=str,
            help="Dataset name.",
        )
        self.parser.add_argument(
            "--split",
            required=True,
            type=str,
            choices=["train", "test", "validation"],
            help="Dataset partition. (Choices: %(choices)s)",
        )
        self.parser.add_argument(
            "--model",
            required=True,
            type=str,
            help="Model name to be evaluated for contamination. "
            "Select an OpenAI model snapshot, such as a version "
            "of GPT-4 or GPT-3.5",
        )

        self.parser.add_argument(
            "--experiment",
            type=str,
            required=True,
            help="The name of the experiment. All final results will be saved in this directory.",
        )

        self.parser.add_argument(
            "--quiz_options_column_names",
            nargs=4,
            default=["option_a", "option_b", "option_c", "option_d"],
            help="List of four column names for four options (A to D). "
            "(Default Column Names: %(default)s)",
        )

        self.parser.add_argument(
            "--dataset_instances_column_name",
            type=str,
            default="instance",
            help="Column name for the dataset instances. This column is generated "
            "automatically after generating the quiz options. (default: %(defualt)s)",
        )

    def parse_args(self):
        args = self.parser.parse_args()
        return args
