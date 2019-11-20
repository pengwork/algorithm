import numpy as np
import math

x = [1, 4, 6, 7]
y = [2, 3, 3, 4]
r = 4
count = [] 
center = [] # 圆心位置

i = 0
j = 0
while i < len(x):
    center.append(x[i] + math.sqrt(16 - y[i]**2)) # 圆心的x坐标；由于在x轴上，所有圆心y坐标为0
    print(center[j])

    count.append(0)
    k = 0
    while ((i+k) < len(x) and math.sqrt((x[i+k]-center[j])**2 + y[i+k]**2) <= r ): # 在当前的圆center[i]中，找半径r内的点
        count[j] += 1
        k += 1
    i += count[j]
    print("第",j+1,"个圆的圆心坐标为:(",center[j],", 0)；其中有",k,"个点")
    j += 1