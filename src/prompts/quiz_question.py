class QuizQuestion:
    def __init__(self):
        self.prompts = {
            "quiz_question_prompt": """You are provided with a five-choice quiz. Your task is to CORRECTLY select the option that EXACTLY corresponds to an instance from the {split_name} split of the {dataset_name} dataset.

When selecting the option, you MUST ensure that you follow the following rules:
(1) You MUST ensure that you ONLY generate a single option letter as your answer.
(2) If you do not know the dataset or the correct answer, you MUST select option "E) None of the provided options."

Hint: While all the following options seem similar in terms of meaning, there is ONLY one option that reflects the EXACT WORDING with respect to the original instance.
---
A)
{option_a}

B)
{option_b}

C)
{option_c}

D)
{option_d}

E)
None of the provided options.
---
ANSWER:
"""
        }

    def get_prompt(self, prompt_type):
        return self.prompts.get(prompt_type, "Invalid prompt type")
