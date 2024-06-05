#!/bin/bash

BASE_PATH="../../../.."

python "${BASE_PATH}/src/taking_quiz.py" \
        --experiment "${BASE_PATH}/results/our_dcq/reported_contamination/humaneval" \
        --filepath "${BASE_PATH}/data/our_dcq/processed/reported_contamination/humaneval_test.csv" \
        --dataset HumanEval \
        --split test \
        --model gpt-4-0613 \
