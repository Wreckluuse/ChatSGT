import openai
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=("GET","POST"))
def homePage():
    if request.method == "POST":
        input = request.form["input"]
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = generate_prompt(input),
            temperature = 0.6,
        )
        return redirect(url_for("homePage", result=response.choices[0].text))
    
    result = request.args.get("result")
    return render_template('index.html', result=result)

def generate_prompt(language, input):
    return """You are a translator, please say
    the following sentence only using sounds and words a
    {} would make and without
    adding context at the end. {}
    """.format(language, input.capitalize())

if __name__ == "__main__":
    app.run(debug=True)



