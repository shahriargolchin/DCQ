#!/bin/bash

BASE_PATH="../../../.."

python  "${BASE_PATH}/src/run.py" \
        --experiment "${BASE_PATH}/results/comparative_framework/wild_evaluation/gpt4/ag_news" \
        --filepath "${BASE_PATH}/data/comparative_framework/wild_evaluation/ag_news_test.csv" \
        --task cls \
        --dataset "AG News" \
        --split test \
        --model gpt-4-0613 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --icl_eval \
