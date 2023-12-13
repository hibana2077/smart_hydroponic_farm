'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-12-12 09:53:18
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-12-12 09:53:23
FilePath: /smart_hydroponic_farm/temp.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np

lambda_rate = 10  # 平均每小時10次
hours = 100       # 總共100小時
events = np.random.poisson(lambda_rate, hours)
print(events)
print(len(events))
