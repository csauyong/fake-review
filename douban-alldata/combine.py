import pandas as pd

file_list = [
    "盛夏未来_labeled.csv", "这个杀手不太冷静_labeled.csv", 
    "心灵奇旅_labeled.csv", "送你一朵小红花_labeled.csv", 
    "独行月球_labeled.csv", "一周的朋友_labeled.csv",
    "唐人街探案3_labeled.csv", "花木兰_labeled.csv",
    "一点就到家_labeled.csv"]


count = 0
for file_name in file_list:
    if count==0:
        df = pd.read_csv(file_name, delimiter= ',')
    else:
        temp = pd.read_csv(file_name, delimiter= ',')
        df = pd.concat([df,temp])
    count += 1

'''
def toInteger(x):
    return int(x)

# apply Function to all columns in the same row
df.Fake = [toInteger(x) for x in df.Fake]
'''

print(list(df['Fake'].unique()))
print(df[df['Fake'].isnull()])

df = df.reset_index(drop=True)

with open("labeled_reviews.csv", 'w') as file:
    file.write(df.to_csv())
