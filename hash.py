# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:19:23 2015

@author: tanay
"""

keys = ['a', 'b', 'c'] 
values = [1, 2, 3] 
hash = {k:v for k, v in zip(keys, values)} 
hash 
map(hash, ['0','1','2','3'])
hash('0')

import hashlib
hashlib.md5('a').digest()
hashlib.md5('a').hexdigest()
hashlib.sha512('a').hexdigest()