###############################################################
#
#  author Li Qi
#  mail stormier@126.com
#
#
###############################################################


from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
import nltk
from nltk.corpus import stopwords

english_stopwords = stopwords.words('english')
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%', '_']


def path_best_sim(pos1,pos2, pos_map, pos_list):
    num = 0
    sent1_last = []
    sent2_last = []
    
    for word in pos1:
        if pos2.count(word) != 0:
            num += 1
        else:
            sent1_last.append(word)
    phi = 0.0
    for word in sent1_last:
        max_sim = 0.0
        if pos_list.count(word[1]) != 0 and pos_map[word[1]] != '':
            for syn in wn.synsets(word[0], pos = pos_map[word[1]]):  # @UndefinedVariable
                for word2 in pos2:
                    if pos_list.count(word2[1]) != 0 and pos_map[word2[1]] == pos_map[word[1]]:
                        for syn2 in wn.synsets(word2[0], pos_map[word2[1]]):  # @UndefinedVariable
                            try: 
                                if syn.path_similarity(syn2) > max:
                                    max_sim = syn.path_similarity(syn2)
                            except:
                                continue
        phi += max_sim
    part1 = (num + phi) / (len(pos1) + len(pos2))
    
    for word in pos2:
        if pos1.count(word) != 0:
            num += 1
        else:
            sent2_last.append(word)
    phi = 0.0
    for word2 in sent2_last:
        max_sim = 0.0
        if pos_list.count(word2[1]) != 0 and pos_map[word2[1]] != '':
            for syn2 in wn.synsets(word2[0], pos_map[word2[1]]):  # @UndefinedVariable
                for word in pos1:
                    if pos_list.count(word[1]) != 0 and pos_map[word2[1]] == pos_map[word[1]]:
                        for syn in wn.synsets(word[0], pos = pos_map[word[1]]):  # @UndefinedVariable
                            try:
                                if syn2.path_similarity(syn) > max:
                                    max_sim = syn.path_similarity(syn2)
                            except:
                                    continue
        phi += max_sim
    part2 = (num + phi) / (len(pos1) + len(pos2))
    return part1 + part2
    
def wup_best_sim(pos1, pos2, pos_map, pos_list):
    num = 0
    sent1_last = []
    sent2_last = []
    
    for word in pos1:
        if pos2.count(word) != 0:
            num += 1
        else:
            sent1_last.append(word)
    phi = 0.0
    for word in sent1_last:
        max_sim = 0.0
        if pos_list.count(word[1]) != 0 and pos_map[word[1]] != '':
            for syn in wn.synsets(word[0], pos = pos_map[word[1]]):  # @UndefinedVariable
                for word2 in pos2:
                   if pos_list.count(word2[1]) != 0 and pos_map[word2[1]] == pos_map[word[1]]:
                        for syn2 in wn.synsets(word2[0], pos_map[word2[1]]):  # @UndefinedVariable
                            try: 
                                if syn.wup_similarity(syn2) > max:
                                    max_sim = syn.wup_similarity(syn2)
                            except:
                                continue
        phi += max_sim
    part1 = (num + phi)/(len(pos1) + len(pos2))
    
    for word in pos2:
        if pos1.count(word) != 0:
            num += 1
        else:
            sent2_last.append(word)
    phi = 0.0
    for word2 in sent2_last:
        max_sim = 0.0
        if pos_list.count(word2[1]) != 0 and pos_map[word2[1]] != '':
            for syn2 in wn.synsets(word2[0], pos_map[word2[1]]):  # @UndefinedVariable
                for word in pos1:
                    if pos_list.count(word[1]) != 0 and pos_map[word2[1]] == pos_map[word[1]]:
                        for syn in wn.synsets(word[0], pos = pos_map[word[1]]):  # @UndefinedVariable
                            try:
                                if syn2.wup_similarity(syn) > max:
                                    max_sim = syn.wup_similarity(syn2)
                            except:
                                    continue
        phi += max_sim
    part2 = (num + phi) / (len(pos1) + len(pos2))
    return part1 + part2


