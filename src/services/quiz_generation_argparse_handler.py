import argparse


class QuizGenerationArgumentParser:
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
            help="The filepath to the CSV file containing the original dataset instances.",
        )

        self.parser.add_argument(
            "--processed_dir",
            type=str,
            required=True,
            help="The directory to save the processed CSV file containing the generated quiz options."
        )

        self.parser.add_argument(
            "--quiz_options_column_names",
            nargs=4,
            default=["option_a", "option_b", "option_c", "option_d"],
            help="List of four column names for four options (A to D). "
            "(Default Column Names: %(default)s)",
        )

        self.parser.add_argument(
            "--columns_to_form_instances",
            type=str,
            nargs="+",
            required=True,
            help="Column names to form dataset instances. "
            "For example, for a classification task, the columns that form dataset instances "
            "are the columns that contain the texts and their corresponding labels. "
            "In general, the columns that form instances are the columns that contribute to "
            "contamination if disclosed during training. Also, make sure that these colunm(s) are "
            "present in the CSV file.",
        )

    def parse_args(self):
        args = self.parser.parse_args()
        return args
