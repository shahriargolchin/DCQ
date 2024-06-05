#!/bin/bash

BASE_PATH="../../../../.."

python "${BASE_PATH}/src/taking_quiz.py" \
        --experiment "${BASE_PATH}/results/our_dcq/wild_evaluation/gpt3.5/ag_news" \
        --filepath "${BASE_PATH}/data/our_dcq/processed/wild_evaluation/ag_news_test.csv" \
        --dataset "AG News" \
        --split test \
        --model gpt-4-0613 \
