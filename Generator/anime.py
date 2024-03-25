import pandas as pd
from datasets import load_dataset
import os


if not os.path.exists("anime_quotes.csv"):
    print("The Dataset not available let me create it for you ")
    dataset = load_dataset("hugginglearners/anime-quotes")

    
    split_to_convert = "train"

     
    data_list = []
    for quote in dataset[split_to_convert]:
         
        data_dict = {
            "Quote": quote["Quote"],
            "Character": quote["Character"]  ,
            "Anime":quote['Anime']
        }
        data_list.append(data_dict)

    
    df = pd.DataFrame(data_list)

     
    df.to_csv("anime_quotes.csv", index=False)  

    print(f"Anime quotes from '{split_to_convert}' split saved to anime_quotes.csv")
else:
    print(f"The Dataset Already Available")
