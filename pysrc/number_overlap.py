###############################################################
#
#  author Li Qi
#  mail stormier@126.com
#
#
###############################################################

def num_overlap(pos1, pos2):
    """
    get number overlap feature
    """
    number1 = []
    number2 = []
    for word_tuple in pos1:
        if word_tuple[1] == 'CD':
            number1.append(word_tuple[0])
    for word_tuple in pos2:
        if word_tuple[1] == 'CD':
            number2.append(word_tuple[0])
    num = 0
    for number in number1:
        if number2.count(number) != 0:
            num += 1
    return float(num + 1) / (len(set(number1+number2)) + 1)