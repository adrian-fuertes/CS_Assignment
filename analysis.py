import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("istherecorrelation.csv",sep=";")
new_list = []
for item in list(df["WO [x1000]"]):
    item_1=item
    string = item_1.replace('.', '')
    string = item_1.replace(',', '.')
    new_list.append(float(string))
df["why_not_just_give_int"]=new_list

ax = df.plot(x="Year", y=["NL Beer consumption [x1000 hectoliter]", "why_not_just_give_int"],color=["white","black"])
ax.legend(["plotting is quite","hard :("])
ax.set_facecolor("lightslategray")
