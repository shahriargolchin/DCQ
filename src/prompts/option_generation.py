class OptionGeneration:
    def __init__(self):
        self.prompts = {
            "option_generation_prompt": """Your task is to create a four-choice quiz by replacing the words in the provided INPUT TEXT with their contextually relevant synonyms.
The meaning and sentence structure of the four options MUST EXACTLY match every detail in the INPUT TEXT.
You MUST NOT include the provided INPUT TEXT as an option.

You MUST make sure that:
(1) You generate DISTINCT options based on the provided INPUT TEXT;
(2) The ONLY difference between options is WORD-LEVEL PERTURBATIONS.
(3) Options are ORDERED;
(4) There is NOT any extra explanation;
(5) You follow the following FORMAT to generate options;
(6) You comply with every specific symbol and letter detail in the given INPUT TEXT; and
(7) All options retain the EXACT LABEL from the INPUT TEXT, if there is one.
---
INPUT TEXT:
{original_instance}
---
FORMAT:

A)
First word-level perturbation goes here

B)
Second word-level perturbation goes here

C)
Third word-level perturbation goes here

D)
Fourth word-level perturbation goes here
---
"""
        }

    def get_prompt(self, prompt_type):
        return self.prompts.get(prompt_type, "Invalid prompt type")
