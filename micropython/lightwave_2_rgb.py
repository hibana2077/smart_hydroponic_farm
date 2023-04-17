'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-04-04 09:28:12
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-04-12 13:15:08
FilePath: /smart_hydroponic_farm/micropython/lightwave_2_rgb.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

# Red = intensity * sin(wavelength * 0.024) ^ 2
# Green = intensity * sin(wavelength * 0.024 + 2 * pi / 3) ^ 2
# Blue = intensity * sin(wavelength * 0.024 + 4 * pi / 3) ^ 2
import math

def wave_2_rgb(wavelength, intensity):
    r = intensity * math.sin(wavelength * 0.024) ** 2
    g = intensity * math.sin(wavelength * 0.024 + 2 * math.pi / 3) ** 2
    b = intensity * math.sin(wavelength * 0.024 + 4 * math.pi / 3) ** 2
    return list(map(int, (r, g, b)))

#wavelength in nm, from 380 to 780
#intensity from 0 to 255
print(wave_2_rgb(380, 255))
#也只能這樣 反正沒有光譜儀