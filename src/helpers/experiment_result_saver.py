from pathlib import Path

from helpers.logging_config import configure_logger

logger = configure_logger(__name__)


class ExperimentResultSaver:
    def __init__(self, df, filepath, experiment):
        self.df = df
        self.filepath = Path(filepath)
        self.experiment = Path(experiment)

    def _check_or_create_experiment_result_folder(self):
        if not self.experiment.exists():
            self.experiment.mkdir(parents=True, exist_ok=True)

    def save_to_csv(self):
        self._check_or_create_experiment_result_folder()
        csv_filepath = self.experiment / self.filepath.name
        self.df.to_csv(csv_filepath, encoding="utf-8", index=False)
        logger.info(f"Results saved to: {csv_filepath}")

    def _format_bdq_results(self, bdq_results, non_preferred_options):
        bdq_section = "BDQ results (positional biases):\n"
        for option, bias in bdq_results.items():
            bdq_section += (
                f"Option {option.upper()}: {(bias/len(self.df)) * 100:.2f}%\n"
            )
        bdq_section += (
            f"Non-preferred Options: {', '.join(non_preferred_options).upper()}\n"
        )
        bdq_section += "=" * 50 + "\n"
        return bdq_section

    def _format_bcq_results(self, bcqs_results):
        bcq_section = ""
        for position, results in bcqs_results.items():
            bcq_section += (
                f"BCQ results with correct answers in position {position.upper()}:\n"
            )
            for option, count in results.items():
                bcq_section += (
                    f"Option {option.upper()}: {(count / len(self.df)) * 100:.2f}%\n"
                )
            bcq_section += "=" * 50 + "\n"
        return bcq_section

    def _format_contamination_levels(self, max_cont_level, min_cont_level):
        return f"Detected Contamination Level: [{min_cont_level * 100:.2f}%, {max_cont_level * 100:.2f}%]\n"

    def prepare_contamination_report(
        self,
        max_cont_level,
        min_cont_level,
        bcqs_results,
        non_preferred_options,
        bdq_results,
    ):
        bdq_section = self._format_bdq_results(bdq_results, non_preferred_options)
        bcq_section = self._format_bcq_results(bcqs_results)
        contamination_levels = self._format_contamination_levels(
            max_cont_level, min_cont_level
        )

        report = bdq_section + bcq_section + contamination_levels
        report_filepath = (
            self.experiment / f"data_contamination_report_for_{self.filepath.stem}.txt"
        )

        with report_filepath.open("w") as f:
            f.write(report)

        logger.info(f"Quiz report saved to: {report_filepath}")
