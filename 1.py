import numpy as np

def greedy_algorithm(v, w, p):
    unit_value = v/w

    actual_capacity = 0
    actual_value = 0

    for i in range(0, len(unit_value)):
        if(actual_capacity + w[np.where(unit_value == unit_value.max())] > p):
            print("第",i,"次寻找单位价值最大的物品的总价值为：",actual_value + (p - actual_capacity)*unit_value.max())
            break
        else:
            actual_capacity += w[np.where(unit_value == unit_value.max())]
            actual_value += v[np.where(unit_value == unit_value.max())]
            print("第",i,"次寻找单位价值最大的物品的总价值为：", v[np.where(unit_value == unit_value.max())])
            unit_value[np.where(unit_value == unit_value.max())] = 0
                
        

        

if __name__ == "__main__":
    prod_value = np.array([2, 4, 8, 7])
    prod_weight = np.array([3, 4, 2, 6])
    package_capacity = 10

    greedy_algorithm(prod_value, prod_weight, package_capacity)


