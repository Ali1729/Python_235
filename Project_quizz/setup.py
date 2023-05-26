import pandas as pd

df = pd.read_csv("Questions_And_Answers.csv")

for i in range(df.size/2):
    # answer1 = str(input(f'Question: {list1[i]} \n'))
    # if str(answer1).upper() ==str(list1[i-1]).upper():
    #     print("Correct")
    # else:
    #     print("Not Correct")
    df["QUESTIONS"][i]