def lch_best_sim(pos1, pos2, pos_map, pos_list):
    num = 0
    sent1_last = []
    sent2_last = []
    
    for word in pos1:
        if pos2.count(word) != 0:
            num += 1
        else:
            sent1_last.append(word)
    phi = 0.0
    for word in sent1_last:
        max_sim = 0.0
        if pos_list.count(word[1]) != 0 and pos_map[word[1]] != '':
            for syn in wn.synsets(word[0], pos = pos_map[word[1]]):  # @UndefinedVariable
                for word2 in pos2:
                    if pos_list.count(word2[1]) != 0 and pos_map[word2[1]] == pos_map[word[1]]:   
                        for syn2 in wn.synsets(word2[0], pos_map[word2[1]]):  # @UndefinedVariable
                            try: 
                                if syn.lch_similarity(syn2) > max:
                                    max_sim = syn.lch_similarity(syn2)
                            except:
                                continue
        phi += max_sim
    part1 = (num + phi) / (len(pos1) + len(pos2))
    
    for word in pos2:
        if pos1.count(word) != 0:
            num += 1
        else:
            sent2_last.append(word)
    phi = 0.0
    for word2 in sent2_last:
        max_sim = 0.0
        if pos_list.count(word2[1]) != 0 and pos_map[word2[1]] != '':
            for syn2 in wn.synsets(word2[0], pos_map[word2[1]]):  # @UndefinedVariable
                for word in pos1:
                    if pos_list.count(word[1]) != 0 and pos_map[word2[1]] == pos_map[word[1]]:
                        for syn in wn.synsets(word[0], pos = pos_map[word[1]]):  # @UndefinedVariable
                            try:
                                if syn2.lch_similarity(syn) > max:
                                    max_sim = syn.lch_similarity(syn2)
                            except:
                                    continue
        phi += max_sim
    part2 = (num + phi) / (len(pos1) + len(pos2))
    return part1 + part2
    
def lin_best_sim(pos1 ,pos2, dic, pos_map, pos_list):
    num = 0
    sent1_last = []
    sent2_last = []
    
    for word in pos1:
        if pos2.count(word) != 0:
            num += 1
        else:
            sent1_last.append(word)
    phi = 0.0
    for word in sent1_last:
        max_sim = 0.0
        if pos_list.count(word[1]) != 0 and pos_map[word[1]] != '':
            for syn in wn.synsets(word[0], pos = pos_map[word[1]]):  # @UndefinedVariable
                for word2 in pos2:
                    if pos_list.count(word2[1]) != 0 and pos_map[word2[1]] == pos_map[word[1]]:
                        for syn2 in wn.synsets(word2[0], pos_map[word2[1]]):  # @UndefinedVariable
                            try:
                                if syn.lin_similarity(syn2, dic) > max:
                                    max_sim = syn.lin_similarity(syn2, dic)
                            except:
                                continue
        phi += max_sim
    part1 = (num + phi)/(len(pos1) + len(pos2))
    
    for word in pos2:
        if pos1.count(word) != 0:
            num += 1
        else:
            sent2_last.append(word)
    phi = 0.0
    for word2 in sent2_last:
        max_sim = 0.0
        if pos_list.count(word2[1]) != 0 and pos_map[word2[1]] != '':
            for syn2 in wn.synsets(word2[0], pos_map[word2[1]]):  # @UndefinedVariable
                for word in pos1:
                    if pos_list.count(word[1]) != 0 and pos_map[word2[1]] == pos_map[word[1]]:
                        for syn in wn.synsets(word[0], pos = pos_map[word[1]]):  # @UndefinedVariable
                            try:
                                if syn2.lin_similarity(syn, dic) > max:
                                    max_sim = syn.lin_similarity(syn2, dic)
                            except:
                                continue
        phi += max_sim
    part2 = (num + phi) / (len(pos1) + len(pos2))
    return part1 + part2
    

