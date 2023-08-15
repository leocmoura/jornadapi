from bardapi import Bard
# import os

token = 'xxxx'
bard = Bard(token=token)

# Set your input text
input_text = "what is google bard? in 100 caractares"

# Send an API request and get a respons
bard_output = bard.get_answer(input_text)['content']
print(bard_output)

