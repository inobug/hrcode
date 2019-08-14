import json
from collections import namedtuple

with open('data.json') as f:
        ret=json.load(f)
dic={}
for k in ret:
        if type(ret[k]) is int:
                dic[k]=ret[k]
dic=sorted(dic.items(),key = lambda x:x[1],reverse = True)
dic={i[0]:i[1] for i in dic}
with open('p2.txt','w',) as f:
        f.write(json.dumps(dic))
