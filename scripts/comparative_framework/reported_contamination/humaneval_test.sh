#!/bin/bash
# Note: The "sum" prompt used for this dataset was modified to adapt to coding task. For this, we replaced the word "summary" with "code" in the prompt.

BASE_PATH="../../.."

python  "${BASE_PATH}/src/run.py" \
        --experiment "${BASE_PATH}/results/comparative_framework/reported_contamination/humaneval" \
        --filepath "${BASE_PATH}/data/comparative_framework/reported_contamination/humaneval_test.csv" \
        --task sum \
        --dataset HumanEval \
        --split test \
        --model gpt-4-0613 \
        --text_column prompt \
        --process_guided_replication  \
        --icl_eval \
