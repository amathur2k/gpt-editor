#!/venv/bin/python
import os

from openai import OpenAI
from flask import Flask, request
app = Flask(__name__)

client = OpenAI(
    # This is the default and can be omitted
    #api_key= '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',
    #api_key=os.environ.get('OAI_API_KEY')
)

@app.route('/')
def hello():
    return 'Hello there'

@app.route('/call_gpt/<prompt>', methods=['POST', 'GET'])
def call_gpt(prompt):
    #if (request.args.get('prompt')):
        #return f'prompt found <br>'
    prompt = request.form.get('prompt')
    #prompt = request.get_json(force=True)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4-1106-preview",
    )
    content = chat_completion.choices[0].message.content
    return f'Hello there <br> {content}'
#    return f'Hello there <br> {prompt}'
# Keep this at the bottom of run.py
#app.run(debug=True)
if __name__ == "__main__":
    if os.environ.get('IS_CONTAINER') != 'true':
        app.run(debug=True)
    else:
        port = os.environ.get('PORT')
        if port == None:
            port = '5000'
        app.run(host=f'0.0.0.0:{port}')