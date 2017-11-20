# 定义按照关键词和词性进行更新的权值
keyvalue = 3
attrvalue = 1
# 定义关键词词性范围
keyword_set = ['nr', 'ns', 'n', 'nt', 'nz']
# 定义词性范围
attribute_set = ['nr', 'ns',  'm', 'q', 't', 'n', 'nt', 'nz']
# 定义词性词典
attribute_dict = {'nr': '人物', 'ns': '地点', 'm': '数字', 'q': '数字', 't': '时间',
                  'n': '实体', 'nt': '实体', 'nz': '实体'}
# 定义类别到词性的映射
cate_attr_dict = {'人物': ['nr'], '地点': ['ns'], '数字': ['m', 'q'],
                  '时间': ['t', 'm'], '实体': ['n', 'nt', 'nz'],
                  '描述': attribute_set}

