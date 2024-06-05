#!/bin/bash

BASE_PATH="../../../../.."

python "${BASE_PATH}/src/taking_quiz.py" \
        --experiment "${BASE_PATH}/results/our_dcq/wild_evaluation/gpt3.5/yelp" \
        --filepath "${BASE_PATH}/data/our_dcq/processed/wild_evaluation/yelp_test.csv" \
        --dataset Yelp \
        --split test \
        --model gpt-3.5-turbo-0613 \
