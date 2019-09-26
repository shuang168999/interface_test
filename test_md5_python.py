# -*- coding:utf-8 -*-

from md5_python import md5Python

param = {
    'c':'ccccccccc',
    'd':'ddddddddd',
    'e':'eeeeeeeee'
}

key = 'kkkkkkkkkk'

print('加密参数：' + md5Python.data_processing(param))
print('加密的完整请求串：' + md5Python.md5_sign_str(param,key))
print('加密生成的sign：' + md5Python.md5_sign(param,key))
print('请求信息：' + md5Python.md5_sign_str(param,key)+'&sign='+md5Python.md5_sign(param,key))