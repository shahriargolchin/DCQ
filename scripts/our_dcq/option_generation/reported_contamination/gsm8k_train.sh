#!/bin/bash

BASE_PATH="../../../.."

python "${BASE_PATH}/src/generating_quiz_options.py" \
        --processed_dir "${BASE_PATH}/data/our_dcq/processed/reported_contamination" \
        --filepath "${BASE_PATH}/data/our_dcq/raw/reported_contamination/gsm8k_train.csv" \
        --columns_to_form_instances question \
