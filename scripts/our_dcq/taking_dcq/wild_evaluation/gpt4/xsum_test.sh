#!/bin/bash

BASE_PATH="../../../../.."

python "${BASE_PATH}/src/taking_quiz.py" \
        --experiment "${BASE_PATH}/results/our_dcq/wild_evaluation/gpt3.5/xsum" \
        --filepath "${BASE_PATH}/data/our_dcq/processed/wild_evaluation/xsum_test.csv" \
        --dataset XSum \
        --split test \
        --model gpt-4-0613 \
