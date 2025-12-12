#Import Statements
import pandas as pd
import matplotlib.pyplot as plt

#Data Exploration

#q1
df = pd.read_csv('QueryResults.csv',names = ['Date','Tag','Post'],header = 0)
#q2
df.head()
df.tail()
#q3
df.shape
#q4
df.count()
#q5
df.groupby('Tag').sum().sort_values('Post',ascending=False)
#q6
df.groupby('Tag').count()


#Data Cleaning
#q7
type(df.Date[1])
df['Date'] = pd.to_datetime(df['Date'])
df.head()


#Data Manipulation

#q8
reshaped_df = df.pivot(index='Date', columns='Tag', values='Post')
#q9
reshaped_df.shape
reshaped_df.columns
reshaped_df.head()
reshaped_df.count()

#Data Visualisaton with with Matplotlib

#q10
plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
for col in reshaped_df.columns:
  plt.plot(reshaped_df.index,reshaped_df[col],linewidth=3, label=reshaped_df[col].name)

plt.legend(fontsize=16)

#q11
roll_df = reshaped_df.rolling(window=6).mean()
 
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], 
             linewidth=3, label=roll_df[column].name)
 
plt.legend(fontsize=16)


