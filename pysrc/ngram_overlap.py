###############################################################
#
#  author Li Qi
#  mail stormier@126.com
#
#
###############################################################
import nltk



def unigram_overlap(sent1_nonstop_word, sent2_nonstop_word):
    """
    get nonstop word overlap feature
    """
    num = 0
    for word in sent1_nonstop_word:
        if sent2_nonstop_word.count(word) != 0:
            num += 1
    return float(num) / len(set(sent1_nonstop_word+(sent2_nonstop_word)))

def bigram_overlap(sent1_tokens,sent2_tokens):
    """
    get bigram overlap feature
    """
    sent1_bigram=[]
    sent2_bigram=[]
    for i in range(len(sent1_tokens)-1):
         sent1_bigram.append(sent1_tokens[i]+sent1_tokens[i+1])
    for i in range(len(sent2_tokens)-1):
         sent2_bigram.append(sent2_tokens[i]+sent2_tokens[i+1])    
    
    num = 0
    for bigram in sent1_bigram:
        if sent2_bigram.count(bigram) != 0:
            num += 1
    return float(num) / len(set(sent1_bigram+sent2_bigram))

def trigram_overlap(sent1_tokens,sent2_tokens):
    """
    get trigram overlap feature
    """
    sent1_trigram=[]
    sent2_trigram=[]
    for i in range(len(sent1_tokens)-2):
         sent1_trigram.append(sent1_tokens[i]+sent1_tokens[i+1]+sent1_tokens[i+2])
    for i in range(len(sent2_tokens)-2):
         sent2_trigram.append(sent2_tokens[i]+sent2_tokens[i+1]+sent2_tokens[i+2])    
    
    num = 0
    for trigram in sent1_trigram:
        if sent2_trigram.count(trigram) != 0:
            num += 1
    return float(num) / len(set(sent1_trigram+sent2_trigram))

def fourgram_overlap(sent1_tokens,sent2_tokens):
    """
    get fourgram overlap feature
    """
    if len(sent1_tokens) < 4 or len(sent2_tokens) < 4:
        return 0;
    sent1_fourgram=[]
    sent2_fourgram=[]
    for i in range(len(sent1_tokens)-3):
         sent1_fourgram.append(sent1_tokens[i]+sent1_tokens[i+1]+sent1_tokens[i+2]+sent1_tokens[i+3])
    for i in range(len(sent2_tokens)-3):
         sent2_fourgram.append(sent2_tokens[i]+sent2_tokens[i+1]+sent2_tokens[i+2]+sent2_tokens[i+3])    
    
    num = 0
    for fourgram in sent1_fourgram:
        if sent2_fourgram.count(fourgram) != 0:
            num += 1
    return float(num) / len(set(sent1_fourgram+sent2_fourgram))



