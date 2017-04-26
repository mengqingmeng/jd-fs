##coding=utf-8

import re
def dealProductName(productName):
    removeKH =re.compile(r'[(【「（].*?[）」)】]')
    removedKH = removeKH.sub('',productName)
    #print(removedKH)
    removeNum = re.compile('[a-zA-Z0-9 | + ！!-\.\\ /]')
    return removeNum.sub('',removedKH)
    #result = removeNum.sub('',removedKH)
    #print(result)

#dealProductName("  姬芮(Za）新能真皙美白隔离霜35g(隔离紫外线 提亮肤色 防晒SPF26)")