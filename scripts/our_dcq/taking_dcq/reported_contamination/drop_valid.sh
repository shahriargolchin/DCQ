#!/bin/bash

BASE_PATH="../../../.."

python "${BASE_PATH}/src/taking_quiz.py" \
        --experiment "${BASE_PATH}/results/our_dcq/reported_contamination/drop" \
        --filepath "${BASE_PATH}/data/our_dcq/processed/reported_contamination/drop_valid.csv" \
        --dataset DROP \
        --split validation \
        --model gpt-4-0613 \
