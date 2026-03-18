import pandas as pd

def score_leads(row):
    score = 0

    if row["Company_Size"] > 200:
        score += 30
    elif row["Company_Size"] > 50:
        score += 20
    else:
        score += 10

    if row["Budget"] > 50000:
        score += 30
    elif row["Budget"] > 20000:
        score += 20
    else:
        score += 10

    if row["Engagement_Score"] > 70:
        score += 40
    elif row["Engagement_Score"] > 40:
        score += 20
    else:
        score += 10

    return score

df = pd.read_csv("data/sample_leads.csv")

df["Lead_Score"] = df.apply(score_leads, axis=1)

df["Priority"] = pd.cut(
    df["Lead_Score"],
    bins=[0, 40, 80, 120],
    labels=["Low", "Medium", "High"]
)

print(df)
