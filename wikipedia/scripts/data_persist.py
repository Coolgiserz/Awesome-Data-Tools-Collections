from dao import Dao
import pandas as pd
if __name__ == "__main__":
    d = Dao()
    df = pd.read_excel("citys.xlsx")
    print(df.shape)
    print(df.columns)
    # assert 1==2
    for data in df.itertuples():
        name = getattr(data, "title")
        intro = getattr(data, "intro")
        print(f"processing {name}")
        # d.write_province_intro(name, intro)
        d.write_city_intro(name, intro)