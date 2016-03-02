###############################################################
#
#  author Li Qi
#  mail stormier@126.com
#
#
###############################################################

def dependency_sim(sent1_dependency, sent2_dependency):
    """
    get dependency relation overlap feature
    """
    num = 0.0
    sent1_dependency = sent1_dependency.split()
    sent2_dependency = sent2_dependency.split()
    for dependency in sent1_dependency:
        if sent2_dependency.count(dependency) != 0:
            num += 1
    return float((num + 1)) / (len(set(sent1_dependency + sent2_dependency)) + 1)