# feature-extracter
该项目主要用于辅助特征抽取的工作
默认使用jieba中文分词的方式处理文本


# Quick Start
### InformationGain
利用信息增益的方式进行特征抽取

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
    print each[0], each[1]
```

### TfIdf
利用TfIdf的方式进行特征抽取
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
