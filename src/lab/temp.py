

'''
Author: hibana2077 hibana2077@gmail.com
Date: 2023-06-14 22:17:30
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-06-16 19:31:25
FilePath: \smart_hydroponic_farm\src\lab\temp.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import threading
global n

class update1(threading.Thread):
    def run(self):
        global n
        x=n
        x=2*n
        n=x
class update2(threading.Thread):
    def run(self):
        global n
        x=n
        x=n+1
        n=x
n=1
t1=update1()
t2=update2()
t1.start()
t2.start()
t1.join()
t2.join()
print(n)

