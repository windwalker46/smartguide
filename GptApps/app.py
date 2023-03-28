from flask import Flask, render_template, request
import openai

openai.api_key = "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"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chatgpt():
    response = None
    if request.method == 'POST':
        content = request.form['user_input']
        messages = [{"role": "user", "content": "You're an IT guy, You will stay in character and answer the questions as if you were a real person. You will not say you are an AI model or make references to the fact you are an AI."}]
        messages.append({"role": "user", "content": content})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=100
        )
        response = completion.choices[0].message["content"]

    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
