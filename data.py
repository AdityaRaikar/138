import pandas as pd

def_1 =pd.read_csv("shared_articles.csv")
def_2 =pd.read_csv("user_interaction.csv")

def_1.rename(columns={'contentId':'id'},inplace=True)
result_def =pd.merge(def_1,def_2,on='id')

print(result_def.shape)
