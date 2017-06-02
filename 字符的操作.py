import re
import os
from collections import Counter
import random
full_text = []
def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')

path = GetDesktopPath()
with open(path + '\zmj-4396-86340\/3390.txt', 'r') as tangshi:
    for i in tangshi:
        full_text.append(i.replace(' ', '').replace('：', '').replace('！', '').replace('］', '').replace('［', '')
                         .replace('。', '').replace('\n', '').replace('？', '').replace('，', '').replace('-', ''))
# 字符串分割
word = ''.join(full_text)
word_str = re.sub(r"(?<=\w)", "", word)
word_list = list(word_str)
a = [v for v in word_list if not str(v).isdigit()]
# 全部字
c = Counter(a)
s = c.most_common(300)
ci = []
for i in s:
    ci.append(i[0])
i = random.sample(ci, 20)
print(i[0]+i[1]+i[2]+i[3]+i[4]+'，'+i[5]+i[6]+i[7]+i[8]+i[9]+'。'+'\n'+i[10]+i[11]
      +i[12]+i[13]+i[14]+'，'+i[15]+i[16]+i[17]+i[18]+i[19]+'。')
