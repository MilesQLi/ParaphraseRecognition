###############################################################
#
#  author Li Qi
#  mail stormier@126.com
#
#
###############################################################

import sys
sys.path.append(r'./')
import codecs
import nltk
from nltk.corpus import wordnet_ic
from nltk.corpus import stopwords
from lcs import *
from sample import *
from get_pos_trans import *
from ngram_overlap import *
from ne_overlap import *
from number_overlap import *
from knowledge_based_similarity import *
from get_pos_trans import *
from dependency_similarity import *

#load brown dictionary
brown_ic = wordnet_ic.ic('ic-brown.dat')

#get resources map LDC POS to wordnet POS
pos_map = get_pos_map()
pos_list = get_pos_list()

# load Porter stemmer tool
porter = nltk.PorterStemmer()

#get English stopwords and punctions
english_stopwords = stopwords.words('english')
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%', '_']


def train_data_feature_extract(train_file,train_dependency_file):
    """
    load train data from train data file and extract features 
    return a sample list
    """
    train_f = codecs.open(train_file,'r', 'utf-8')
    train_dependency_f = codecs.open(train_dependency_file, 'r', 'utf-8')
    lines = train_f.readlines()
    dependency_lines = train_dependency_f.readlines()
    train_f.close()
    train_dependency_f.close()
    train_samples = []
    for i,(line, dependency_line) in enumerate(zip(lines,dependency_lines)):
        print i
        new_sample = sample()
        line = line.split('\t')
        dependency_line = dependency_line.split('\t')
        if line[0] == '0':
            new_sample.is_repeat = 0
        else:
            new_sample.is_repeat = 1
        new_sample.sent1_id = int(line[1])
        new_sample.sent2_id = int(line[2])
        assert line[1] == dependency_line[0]
        assert line[2] == dependency_line[1]
        #preprocessing of text:tokenization and stemming
        sent1 = [porter.stem(t) for t in nltk.word_tokenize(line[3])]
        new_sample.sent1 = sent1
        sent2 = [porter.stem(t) for t in nltk.word_tokenize(line[4])]
        new_sample.sent2 = sent2
        #filter stop words
        sent1_nonstop_word =  [word for word in sent1 if not word in english_stopwords and not word in english_punctuations]
        sent2_nonstop_word =  [word for word in sent2 if not word in english_stopwords and not word in english_punctuations]
        #get n-gram features
        new_sample.word_overlap = unigram_overlap(sent1_nonstop_word,sent2_nonstop_word)
        new_sample.bigram_overlap = bigram_overlap(sent1, sent2)
        new_sample.trigram_overlap = trigram_overlap(sent1, sent2)
        new_sample.fourgram_overlap = fourgram_overlap(sent1, sent2)
        #get lcs feature
        new_sample.lcs = float(max_LCS(sent1, sent2)) / min(len(sent1),len(sent2))
        #get length different feature
        new_sample.length_diff = float(abs(len(sent1)-len(sent2))) / min(len(sent1),len(sent2))
        #pos texts
        pos1 = nltk.pos_tag(sent1)
        pos2 = nltk.pos_tag(sent2)
        #filter stop words
        pos1_nonstop_word = [word for word in pos1 if not word[0] in english_stopwords and not word[0] in english_punctuations]
        pos2_nonstop_word = [word for word in pos2 if not word[0] in english_stopwords and not word[0] in english_punctuations]
        #get proper noun, name entity and number overlap feature
        new_sample.nnp_overlap = nnp_overlap(pos1,pos2)
        new_sample.ne_overlap = ne_overlap(pos1,pos2)
        new_sample.num_overlap = num_overlap(pos1,pos2)
        #get knowledge based features
        new_sample.path_best_sim = path_best_sim(pos1_nonstop_word, pos2_nonstop_word, pos_map, pos_list)
        new_sample.wup_best_sim = wup_best_sim(pos1_nonstop_word, pos2_nonstop_word, pos_map, pos_list)
        new_sample.lch_best_sim = lch_best_sim(pos1_nonstop_word, pos2_nonstop_word, pos_map, pos_list)
        new_sample.lin_best_sim = lin_best_sim(pos1_nonstop_word, pos2_nonstop_word, brown_ic, pos_map, pos_list)
        new_sample.res_best_sim = res_best_sim(pos1_nonstop_word, pos2_nonstop_word, brown_ic, pos_map, pos_list)
        new_sample.jcn_best_sim = jcn_best_sim(pos1_nonstop_word, pos2_nonstop_word, brown_ic, pos_map, pos_list)
        new_sample.dependency_sim = dependency_sim(dependency_line[2], dependency_line[3])
        #add sample to train sample set
        train_samples.append(new_sample)
    return train_samples

