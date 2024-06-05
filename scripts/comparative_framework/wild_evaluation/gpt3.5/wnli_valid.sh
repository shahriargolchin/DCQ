#!/bin/bash

BASE_PATH="../../../.."

python  "${BASE_PATH}/src/run.py" \
        --experiment "${BASE_PATH}/results/comparative_framework/wild_evaluation/gpt3.5/wnli" \
        --filepath "${BASE_PATH}/data/comparative_framework/wild_evaluation/wnli_valid.csv" \
        --task nli \
        --dataset WNLI \
        --split validation \
        --model gpt-3.5-turbo-0613 \
        --text_column sentence1 sentence2 \
        --label_column label \
        --process_guided_replication  \
        --icl_eval \
