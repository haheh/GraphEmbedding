import numpy as np


def create_alias_table(area_ratio):
    """

    :param area_ratio: sum(area_ratio)=1
    :return: accept,alias
    """
    l = len(area_ratio)
    accept, alias = [0] * l, [0] * l
    small, large = [], [] #存id/索引
    area_ratio_ = np.array(area_ratio) * l #数组创建
    for i, prob in enumerate(area_ratio_):
        if prob < 1.0:
            small.append(i)
        else:
            large.append(i)

    while small and large:
        small_idx, large_idx = small.pop(), large.pop() #pop()用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        accept[small_idx] = area_ratio_[small_idx] #索引为small_idx对应的小于1的面积
        alias[small_idx] = large_idx #索引为small_idx对应的大于1的索引
        area_ratio_[large_idx] = area_ratio_[large_idx] - \
            (1 - area_ratio_[small_idx]) #剩余面积
        if area_ratio_[large_idx] < 1.0:
            small.append(large_idx)
        else:
            large.append(large_idx)

    while large:
        large_idx = large.pop()
        accept[large_idx] = 1
    while small:
        small_idx = small.pop()
        accept[small_idx] = 1

    return accept, alias


def alias_sample(accept, alias):
    """

    :param accept:
    :param alias:
    :return: sample index
    """
    N = len(accept)
    i = int(np.random.random()*N) #产生1-N之间的随机数i，决定落在哪一列
    r = np.random.random() #产生0-1之间的随机数
    if r < accept[i]:
        return i
    else:
        return alias[i]
