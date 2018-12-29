__author__ = 'du'
# coding=utf-8

def O_nW(W, weight, value):
    OPT = [[0 for j in range(W + 1)] for i in range(len(weight) + 1)]
    for i in range(1, W + 1):
        for j in range(1, len(weight) + 1):
            if weight[j - 1] > i:
                OPT[j][i] = OPT[j - 1][i]
            else:
                v1 = OPT[j - 1][i]
                v2 = value[j - 1] + OPT[j - 1][i - weight[j - 1]]
                OPT[j][i] = max([v1, v2])
    max_l = [max(one) for one in OPT]
    print max(max_l)

    # 输出所选物品列表
    remainspace = W
    for i in range(len(weight), 0, -1):
        if remainspace >= weight[i - 1]:
            if OPT[i][remainspace] - OPT[i - 1][remainspace - weight[i - 1]] == value[i - 1]:
                remainspace -= weight[i - 1]
                print "goods: {} is selected!".format(i)


def O_n(W, weight, value):
    pass


if __name__ == "__main__":
    W = 11
    weight = [1, 2, 5, 6, 7]
    value = [1, 6, 18, 22, 28]
    O_nW(W, weight, value)


