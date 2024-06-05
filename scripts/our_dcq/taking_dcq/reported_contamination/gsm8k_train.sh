#!/bin/bash

BASE_PATH="../../../.."

python "${BASE_PATH}/src/taking_quiz.py" \
        --experiment "${BASE_PATH}/results/our_dcq/reported_contamination/gsm8k" \
        --filepath "${BASE_PATH}/data/our_dcq/processed/reported_contamination/gsm8k_train.csv" \
        --dataset GSM8k \
        --split train \
        --model gpt-4-0613 \
