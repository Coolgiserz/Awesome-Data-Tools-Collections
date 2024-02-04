# @Author: weirdgiser
# @Time: 2024/1/31
# @Function: Word Cloud
import os.path
import settings
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import multidict
import re
import matplotlib.pyplot as plt
import jieba
from matplotlib import font_manager
for font in font_manager.fontManager.ttflist:
    print(font.name)
DATA_DIR = os.path.join(settings.BASE_DIR, "data", "王者荣耀英雄属性数据")
plt.rcParams["font.family"] = 'Arial Unicode MS'

plt.rcParams['font.sans-serif'] = ['SimHei']  # 替换为你所安装的字体名称
plt.rcParams['axes.unicode_minus'] = False

def makeImage(text):
    # 指定font_path， 否则中文乱码
    wc = WordCloud(background_color="white", max_words=1000, font_path="/System/Library/Fonts/Supplemental/Arial Unicode.ttf")
    # generate word cloud
    wc.generate_from_frequencies(text)
    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def skin_process():
    path = os.path.join(DATA_DIR, "王者荣耀英雄皮肤.csv")
    df = pd.read_csv(path)
    tmpDict = {}
    fullTermsDict = multidict.MultiDict()

    for text in df["口号"]:
        seg_list = jieba.cut(text)
        for seg in seg_list:
            if re.match("荣耀|王者|的|系列|赛季|年|之|撼|皮肤|主题|元|与|在|为|狗|合作|还原|风格|活动|五|中", seg):
                continue
            val = tmpDict.get(seg, 0)
            tmpDict[seg.lower()] = val+1
    for key in tmpDict:
        fullTermsDict.add(key=key, value=tmpDict[key])

    makeImage(fullTermsDict)


def attr_process():
    pass
def main():
    skin_process()

if __name__ == "__main__":
    main()