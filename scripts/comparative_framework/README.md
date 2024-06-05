## Detailed Explanation of the Comparative Framework

As mentioned in the chief README file, for every setting in the paper involving the comparative framework, we have provided corresponding bash files. You can find these bash files in the respective subdirectories here.

While the corresponding bash files are provided here, to run these scripts, you need to clone the repository corresponding to our [comparative framework](https://arxiv.org/abs/2311.06233). You can find the repository [here](https://github.com/shahriargolchin/time-travel-in-llms/tree/main).

> [!IMPORTANT]
> For our comparative framework, we discovered that selecting random-length initial segments within the range of 40% to 70% for dataset instances leads to higher counts of replicated exact and near-exact matches. To reflect this finding and to ensure the reproducibility of the results presented in this paper, pre-split instances have been provided in the CSV files related to this framework under the `data` directory. In fact, the provided bash files are configured to use these pre-split instances, so we did not activate the argument that is responsible for splitting the instances in this framework (`should_text_split`).
