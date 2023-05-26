import pandas as pd
import  random
import os
import sys


def start_questionnaire(csv_file_path):
    try:
        df = pd.read_csv(csv_file_path)
        list1 = list(range(int(df.size/2)))
        random.shuffle(list1)


        for i in list1:
            answer1 = str(input(f'Question: {df["QUESTIONS"][i]} \n'))
            if str(answer1).upper() ==str(df["QUESTIONS"][i]).upper():
                print("Correct")
            else:
                print("Not Correct")
        
    
    except Exception as e:
        print("Error occured in start questionnaire")
        sys.exit(-1)
            
            
            
csv_file_path = input("Enter your csv file Path")
if os.path.exists(csv_file_path):
    start_questionnaire(csv_file_path)
else:
    print("File path does not exist . Check path ",str(csv_file_path))
    
print("Congratulation  Game Completed")
  