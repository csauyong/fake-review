import pandas as pd

file_list = [
    "盛夏未来_labeled.csv", "这个杀手不太冷静_labeled.csv", 
    "心灵奇旅_labeled.csv", "送你一朵小红花_labeled.csv", 
    "独行月球_labeled.csv", "一周的朋友_labeled.csv",
    "唐人街探案3_labeled.csv", "花木兰_labeled.csv",
    "一点就到家_labeled.csv"]

positive_df = 0
negative_df = 0
total_positive_df = 0
total_negative_df = 0

for file_name in file_list:
    df = pd.read_csv(file_name, delimiter= ',')
    positive_df = len(df[(df.Fake == 1)])
    negative_df = len(df[(df.Fake == 0)])
    total_positive_df += positive_df
    total_negative_df += negative_df
    print(file_name, "positive no:", positive_df)
    print(file_name, "negative no:", negative_df)

print("Total positive no:", total_positive_df)
print("Total negative no:", total_negative_df)