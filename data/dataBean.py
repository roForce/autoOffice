# -*- coding: utf-8 -*-
# @Time    : 2023/10/19 10:45
# @Author  : Zhang Zhimin
# @File    : dataBean.py
import yaml
import pandas as pd
class dataBean:
    #初始化，从文件中读取数据的类型，一共有
    def __init__(self,num_type):
        self.type_config = self.readType()
        #不需要重新获取数据的类型和形式
        self.Element_type = self.type_config.get('ElementType')
        self.Multi_type = self.type_config.get('MultiType')
        #检查当前数据类型，合规则对数据进行初始化
        if self.checkType(num_type):
            #初始化dataBean文件
            self.data = self.type_config[num_type]
            print(self.data)
        else:
            print("数据初始化异常，请检查输入")


    def readType(self):
        with open(r'../data/datatype.yaml',encoding='utf-8') as f:
            #这里使用load,loadall是生成一个迭代器，不方便使用
            result = yaml.load(f.read(),Loader=yaml.FullLoader)

        print(result.get('ElementType'))
        #装载获取的数据类型,用于查看输入的数据类型和本来有的数据类型是否一直
        return result
    #用于检查输入的类型和当前的配置文件中有的数据类型是否一致，没有需要报警
    def checkType(self,num_type):
        if (num_type not in self.Multi_type) and (num_type not in self.Element_type):
            print('数据不在讨论的数据类型中，请检查是否是输入错误？')
            return False
        return True






    #根据数据的类型配合不同的测试方法
