#!/bin/bash

BASE_PATH="../../../.."

python  "${BASE_PATH}/src/run.py" \
        --experiment "${BASE_PATH}/results/comparative_framework/wild_evaluation/gpt4/xsum" \
        --filepath "${BASE_PATH}/data/comparative_framework/wild_evaluation/xsum_test.csv" \
        --task xsum \
        --dataset XSum \
        --split test \
        --model gpt-4-0613 \
        --text_column summary \
        --process_guided_replication  \
        --icl_eval \
