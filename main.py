###############################################################
#
#  author Li Qi
#  mail stormier@126.com
#
#
###############################################################
import sys
sys.path.append(r'./pysrc')
import nltk
import logging
from random import random

from sklearn import svm
from sklearn.feature_extraction import FeatureHasher
from sklearn.feature_extraction import DictVectorizer
from sklearn.grid_search import GridSearchCV

import numpy as np
from numpy import asarray
from numpy.random import shuffle

from data_loader import *

if __name__ == '__main__':
    """
    take train data to train model and tune hyperparameter and test on dev data
    """
    logging.basicConfig(level = logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filemode='w')
    
    if len(sys.argv) == 9:
        train_file = sys.argv[1]
        train_dependency_file = sys.argv[2]
        dev_file = sys.argv[3]
        dev_dependency_file = sys.argv[4]
        dev_gold_file = sys.argv[5]
        test_file = sys.argv[6]
        test_dependency_file = sys.argv[7]
        test_gold_file = sys.argv[8]
    else:
        train_file = r'./data/train_data.txt'
        train_dependency_file = r'./data/train_data_dependency.txt'
        dev_file = r'./data/dev_data.txt'
        dev_dependency_file = r'./data/dev_data_dependency.txt'
        dev_gold_file = r'./data/dev_gold.txt'
        test_file = r'./data/test_data.txt'
        test_dependency_file = r'./data/test_data_dependency.txt'
        test_gold_file = r'./data/test_gold.txt'

    logging.info("start loading and extracting train datas")
    #extract features from train data
    train_samples = train_data_feature_extract(train_file, train_dependency_file)
    #transform sample to map
    (train_datas, train_y) = transform_train_data(train_samples)

    logging.info("start loading and extracting dev datas")
    #extract features from dev data
    dev_samples = dev_or_test_data_feature_extract(dev_file, dev_dependency_file)
    #transform sample to map
    dev_datas = transform_dev_or_test_data(dev_samples)
    #load dev gold 
    dev_y = load_dev_y(dev_samples, dev_gold_file)
    logging.info("finish loading and extracting dev datas")
    
    #concatenate train data and dev data
    train_datas.extend(dev_datas)
    train_y.extend(dev_y)
    #transform map to vector
    vectorizer = DictVectorizer()
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
    #train SVM model and find best hyperparameter
    clf.fit(train_x, train_y)
    print clf.score(train_x, train_y)
    print clf.best_estimator_
    logging.info("finish training model")
    
    logging.info("start loading test datas")
    #extract features from dev data
    test_samples = dev_or_test_data_feature_extract(test_file, test_dependency_file);
    test_datas = transform_dev_or_test_data(test_samples)
    test_x = vectorizer.transform(test_datas).toarray()
    logging.info("finish loading test datas")
    
    logging.info("start predicting test datas")
    #predict test data
    test_y = clf.predict(test_x)
    logging.info("finish predicting test datas")
    
    #output result
    result_writer = codecs.open(test_gold_file, 'w', 'utf-8')
    result_writer.write("Quality\t#1 ID\t#2 ID\r\n")
    for y, test_sample in zip(test_y, test_samples):
        result_writer.write("%d\t%d\t%d\r\n" % (y, test_sample.sent1_id, test_sample.sent2_id))    
    result_writer.flush()
    result_writer.close()
    
    
