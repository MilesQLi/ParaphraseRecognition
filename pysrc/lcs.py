###############################################################
#
#  author Li Qi
#  mail stormier@126.com
#
#
###############################################################
def LCS(x, y):
    if (len(x) == 0 or len(y) == 0):
        return 0
    else:
        if (x[0] == y[0]):
            return LCS(x[1:], y[1:])+1
        else:
            return 0

def max_LCS(x,y):
    """
    calculate Longest Common Substring
    """
    max_cl = 0
    #print("lenx:%d,leny:%d"%(len(x),len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            #print i,j
            temp = LCS(x[i:],y[j:])
            if temp > max_cl:
                max_cl = temp       
    return max_cl