def res_best_sim(pos1 ,pos2, dic, pos_map, pos_list):
    num = 0
    sent1_last = []
    sent2_last = []
    
    for word in pos1:
        if pos2.count(word) != 0:
            num += 1
        else:
            sent1_last.append(word)
    phi = 0.0
    for word in sent1_last:
        max_sim = 0.0
        if pos_list.count(word[1]) != 0 and pos_map[word[1]] != '':
            for syn in wn.synsets(word[0], pos = pos_map[word[1]]):  # @UndefinedVariable
                for word2 in pos2:
                    if pos_list.count(word2[1]) != 0 and pos_map[word2[1]] == pos_map[word[1]]:
                        for syn2 in wn.synsets(word2[0], pos_map[word2[1]]):  # @UndefinedVariable
                            try:
                                if syn.res_similarity(syn2, dic) > max:
                                    max_sim = syn.res_similarity(syn2, dic)
                            except:
                                continue
        phi += max_sim
    part1 = (num + phi)/(len(pos1) + len(pos2))
    
    for word in pos2:
        if pos1.count(word) != 0:
            num += 1
        else:
            sent2_last.append(word)
    phi = 0.0
    for word2 in sent2_last:
        max_sim = 0.0
        if pos_list.count(word2[1]) != 0 and pos_map[word2[1]] != '':
            for syn2 in wn.synsets(word2[0], pos_map[word2[1]]):  # @UndefinedVariable
                for word in pos1:
                    if pos_list.count(word[1]) != 0 and pos_map[word2[1]] == pos_map[word[1]]:
                        for syn in wn.synsets(word[0], pos = pos_map[word[1]]):  # @UndefinedVariable
                            try:
                                if syn2.res_similarity(syn, dic) > max:
                                    max_sim = syn.res_similarity(syn2, dic)
                            except:
                                continue
        phi += max_sim
    part2 = (num + phi) / (len(pos1) + len(pos2))
    return part1 + part2
    

def jcn_best_sim(pos1 ,pos2, dic, pos_map, pos_list):
    num = 0
    sent1_last = []
    sent2_last = []
    
    for word in pos1:
        if pos2.count(word) != 0:
            num += 1
        else:
            sent1_last.append(word)
    phi = 0.0
    for word in sent1_last:
        max_sim = 0.0
        if pos_list.count(word[1]) != 0 and pos_map[word[1]] != '':
            for syn in wn.synsets(word[0], pos = pos_map[word[1]]):  # @UndefinedVariable
                for word2 in pos2:
                    if pos_list.count(word2[1]) != 0 and pos_map[word2[1]] == pos_map[word[1]]:
                        for syn2 in wn.synsets(word2[0], pos_map[word2[1]]):  # @UndefinedVariable
                            try:
                                if syn.jcn_similarity(syn2, dic) > max:
                                    max_sim = syn.jcn_similarity(syn2, dic)
                            except:
                                continue
        phi += max_sim
    part1 = (num + phi)/(len(pos1) + len(pos2))
    
    for word in pos2:
        if pos1.count(word) != 0:
            num += 1
        else:
            sent2_last.append(word)
    phi = 0.0
    for word2 in sent2_last:
        max_sim = 0.0
        if pos_list.count(word2[1]) != 0 and pos_map[word2[1]] != '':
            for syn2 in wn.synsets(word2[0], pos_map[word2[1]]):  # @UndefinedVariable
                for word in pos1:
                    if pos_list.count(word[1]) != 0 and pos_map[word2[1]] == pos_map[word[1]]:
                        for syn in wn.synsets(word[0], pos = pos_map[word[1]]):  # @UndefinedVariable
                            try:
                                if syn2.jcn_similarity(syn, dic) > max:
                                    max_sim = syn.jcn_similarity(syn2, dic)
                            except:
                                continue
        phi += max_sim
    part2 = (num + phi) / (len(pos1) + len(pos2))
    return part1 + part2
