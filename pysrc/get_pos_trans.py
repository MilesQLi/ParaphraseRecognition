###############################################################
#
#  author Li Qi
#  mail stormier@126.com
#
#
###############################################################


def get_pos_map():
    """
    use this to map LDC POS to wordnet POS
    """
    map = {}
    map['CC'] = ''
    map['CD'] = 'n'
    map['DT'] = ''
    map['EX'] = 'r'
    map['FW'] = ''
    map['IN'] = ''
    map['JJ'] = 'a'
    map['JJR'] = 'a'
    map['JJS'] = 'a'
    map['LS'] = ''
    map['MD'] = ''
    map['NN'] = 'n'
    map['NNS'] = 'n'
    map['NNP'] = 'n'
    map['NNPS'] = 'n'
    map['PDT'] = ''
    map['POS'] = ''
    map['PRP'] = ''
    map['PRPS$'] = ''
    map['RB'] = 'r'
    map['RBR'] = 'r'
    map['RBS'] = 'r'
    map['RP'] = ''
    map['SYM'] = ''
    map['TO'] = ''
    map['UH'] = ''
    map['VB'] = ''
    map['VBD'] = 'v'
    map['VBG'] = 'v'
    map['VBN'] = 'v'
    map['VBP'] = 'v'
    map['VBZ'] = 'v'
    map['WDT'] = ''
    map['WP'] = ''
    map['WP$'] = ''
    map['WRB'] = ''
    return map


def get_pos_list():
    """
    use this list to Check if a LDC POS has a wordnet POS mapping 
    """
    pos_list = ['CD','EX','JJ','JJR','JJS','NN','NNS','NNP','NNPS','PDT','VBD','VBG','VBN','VBP','VBZ']
    return pos_list
    