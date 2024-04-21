# https://huggingface.co/google/canine-c
from transformers import CanineTokenizer, CanineModel
import json

model = CanineModel.from_pretrained('google/canine-c')
tokenizer = CanineTokenizer.from_pretrained('google/canine-c')

inputs = ["Life is like a box of chocolates.",
          "A broown fox jumps over the lazy dog.",
          "A blue fox jumps over the lazy dog.",
          "You never know what you gonna get."]
encoding = tokenizer(inputs, padding="longest", truncation=True, return_tensors="pt")
print("encoding", type(encoding), encoding)

outputs = model(**encoding) # forward pass
print("outputs", type(outputs), outputs)

pooled_output = outputs.pooler_output
print("pooled_output", type(pooled_output), pooled_output.size(),  pooled_output)

sequence_output = outputs.last_hidden_state
print("sequence_output", type(sequence_output), sequence_output.size(), sequence_output)

list_data = pooled_output.detach().numpy().tolist()
json_output = json.dumps(list_data)
print("REST-response", json_output)