# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import yaml
dict_fruits={"orange":5,"apples":20,"banana":30}
with open(r'C:/Users/JCN/Desktop/Nameg/Hello_World/FruitsYAML.yaml', 'w') as file:
    documents = yaml.dump(dict_fruits, file)