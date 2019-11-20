# 1代表黑色，0代表白色
seq = [1, 1, 0, 1, 0, 0, 0, 1]

for k in range(len(seq)-1): # 点之间的间隔 最小为1 最大为序列长度减1
    for i in range(len(seq) - k):
        if (seq[i] == 1 and seq[i+k] == 0) or (seq[i] == 0 and seq[i+k] == 1):
            print(i+1,"和",i+k+1,"为一对")
            seq[i] = float("inf")
            seq[i+k] = float("inf")