###############################################################
#
#  author Li Qi
#  mail stormier@126.com
#
#
###############################################################

import nltk
from nltk.corpus import wordnet_ic
from nltk.corpus import stopwords
import sys
sys.path.append(r'./')
import codecs
import logging
from random import random

from sklearn import svm
from sklearn.feature_extraction import DictVectorizer
from sklearn.grid_search import GridSearchCV

import numpy as np
from numpy import asarray
from numpy.random import shuffle

from data_loader import *

if __name__ == '__main__':
    """
    take train data to train model and tune hyperparameter by cross-validation and test on dev data
    """
    logging.basicConfig(level = logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filemode='w')
    
    if len(sys.argv) == 6:
        train_file = sys.argv[1]
        train_dependency_file = sys.argv[2]
        dev_file = sys.argv[3]
        dev_dependency_file = sys.argv[4]
        dev_gold_file = sys.argv[5]
    else:
        train_file = r'train_data.txt'
        train_dependency_file = r'train_data_dependency.txt'
        dev_file = r'dev_data.txt'
        dev_dependency_file = r'dev_data_dependency.txt'
        dev_gold_file = r'dev_gold.txt'

    logging.info("start loading and extracting train datas")
 
    #extract features from train data
    train_samples = train_data_feature_extract(train_file, train_dependency_file)

    #transform sample to map
    (train_datas, train_y) = transform_train_data(train_samples)
    
    #transform map to vector
    vectorizer = DictVectorizer()
    #transform map to vector
    train_x = vectorizer.fit_transform(train_datas).toarray()

    logging.info("start training model")
    #grid of parameter to search the best one
    param_grid = [
          {'C': [1, 10, 100, 120, 150], 'kernel': ['linear']},
          {'C': [1, 10, 100, 110, 120], 'gamma': np.logspace(-5, 1, 6), 'kernel': ['rbf']},
          {'C': [1, 10, 100, 120, 150], 'gamma': np.logspace(-10, 1, 10), 'kernel': ['sigmoid']},
          {'C': [1, 10, 100, 120, 150], 'degree': [2,3,4,5], 'kernel': ['poly']},
         ]
    clf = GridSearchCV(estimator=svm.SVC(), param_grid=param_grid, n_jobs=1)
    clf.fit(train_x, train_y)
    logging.info("finish training model")

    logging.info("start loading and extracting dev datas")
    #extract features from dev data
    dev_samples = dev_or_test_data_feature_extract(dev_file, dev_dependency_file)
    #transform sample to map
    dev_datas = transform_dev_or_test_data(dev_samples)
    #load dev gold 
    dev_y = load_dev_y(dev_samples, dev_gold_file)
    #transform map to vector
    dev_x = vectorizer.transform(dev_datas).toarray()
    logging.info("finish loading and extracting dev datas")
    
    logging.info("start predicting dev datas")
    pred_y = clf.predict(dev_x)

    right_num = 0
    print pred_y
    for i,(y_p,y_r) in enumerate(zip(pred_y, dev_y)):
        if y_p == y_r:
            right_num += 1
        else:
            print("%d predict: %d real:%d" % (i+1, y_p, y_r))
    print("accuracy: %f" % clf.score(dev_x, dev_y))
    
    print clf.best_estimator_


