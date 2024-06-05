#!/bin/bash

# -- Set the variables below with appropriate values --
EXPERIMENT="Path to Where Results Are Saved" 
FILEPATH="Path to CSV File Containing Original Dataset Instances and Their Perturbed Versions"
DATASET="Actual Dataset Name" 
SPLIT="Split Corresponds to Data" 
MODEL="OpenAI Model Snapshot"
# -- End of variables --


python  "../../src/taking_quiz.py" \
        --experiment "${EXPERIMENT}" \
        --filepath "${FILEPATH}" \
        --dataset "${DATASET}" \
        --split "${SPLIT}" \
        --model "${MODEL}" \
