# encoding=utf-8

import re
import matplotlib.pyplot as plt
from scipy.misc import imread
import jieba.analyse
from wordcloud import WordCloud

# 读入背景图片
bg_pic = imread('mask.jpg')

# 读取一个txt文件
blog_path = r'../_posts/字典和集合.md'
text_source = ''
with open(blog_path, 'r', encoding='utf8') as f:
    text_source = f.read()

word_freq = dict(jieba.analyse.extract_tags(text_source, topK=100, withWeight=True))
# print(dict(word_freq))
wc = WordCloud(
    background_color='black',  # 背景底色
    mask=bg_pic,  # 设置背景图
    max_words=2000,  # 设置最大显示的字数
    font_path=r"C:\Windows\Fonts\AdobeHeitiStd-Regular.otf",
    # 设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
    max_font_size=200,  # 设置字体最大值
    random_state=50,  # 设置有多少种随机生成状态，即有多少种配色方案
)
myword = wc.generate_from_frequencies(word_freq) #生成词云

#展示词云图
# plt.imshow(myword,interpolation='bilinear')
# plt.axis("off")
# plt.show()

# 提取文件名
pattern = re.compile(r'(\w+).md')
out_img = re.search(pattern, blog_path).group(1)
# 导出图片
wc.to_file('{}.jpg'.format(out_img))