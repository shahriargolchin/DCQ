#!/bin/bash

BASE_PATH="../../../.."

python "${BASE_PATH}/src/generating_quiz_options.py" \
        --processed_dir "${BASE_PATH}/data/our_dcq/processed/wild_evaluation" \
        --filepath "${BASE_PATH}/data/our_dcq/raw/wild_evaluation/imdb_test.csv" \
        --columns_to_form_instances text label \
