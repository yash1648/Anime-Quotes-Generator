from flask import Blueprint,render_template,request,jsonify
import pandas as pd
import random



route = Blueprint('blueprint',__name__)

@route.route("/",methods=['GET','POST'])
def  index():
    if  request.method == 'POST':
        print("Button pressed")
        df = pd.read_csv("Generator/anime_quotes.csv")


        random_quote_index = random.randint(0, len(df) - 1)
        random_quote = df.iloc[random_quote_index]


        quote = random_quote["Quote"]
        character = random_quote["Character"]
        
        doc={
            "Quote":quote,
            "Character":character
            
        }
        response = jsonify(doc)
        response.headers['Content-Type'] = 'application/json'
        return response
    
    return render_template('index.html')