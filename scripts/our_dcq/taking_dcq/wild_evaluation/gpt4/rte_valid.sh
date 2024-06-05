#!/bin/bash

BASE_PATH="../../../../.."

python "${BASE_PATH}/src/taking_quiz.py" \
        --experiment "${BASE_PATH}/results/our_dcq/wild_evaluation/gpt3.5/rte" \
        --filepath "${BASE_PATH}/data/our_dcq/processed/wild_evaluation/rte_valid.csv" \
        --dataset RTE \
        --split validation \
        --model gpt-4-0613 \
