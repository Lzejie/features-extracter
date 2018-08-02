# feature-extracter
该项目主要用于辅助特征抽取的工作
默认使用jieba中文分词的方式处理文本


# Quick Start
快速安装
```shell
sudo pip install features-extracter
```

### InformationGain
利用信息增益的方式进行特征抽取

信息增益的大体思想就是在多类文本中找出区分度最高的词，区分度越高，分数也越高

```python
from extracter import InformationGain

sentences = [
    '我想吃红烧牛肉',
    '我想吃牛肉拉面',
    '我想要去旅游',
    '我旅游去的大理了',
    '那个牛肉挺好吃的',
    '下次去玩想去海南'
]

labels = [
    '饮食',
    '饮食',
    '旅行',
    '旅行',
    '饮食',
    '旅行'
]

ig = InformationGain(sentences, labels)

for each in ig.get_top(10):
    print(each[0], each[1])
```

### TfIdf
利用TfIdf的方式进行特征抽取。

这里的大概实现思路是计算出所有文本的tfidf值，然后从每条文本中筛选最重要的n个词语。

然后统计出现次数最多的N个词。

```python
from extracter import TfIdf

sentences = [
    '我想吃红烧牛肉',
    '我想吃牛肉拉面',
    '我想要去旅游',
    '我旅游去的大理了',
    '那个牛肉挺好吃的',
    '下次去玩想去海南'
]

tfidf = TfIdf(sentences)

for each in tfidf.get_top(10):
    print(each[0], each[1])
```