def dev_or_test_data_feature_extract(data_file,dependency_file):
    """
    load dev or test data from dev or test data file and extract features 
    return a sample list
    """
    dev_f = codecs.open(data_file, 'r', 'utf-8')
    dev_dependency_f = codecs.open(dependency_file, 'r', 'utf-8')    
    lines = dev_f.readlines()
    dependency_lines = dev_dependency_f.readlines()
    dev_f.close()
    dev_dependency_f.close()

    samples = []
    for i,(line, dependency_line) in enumerate(zip(lines,dependency_lines)):
        print i
        new_sample = sample()
        line = line.split('\t')
        dependency_line = dependency_line.split('\t')
        new_sample.sent1_id = int(line[0])
        new_sample.sent2_id = int(line[1])
        assert line[0] == dependency_line[0]
        assert line[1] == dependency_line[1]
        #preprocessing of text:tokenization and stemming
        sent1 = [porter.stem(t) for t in nltk.word_tokenize(line[2])]
        new_sample.sent1 = sent1
        sent2 = [porter.stem(t) for t in nltk.word_tokenize(line[3])]
        new_sample.sent2 = sent2
        #filter stop words
        sent1_nonstop_word =  [word for word in sent1 if not word in english_stopwords and not word in english_punctuations]
        sent2_nonstop_word =  [word for word in sent2 if not word in english_stopwords and not word in english_punctuations]
        #get n-gram features
        new_sample.word_overlap = unigram_overlap(sent1_nonstop_word,sent2_nonstop_word)
        new_sample.bigram_overlap = bigram_overlap(sent1, sent2)
        new_sample.trigram_overlap = trigram_overlap(sent1, sent2)
        new_sample.fourgram_overlap = fourgram_overlap(sent1, sent2)
        new_sample.lcs = float(max_LCS(sent1, sent2)) /  min(len(sent1),len(sent2))
        new_sample.length_diff = float(abs(len(sent1)-len(sent2))) / min(len(sent1),len(sent2))
        pos1 = nltk.pos_tag(sent1)
        pos2 = nltk.pos_tag(sent2)
        pos1_nonstop_word = [word for word in pos1 if not word[0] in english_stopwords and not word[0] in english_punctuations]
        pos2_nonstop_word = [word for word in pos2 if not word[0] in english_stopwords and not word[0] in english_punctuations]
        new_sample.nnp_overlap = nnp_overlap(pos1, pos2)
        new_sample.ne_overlap = ne_overlap(pos1, pos2)
        new_sample.num_overlap = num_overlap(pos1,pos2)
        #get knowledge based features
        new_sample.path_best_sim = path_best_sim(pos1_nonstop_word, pos2_nonstop_word, pos_map, pos_list)
        new_sample.wup_best_sim = wup_best_sim(pos1_nonstop_word, pos2_nonstop_word, pos_map, pos_list)
        new_sample.lch_best_sim = lch_best_sim(pos1_nonstop_word, pos2_nonstop_word, pos_map, pos_list)
        new_sample.lin_best_sim = lin_best_sim(pos1_nonstop_word, pos2_nonstop_word, brown_ic, pos_map, pos_list)
        new_sample.res_best_sim = res_best_sim(pos1_nonstop_word, pos2_nonstop_word, brown_ic, pos_map, pos_list)
        new_sample.jcn_best_sim = jcn_best_sim(pos1_nonstop_word, pos2_nonstop_word, brown_ic, pos_map, pos_list)
        new_sample.dependency_sim = dependency_sim(dependency_line[2], dependency_line[3])
        samples.append(new_sample)
    return samples

def load_dev_y(dev_samples, dev_gold_file):
    """
    load dev gold from dev_gold.txt
    return dev datas' paraphrase relation list
    """
    dev_ans_f = codecs.open(dev_gold_file,'r', 'utf-8')
    lines = dev_ans_f.readlines()
    lines.pop(0)
    dev_y = []
    for dev_sample,line in zip(dev_samples, lines):
        line = line.split('\t')
        assert dev_sample.sent1_id == int(line[1])
        assert dev_sample.sent2_id == int(line[2])
        dev_sample.is_repeat = int(line[0])
        dev_y.append(int(line[0]))
    return dev_y


def transform_train_data(train_samples):
    """
    transfrom train sample list to map list
    return map list
    """
    train_datas = []
    train_y = []
    for train_sample in train_samples:
        x = {'BIAS':1}
        x['word_overlap'] = train_sample.word_overlap
        x['nnp_overlap'] = train_sample.nnp_overlap
        x['ne_overlap'] = train_sample.ne_overlap
        x['num_overlap'] = train_sample.num_overlap
        x['bigram_overlap'] = train_sample.bigram_overlap
        x['trigram_overlap'] = train_sample.trigram_overlap
        x['fourgram_overlap'] = train_sample.fourgram_overlap
        x['lcs'] = train_sample.lcs
        x['length_diff'] = train_sample.length_diff
        x['path_best_sim'] = train_sample.path_best_sim
        x['wup_best_sim'] = train_sample.wup_best_sim
        x['lch_best_sim'] = train_sample.lch_best_sim
        x['lin_best_sim'] = train_sample.lin_best_sim
        x['res_best_sim'] = train_sample.res_best_sim
        x['jcn_best_sim'] = train_sample.jcn_best_sim
        x['dependency_sim'] = train_sample.dependency_sim
        train_datas.append(x)
        train_y.append(train_sample.is_repeat)
    return (train_datas, train_y)


def transform_dev_or_test_data(samples):
    """
    transfrom dev or test sample list to map list
    return map list
    """
    datas = []
    for dev_sample in samples:
        x = {'BIAS':1}
        x['word_overlap'] = dev_sample.word_overlap
        x['nnp_overlap'] = dev_sample.nnp_overlap
        x['ne_overlap'] = dev_sample.ne_overlap
        x['num_overlap'] = dev_sample.num_overlap
        x['bigram_overlap'] = dev_sample.bigram_overlap
        x['trigram_overlap'] = dev_sample.trigram_overlap
        x['fourgram_overlap'] = dev_sample.fourgram_overlap
        x['lcs'] = dev_sample.lcs
        x['length_diff'] = dev_sample.length_diff
        x['path_best_sim'] = dev_sample.path_best_sim
        x['wup_best_sim'] = dev_sample.wup_best_sim
        x['lch_best_sim'] = dev_sample.lch_best_sim
        x['lin_best_sim'] = dev_sample.lin_best_sim
        x['res_best_sim'] = dev_sample.res_best_sim
        x['jcn_best_sim'] = dev_sample.jcn_best_sim
        x['dependency_sim'] = dev_sample.dependency_sim
        datas.append(x)
    return datas