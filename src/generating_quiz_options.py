import pandas as pd

from core.quiz_generation import QuizGeneration
from helpers.logging_config import configure_logger
from services.quiz_generation_argparse_handler import \
    QuizGenerationArgumentParser

logger = configure_logger(__name__)


def main():
    args = QuizGenerationArgumentParser().parse_args()
    df = pd.read_csv(args.filepath, encoding="utf-8")
    QuizGeneration(df=df, args=args).process()
    logger.info("*** All process done! ***")


if __name__ == "__main__":
    main()
