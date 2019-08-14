#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
ret=requests.get('http://www.bluecore.com.cn/').content

with open('a.html','wb',) as f:

        f.write(ret)