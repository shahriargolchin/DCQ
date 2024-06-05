import pandas as pd

from core.bias_compensator_quiz import BiasCompensatorQuiz
from core.bias_detector_quiz import BiasDetectorQuiz
from helpers.logging_config import configure_logger
from services.taking_quiz_argparse_handler import TakingQuizArgumentParser

logger = configure_logger(__name__)


def main():
    args = TakingQuizArgumentParser().parse_args()
    df = pd.read_csv(args.filepath, encoding="utf-8")

    non_preferred_options, bdq_results = BiasDetectorQuiz(
        df=df,
        args=args,
    ).process()

    BiasCompensatorQuiz(
        df=df,
        args=args,
        non_preferred_options=non_preferred_options,
        bdq_results=bdq_results,
    ).process()

    logger.info("*** All process done! ***")


if __name__ == "__main__":
    main()
