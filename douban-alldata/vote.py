import pandas as pd
import numpy as np 
import random



name_list = [
    "盛夏未来_labeled", "这个杀手不太冷静_labeled", 
    "心灵奇旅_labeled", "送你一朵小红花_labeled", 
    "独行月球_labeled", "一周的朋友_labeled",
    "唐人街探案3_labeled", "花木兰_labeled",
    "一点就到家_labeled"]

for name in name_list:
    file_name = name + "_fixed" + ".csv"
    new_file_name = name + ".csv"

    df = pd.read_csv(file_name, delimiter= ',').copy()

    df["Fake"] = 0

    vote_list = ["Marker1","Marker2","Marker3","Marker4","Marker5"]

    for i in range(len(df)):
        count = 0
        for vote in vote_list:
            if df[vote].iloc[i] == 1:
                count += 1
        if count>=3:
            df.at[i, "Fake"] = 1

    df = df[list(('movie_name','id','short_comment','score','comment_time','votes','Fake','Marker1','Marker2','Marker3','Marker4','Marker5'))]
            
    with open(file_name, 'w') as file:
        file.write(df.to_csv())

    df = df.drop('Marker1', axis=1)
    df = df.drop('Marker2', axis=1)
    df = df.drop('Marker3', axis=1)
    df = df.drop('Marker4', axis=1)
    df = df.drop('Marker5', axis=1)

    with open(new_file_name, 'w') as file:
        file.write(df.to_csv())
