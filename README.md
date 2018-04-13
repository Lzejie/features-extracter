# feature-extracter
该项目主要用于辅助特征抽取的工作

## InformationGain
利用信息增益的方式进行特征抽取

```python
from ig import InformationGain

sentences = [
    u'我想吃红烧牛肉',
    u'我想吃牛肉拉面',
    u'我想要去旅游',
    u'我旅游去的大理了',
    u'那个牛肉挺好吃的',
    u'下次去玩想去海南'
]

labels = [
    u'饮食',
    u'饮食',
    u'旅行',
    u'旅行',
    u'饮食',
    u'旅行'
]

ig = InformationGain(sentences, labels)

for each in ig.get_top(10):
    print each[0], each[1]
```