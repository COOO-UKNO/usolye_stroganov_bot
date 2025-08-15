import pandas as pd

df = pd.read_excel('bot_data.xlsx', sheet_name=0)


def voz(button_zavod):
    st3 = ""
    otv=[]
    for fir in range(0,100):
        value = df.iloc[fir, 0]
        if value == button_zavod:
            photo= df.iloc[fir, 3].split(";")
            for i in range(len(photo)):
                st3 += "photos/" +  photo[i]+";"
            otv = [df.iloc[fir, 1],df.iloc[fir, 2],st3.split(";")]
            break
    return(otv)
