import pandas as pd

# Your input data
data = [
    ["Axel system", "", "", "", "A00000001"],
    ["Axel system", "Front Axel", "", "", "A00000002"],
    ["Axel system", "Front Axel", "FR Wheel", "", "A00000003"],
    ["Axel system", "Front Axel", "FR Wheel", "Rim", "A00000004"],
    ["Axel system", "Front Axel", "FR Wheel", "Tyre", "A00000005"],
    ["Axel system", "Front Axel", "FR Wheel", "Tube", "A00000006"],
    ["Axel system", "Front Axel", "FL Wheel", "", "A00000007"],
    ["Axel system", "Front Axel", "FL Wheel", "Rim", "A00000008"],
    ["Axel system", "Front Axel", "FL Wheel", "Tyre", "A00000009"],
    ["Axel system", "Front Axel", "FL Wheel", "Tube", "A00000010"],
    ["Axel system", "Rear Axel", "", "", "A00000011"],
    ["Axel system", "Rear Axel", "RR Wheel", "", "A00000012"],
    ["Axel system", "Rear Axel", "RR Wheel", "Rim", "A00000013"],
    ["Axel system", "Rear Axel", "RR Wheel", "Tyre", "A00000014"],
    ["Axel system", "Rear Axel", "RR Wheel", "Tube", "A00000015"],
    ["Axel system", "Rear Axel", "RL Wheel", "", "A00000016"],
    ["Axel system", "Rear Axel", "RL Wheel", "Rim", "A00000017"],
    ["Axel system", "Rear Axel", "RL Wheel", "Tyre", "A00000018"],
    ["Axel system", "Rear Axel", "RL Wheel", "Tube", "A00000019"]
]

columns = ["Component 1", "Component 2", "Component 3", "Component 4", "Part Number"]

df = pd.DataFrame(data, columns=columns)
df = df.set_index(["Component 1", "Component 2", "Component 3",], drop=False) 


df["Depth"] = df.apply(lambda row: sum(1 for x in row if x), axis=0)

df["Hierarchy"] = df.apply(lambda row: "||".join(filter(None, row[:-2])), axis=1)

df=df [["Component 1", "Component 2", "Component 3", "Component 4", "Depth","Part Number","Hierarchy",]]

df = df.set_index(["Component 1", "Component 2", "Component 3",],drop=False)

df.to_excel("first4.xlsx", index=False)


