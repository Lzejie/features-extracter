# feature-extracter
该项目主要用于辅助特征抽取的工作

## InformationGain
利用信息增益的方式进行特征抽取

```python
from ig import InformationGain

sentences = [
    u'我想吃牛肉',
    u'我想吃饺子',
    u'我要去旅游',
    u'我去了大理'
]

labels = [
    u'饮食',
    u'饮食',
    u'旅行',
    u'旅行'
]

ig = InformationGain(sentences, labels)

```