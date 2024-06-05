#!/bin/bash

# -- Set the variables below with appropriate values --
PROCESSED_DIR="Directory to Where Results to be Saved"
FILEPATH="Path to Input CSV File" 
COLUMNS_TO_FORM_INSTANCES=("Column 1" "Column 2")
# -- End of variables --


python  "../../src/generating_quiz_options.py" \
        --processed_dir "${PROCESSED_DIR}" \
        --filepath "${FILEPATH}" \
        --columns_to_form_instances "${COLUMNS_TO_FORM_INSTANCES[@]}" \
