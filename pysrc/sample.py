###############################################################
#
#  author Li Qi
#  mail stormier@126.com
#
#
###############################################################
class sample:
    """
    a sample contains the feature of sentence pair to depend whether they are paraphrase
    """
    is_repeat = 0
    sent1_id = 0
    sent2_id = 0
    sent1 = []
    sent2 = []
    lcs = 0.0
    nnp_overlap = 0.0
    ne_overlap = 0.0
    num_overlap = 0.0
    length_diff = 0.0
    word_overlap = 0.0
    bigram_overlap = 0.0
    trigram_overlap = 0.0
    fourgram_overlap = 0.0
    path_best_sim = 0.0
    wup_best_sim = 0.0
    lch_best_sim = 0.0
    lin_best_sim = 0.0
    res_best_sim = 0.0
    jcn_best_sim = 0.0
    dependency_sim = 0.0