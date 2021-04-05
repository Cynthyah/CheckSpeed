''' Plot the speed of Download and Upload getting during some intervals
    from file saved with the information '''

import os
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame


def get_data():
    file = "Files/checkspeed.csv"
    df: DataFrame = pd.DataFrame()
    if not os.path.isfile(file):
        print(f"{file} not found !")
    else:
        df = pd.read_csv(file)
    return df

def plot_speed():
    df = get_data()
    if len(df) == 0: # return empty df
        return
    plt.style.use('ggplot')
    plt.figure(figsize=(15,8))
    plt.title(f"Speed Download and Upload", fontsize = 20 )
    plt.plot(df["Date"]+ " at " + df["Time"], df["Download"],color = "red",label = "Download")
    plt.plot(df["Date"]+ " at " + df["Time"], df["Upload"],color = "blue", label = "Upload")
    plt.legend()
    plt.ylabel("Mbps",fontsize=20)
    plt.xticks(rotation=45,fontsize=8)
    plt.show()

if __name__ == "__main__":
   plot_speed()
