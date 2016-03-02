###############################################################
#
#  author Li Qi
#  mail stormier@126.com
#
#
###############################################################
import nltk
from nltk.corpus import stopwords

def nnp_overlap(pos1,pos2):
    """
    get proper noun overlap feature
    """
    nnp1 = []
    nnp2 = []
    for word_tuple in pos1:
        if word_tuple[1] == 'NNP' or word_tuple[1] == 'NNPS' :
            nnp1.append(word_tuple[0])
    for word_tuple in pos2:
        if word_tuple[1] == 'NNP' or word_tuple[1] == 'NNPS' :
            nnp2.append(word_tuple[0])
    num = 0
    for noun in nnp1:
        if nnp2.count(noun) != 0:
            num += 1
    return float(num + 1) / (len(set(nnp1+nnp2)) + 1)

def ne_overlap(pos1,pos2):
    """
    get name entity overlap feature
    """
    ne1 = []
    ne2 = []
    for item in nltk.ne_chunk(pos1):
        if type(item) == nltk.tree.Tree:
            ne1.append(item.pop()[0])
    for item in nltk.ne_chunk(pos2):
        if type(item) == nltk.tree.Tree:
            ne2.append(item.pop()[0])
    num = 0 
    for ne in ne1:
        if ne2.count(ne) != 0:
            num += 1
    return float(num + 1) / (len(set(ne1+ne2)) + 1)
    
    
    
    