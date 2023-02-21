import openai
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=("GET","POST"))
def homePage():
    
    if request.method == "POST":
        
        input = request.form["input"]
        language = list(request.form.keys())[0]
        if language != "Human":
             
            if len(input) <= 750:

                response = openai.Completion.create(
                    model = "text-davinci-003",
                    prompt = generate_prompt(language, input),
                    max_tokens = 256,
                    temperature = 0.6,
                )
                return redirect(url_for("homePage", result=response.choices[0].text))

            else:       
                return redirect(url_for("homePage", result="Oops! that was too long to translate, please try again."))
        else:
            return redirect(url_for("homePage", result=""))
        
    result = request.args.get("result")
    return render_template('index.html', result=result)

def generate_prompt(language, input):

    return "You are roleplaying as a {}. Say \"{}\"".format(language, input)




