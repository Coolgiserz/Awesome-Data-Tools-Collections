# @Author: weirdgiser
# @Time: 2024/2/1
# @Function:
import os
import settings
from core.backend._bokeh.bar import BaseBarProxy
import pandas as pd
DATA_DIR = os.path.join(settings.BASE_DIR, "data", "王者荣耀英雄属性数据")

class HeroModel():
    def __init__(self, name, hp1, hp15):
        self.name = name
        self.hp1 = hp1
        self.hp15 = hp15

class HeroModelCollections:
    def __init__(self):
        self.collection = []

    def add_hero_models(self, models):
        self.collection = self.collection.extend(list(models))

    def sort_collection(self, **kwargs):
        # TODO
        pass

def visual_hp1():
    df_hero_out = pd.read_csv(os.path.join(DATA_DIR, "hero_out.csv"),encoding="gbk")
    df_hero_out_sorted = df_hero_out.sort_values(by="1级生命", ascending=False)
    bbp = BaseBarProxy(df_hero_out_sorted["名称"].iloc[:10], y_data=df_hero_out_sorted["1级生命"].iloc[:10])
    bbp.vbar(title="1级生命")



def visual_hp1_o(duty="射手", top_N=20, title="王者荣耀射手英雄1级生命值"):
    df_hero_out = pd.read_csv(os.path.join(DATA_DIR, "hero_out.csv"), encoding="gbk")
    df_hero_out_sorted = df_hero_out[df_hero_out["定位"]==duty].sort_values(by="1级生命", ascending=False)
    bbp = BaseBarProxy(df_hero_out_sorted["名称"].iloc[:top_N], y_data=df_hero_out_sorted["1级生命"].iloc[:top_N])
    bbp.vbar(title=title, x_axis_label="英雄名称", y_axis_label="1级生命值")


def visual_hp1_o_common(duty="射手", top_N=20, y_axis_label="1级物理攻击", output_filename=None):
    """
    可视化某一职业英雄的某一属性，按属性值大小降序排列
    :param duty:
    :param top_N:
    :param y_axis_label:
    :param output_filename:
    :return:
    """
    df_hero_out = pd.read_csv(os.path.join(DATA_DIR, "hero_out.csv"), encoding="gbk")
    df_hero_out_sorted = df_hero_out[df_hero_out["定位"]==duty].sort_values(by=y_axis_label, ascending=False)
    bbp = BaseBarProxy(df_hero_out_sorted["名称"].iloc[:top_N], y_data=df_hero_out_sorted[y_axis_label].iloc[:top_N])
    bbp.vbar(title=f"王者荣耀{duty}{y_axis_label}",
             x_axis_label="英雄名称",
             y_axis_label=y_axis_label,
             output_filename=output_filename)

def main():
    dutys=["射手", "法师", "坦克", "战士", "辅助", "刺客"]
    y_axis_labels = ["1级生命", "1级物理攻击", "15级生命", "15级物理攻击", "1级物理防御", "15级物理防御"]
    for duty in dutys:
        for y in y_axis_labels:
            filename = os.path.join("output", f"{duty}-{y}.png")
            visual_hp1_o_common(duty=duty, y_axis_label=y, output_filename=filename)
    print("Done!")

if __name__ == "__main__":
    main()