## Detailed Explanation of Experiments:

As mentioned in the chief README file, for every setting in the paper, we have provided corresponding bash files. You can find these bash files in the respective subdirectories here.

We also provide two bash files, `option_generation.sh` and `taking_dcq.sh`, with which you can implement our methodology for estimating data contamination tailored to your own data. Using the first bash file, you can generate word-level perturbations which serve as the quiz options for DCQ. Then, using the second bash file, you can run DCQ on your data.

Since our technique is inexpensive and is capable of estimating contamination using a small subset of data (in our research, we used a maximum of 100 instances per dataset partition), a CSV file is used as the input into this project.

## Detailed Explanation of Input Arguments:

### Option Generation:

- `filepath` (required): The filepath to the input CSV file containing the original dataset instances. As mentioned, we used a maximum of 100 dataset instances per dataset partition in our paper. More instances result in a more accurate estimation of data contamination, but also increase the computational cost.

- `processed_dir` (required): The directory to save the output CSV file containing the generated quiz options (word-level perturbations) generated by the script.

- `columns_to_form_instances` (required): The column names in the input CSV file that will be used to form the instances for which the quiz options will be generated. The selection of these columns is dataset-specific. Depending on the task, the columns should be selected so that if their values are revealed during model pre-training, it can lead to data contamination. The column names should be separated by space.

- `quiz_options_column_names` (optional): The column names that the four generated quiz options (word-level perturbations) will be stored under in the output CSV file. The default values are `option_a`, `option_b`, `option_c`, and `option_d`.

### Taking DCQ:

- `filepath` (required): The filepath to the CSV file containing the original dataset instances and word-level perturbations. This file is generated after running the corresponding script for option generation.

- `dataset` (required): The actual name of the dataset that your data belongs to.

- `split` (required): The split of the dataset that your data belongs to. The split should be one of `train`, `validation`, or `test`.

- `model` (required): The snapshot of the OpenAI model that serves as the underlying model.

- `experiment` (required): The directory that all the output files will be saved in. This directory is considered with respect to the base directory of the project.

- `quiz_options_column_names` (optional): The column names that the four generated quiz options (word-level perturbations) are stored under in the input CSV file. The default values are `option_a`, `option_b`, `option_c`, and `option_d`.

- `dataset_instances_column_name` (optional): The column name in the input CSV file that contains the original dataset instances. The default column name is `instance`.