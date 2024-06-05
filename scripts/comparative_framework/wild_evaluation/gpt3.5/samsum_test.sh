#!/bin/bash

BASE_PATH="../../../.."

python  "${BASE_PATH}/src/run.py" \
        --experiment "${BASE_PATH}/results/comparative_framework/wild_evaluation/gpt3.5/samsum" \
        --filepath "${BASE_PATH}/data/comparative_framework/wild_evaluation/samsum_test.csv" \
        --task sum \
        --dataset SAMSum \
        --split test \
        --model gpt-3.5-turbo-0613 \
        --text_column summary \
        --process_guided_replication  \
        --icl_eval \
