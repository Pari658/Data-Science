#Question 1
df.shape[0]

#Question 2
df.shape[1]

#Question 3
df.columns

#Question 4
df.findna()

#Question 5
df.loc[df["Mid-Career Median Salary"].idxmax(), 
        ["Undergraduate Major", "Mid-Career Median Salary"]]

#Question 6
df.loc[df["Starting Median Salary"].idxmin(), 
       ["Undergraduate Major", "Starting Median Salary"]]

#Question 7
df.loc[df["Mid-Career Median Salary"].idxmin(), 
       ["Undergraduate Major", "Mid-Career Median Salary"]]

#Question 8
df.sort_values(
    by="Mid-Career 90th Percentile Salary", 
    ascending=False
).head(5)[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]]

#Question 9
df["Salary Spread"] = df["Mid-Career 90th Percentile Salary"] - df["Mid-Career 10th Percentile Salary"]

df.sort_values(by="Salary Spread", ascending=False).head(10)[
    ["Undergraduate Major", "Salary Spread"]
]

#Question 10
df.groupby("Group")["Mid-Career Median Salary"].mean()

#Question 11
df.groupby("Group").mean(numeric_only=True)
