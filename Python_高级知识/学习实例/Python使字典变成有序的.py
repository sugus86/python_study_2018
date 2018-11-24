#字典本身是无序的，当需要有序的使用字典时，可以借助collections模块中的OrderedDict类。
#在迭代操作是它会保持元素被插入时的顺序：
#例如：

import json
from collections import OrderedDict
dic_normal = {'a': 1, 'b': 2, 'c': 3}
dic_order = OrderedDict()
dic_order['a'] = 1
dic_order['b'] = 2
dic_order['c'] = 3
print (json.dumps(dic_normal))
print (json.dumps(dic_order))