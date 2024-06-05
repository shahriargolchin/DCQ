#!/bin/bash
# Note: The "sum" prompt used for this dataset was modified to adapt to QA task. For this, we replaced the word "summary" with "question" in the prompt.

BASE_PATH="../../.."

python  "${BASE_PATH}/src/run.py" \
        --experiment "${BASE_PATH}/results/comparative_framework/reported_contamination/drop" \
        --filepath "${BASE_PATH}/data/comparative_framework/reported_contamination/drop_valid.csv" \
        --task sum \
        --dataset DROP \
        --split validation \
        --model gpt-4-0613 \
        --text_column question \
        --process_guided_replication  \
        --icl_eval \
