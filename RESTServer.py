from flask import Flask, jsonify, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from transformers import CanineTokenizer, CanineModel
import json

class TextVectorRequest():
    workload: str

class TextVectorResponse():
    vector: list

    def __init__(self, vector):
        self.vector = vector

    def serialize(self):
        return {"vector": json.dumps(self.vector)}

print("Load model...")
model = CanineModel.from_pretrained('google/canine-c')

print("Load tokenizer...")
tokenizer = CanineTokenizer.from_pretrained('google/canine-c')

print("start REST-server")
app = Flask(__name__)

@app.route('/encoding', methods=['POST'])
def compute_sentiment():
    request_data = request.get_json()
    inputs = request_data['workload']
    print("inputs", type(inputs), inputs)
    encoding = tokenizer(inputs, return_tensors="pt") #, padding="longest", truncation=True)
    #print("encoding", type(encoding), encoding)
    outputs = model(**encoding)
    #print("outputs", type(outputs), outputs)
    pooled_output = outputs.pooler_output
    #print("pooled_output", type(pooled_output), pooled_output.size(), pooled_output)
    list_data = pooled_output.detach().numpy().tolist()
    #print("list_data", type(list_data), list_data)
    ret_val = TextVectorResponse(list_data)
    #print("ret_val", type(ret_val), ret_val)
    return jsonify(ret_val.serialize()), 200

if __name__ == '__main__':
    app.run(debug=False, port=8092)
