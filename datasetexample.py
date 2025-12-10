#----------------------------------
#write and read large datasets using python packages
#School test score veiwing system
#-----------


import random

#import csv module
import csv

#import os module
import os 

#import pandas package and give it the short name "pd"
import pandas as pd

def create_large_dataset(file_name, num_rows=1000):
    #open the file in write mode (w) and use the newlines=""
    with open(file_name, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file) #create a csv writer object that will help us write rows

        #write the header row (colum names)
        writer.writerow(["user_id", "test_number",  "score", "time_spent"])

        for i in range(1, num_rows + 1):
            user_id = f"user_{(i % 50) + 1}" #for user id we will just number users from 1 to 50 and repeat

            test_number = i

            score = random.randint(1, 100)

            time_spent = random.randint(0,100)

            #write a row of data into the csv file
            writer.writerow([user_id, test_number, score, time_spent])

    print(f"[INFO] createed large dataset: '{file_name} with {num_rows} rows'")


def load_dataset(file_name):
    df = pd.read_csv(file_name)

    print(f"[INFO] Loaded dataset from '{file_name}'.")
    return df


#----------
def format_dataset(df):

    df = df.rename(
        columns={
            "user_id": "UserID",
            "test_number": "TestNumber",
            "score": "Score",
            "time_spent": "TimeSpent",
        }
    )

    def categorize_score(score_value):
        if score_value < 50:
            return "low"
        elif score_value < 80:
            return "moderate"
        else:
            return "high"
        
    df["skill_level"] = df["Score"].apply(categorize_score)

    return df

def display_results(df):
    print("\n==============================")
    print(" SAMPLE OF FORMATTED DATA")
    print("==============================")
    print(df.head(10))

    print("\n====================================")
    print(" SUMMARY STATISTICS")
    print("======================================")

    print(df.describe())

    print("\n=====================================")
    print(" SKILL LEVEL COUNTS")
    print("===============================")

    print(df["skill_level"].value_counts())

    print("\n[INFO] Display completed. You have successfully read and formatted a large dataset")


def main():
    file_name = "grade_tracker.csv"

    print("=========================")
    print("LARGE GRADE TRACKER DEMO")
    print("=========================")

    if not os.path.exists(file_name):
        print(f"[INFO] '{file_name}' nnot found. Creating a new large dataset...")
        create_large_dataset(file_name, num_rows=1000)

    else:
        print(f"[INFO] found existing file'{file_name}'. Using existing dataset.")

    df = load_dataset(file_name)

    df_formatted = format_dataset(df)

    display_results(df_formatted)

    print("\n[PROGRAM COMPLETE] Thank you for using the large dataset!")

if __name__ == "__main__":
    main()


