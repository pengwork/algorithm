n = 3
c = [2, 5, 3] # 生产成本
y = [2, 4, 5] # 产品需求
x = [] # 该月需要生产的产品数量

cost = c[0] * y[0] # 第一个月的产品只能在第一个月生产不能更早了
print("第 1 月的",y[0],"件产品")
print("在第 1 月生产，花费是",cost)
for i in range(1, len(c)):
    print("第",i+1,"月的",y[i],"件产品")

    current_cost = c[i] * y[i] # 以本月自产自销的cost为基础，如果在前面某天生成成本更低，则在前面某天生产
    for j in range(0, i+1):
        if(current_cost > (c[j] + (i-j)*1) * y[i]): # i-j 就是中间相差了t天
            current_cost = ((c[j] + (i-j)*1) * y[i])
        print("在第",j+1,"月生产，当前产品最小花费是",current_cost)
    
    cost += current_cost
print("最少的花费是：", cost)