from urllib import request,parse
import json
data = '''
[{"qqq": 1}, {"ppp": 2 }]
'''

print(type(data))
da = json.loads(data)
print(type(da))
print(da)