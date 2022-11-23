import pandas as pd
    
df = pd.read_csv("labeled_reviews.csv", delimiter= ',')

df_fake = df[(df.Fake == 1)]
df_real = df[(df.Fake == 0)]

df_fake_sample = df_fake.sample(n=800)
#df_fake_sample = df_fake_sample.reset_index(drop=True)

df_real_sample = df_real.sample(n=800)
#df_real_sample = df_real_sample.reset_index(drop=True)

df_final = pd.concat([df_fake_sample, df_real_sample])
df_final = df_final.reset_index(drop=True)
df_final = df_final.drop('Unnamed: 0', axis=1)

df_final.to_csv("finalized_reviews.csv", index=False)