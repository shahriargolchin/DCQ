#!/bin/bash

BASE_PATH="../../../.."

python  "${BASE_PATH}/src/run.py" \
        --experiment "${BASE_PATH}/results/comparative_framework/wild_evaluation/gpt3.5/yelp" \
        --filepath "${BASE_PATH}/data/comparative_framework/wild_evaluation/yelp_test.csv" \
        --task cls \
        --dataset Yelp \
        --split test \
        --model gpt-3.5-turbo-0613 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --icl_eval \
