from copy import deepcopy
from enum import Enum
from typing import Callable, Union
from lemmatree import LemmaTree

consonants = [
    'ʾ', 'b', 'c', 'c̭', 'č', 'č̭',
    'd', 'f', 'ġ', 'h', 'ɟ', 'j',
    'k̭', 'l', 'm', 'n', 'p', 'p̂',
    'r', 's', 'š', 't', 'ṱ', 'v',
    'x', 'y', 'z', 'ž',
]
vowels = [
    'a', 'à', 'á', 'ā', 'ā̀', 'ā́',
    'e', 'è', 'é', 'ē', 'ḕ', 'ḗ',
    'i', 'ì', 'í', 'ī', 'ī̀', 'ī́',
    'o', 'ò', 'ó', 'ō', 'ṑ', 'ṓ',
    'u', 'ù', 'ú', 'ū', 'ū̀', 'ū́',
    'ə', 'ə̀', 'ə́', 'ắ', 'ã', 'ŭ'
]
marks = [
    '+', '-', '꞊',
]

punctuation = [
    ' ', '.', '|', '?', "!", ",",
    '…', '(', ')', '/', '~',
]


class Gender(Enum):
    MS = 'MS'
    FS = 'FS'
    PL = 'PL'


def attach_cop_trans(cop: str, gender: str = None) -> Callable:
    def attach_cop(x: str, **kwargs) -> str:
        if gender:
            path = kwargs['path']
            i = max(path.find(g) for g in {'.MS', '.FS', '.PL'})
            if i != -1 and path[i+1:i+3] != gender:
                return None
        final_letter = x[-1]
        syllable_count = 2
        if final_letter in consonants or syllable_count == 1:
            return x + '꞊' + cop.lstrip('ʾ')
        elif final_letter == 'a':
            return x[:-1] + 'ə' + cop.lstrip('ʾiī')
        else:
            return x + cop.lstrip('ʾiī')
    return attach_cop


def contract_cop(x: str, **kwargs) -> str:
    i = x.rfind('꞊')
    if i == -1:
        vV = x[-3:-1]
        if vV in ('və', 'va'):
            return x[:-3] + x[-1]
        return None
    else:
        if 'ī' in x[i:]:
            return None
        return x[:i+1] + x[i+2:]


def elide_ə(x: str, **kwargs):
    '''
    ptixəl < ptixələ < ptixa + ʾilə
    '''
    if not x.endswith('lə'):
        return None
    return x.rstrip('ə')


def create_enclitic_copula_lemmatree(ə_elidable: bool = False):
    children = [LemmaTree('.(CNTR)', trans=contract_cop)]
    if ə_elidable:
        children.append(LemmaTree('.(ELIS)', trans=elide_ə))
    present_enclitic_copula_lemmatree = LemmaTree('.PRS', group=True, children=[
        LemmaTree('.3MS', trans=attach_cop_trans('ʾilə', gender='MS'), children=deepcopy(children)),
        LemmaTree('.3FS', trans=attach_cop_trans('ʾila', gender='FS'), children=deepcopy(children)),
        LemmaTree('.3PL', trans=attach_cop_trans('ʾina', gender='PL'), children=deepcopy(children)),
        LemmaTree('.2MS', trans=attach_cop_trans('ʾivət', gender='MS'), children=deepcopy(children)),
        LemmaTree('.2FS', trans=attach_cop_trans('ʾivat', gender='FS'), children=deepcopy(children)),
        LemmaTree('.2PL', trans=attach_cop_trans('ʾitun', gender='PL'), children=deepcopy(children)),
        LemmaTree('.1MS', trans=attach_cop_trans('ʾivən', gender='MS'), children=deepcopy(children)),
        LemmaTree('.1FS', trans=attach_cop_trans('ʾivan', gender='FS'), children=deepcopy(children)),
        LemmaTree('.1PL', trans=attach_cop_trans('ʾivax', gender='PL'), children=deepcopy(children)),
    ])
    past_enclitic_copula_lemmatree = LemmaTree('.PST', group=True, children=[
        LemmaTree('.3MS', trans=attach_cop_trans('ʾiva', gender='MS'), children=deepcopy(children)),
        LemmaTree('.3FS', trans=attach_cop_trans('ʾiva', gender='FS'), children=deepcopy(children)),
        LemmaTree('.3PL', trans=attach_cop_trans('ʾiva', gender='PL'), children=deepcopy(children)),
        LemmaTree('.2MS', trans=attach_cop_trans('ʾītva', gender='MS'), children=deepcopy(children)),
        LemmaTree('.2FS', trans=attach_cop_trans('ʾītva', gender='FS'), children=deepcopy(children)),
        LemmaTree('.2PL', trans=attach_cop_trans('ʾitunva', gender='PL'), children=deepcopy(children)),
        LemmaTree('.1MS', trans=attach_cop_trans('ʾīnva', gender='MS'), children=deepcopy(children)),
        LemmaTree('.1FS', trans=attach_cop_trans('ʾīnva', gender='FS'), children=deepcopy(children)),
        LemmaTree('.1PL', trans=attach_cop_trans('ʾīxva', gender='PL'), children=deepcopy(children)),
    ])

    return LemmaTree('-COP', group=True, children=[
        present_enclitic_copula_lemmatree,
        past_enclitic_copula_lemmatree,
    ])


# only for nouns and adjectives
# fuller ending!!!!"
def attach_annexation_trans(after_suffix: bool):
    def attach_annexation(x: str, **kwargs) -> str:
        final_letter = x[-1]
        if final_letter == '-':
            return x[:-1] + 'ət'
        elif final_letter in vowels:
            if after_suffix:
                return x + '꞊t'
            elif attach_annexation == 'u':
                return x + 'ntət'
            else:
                return x[:-1] + 'ət'
        else:
            return x + '꞊ət'
    return attach_annexation


def contract_annexation(x: str, **kwargs) -> str:
    if x[-3:] != '꞊ət':
        return None
    return x[:-2] + x[-1]


def create_annexation_lemmatree(lemma: Union[str, bool] = None, after_suffix: bool = False):
    return LemmaTree('-GEN', lemma=lemma, trans=attach_annexation_trans(after_suffix), children=[
        LemmaTree('.(CNTR)', trans=contract_annexation)
    ])


def attach_pronominal_suffix_trans(suffix):
    def attach_pronominal_suffix(x: str, **kwargs) -> str:
        final_letter = x[-1]
        if x in ('tre', '⁺ṱla'):
            return x + 'y' + suffix
        elif final_letter == '-':
            return x.rstrip('-') + suffix
        elif final_letter in ('a', 'e'):
            return x.rstrip('ae') + suffix
        elif final_letter == 'i':
            return x + 'yy' + suffix
        elif final_letter == 'u':  # this might not be true for everything
            return x + 'nt' + suffix
        elif x[-2:] == 'at':  # this should be only for unintegrated arabic load words
            return x + 't' + suffix
        else:
            return x + suffix
    return attach_pronominal_suffix


def create_pronominal_suffix_lemmatree(annexable: bool = False):
    children = [
        LemmaTree('.3MS', trans=attach_pronominal_suffix_trans('u'), children=[create_enclitic_copula_lemmatree()]),
        LemmaTree('.3FS', trans=attach_pronominal_suffix_trans('o'), children=[create_enclitic_copula_lemmatree()]),
        LemmaTree('.3PL', trans=attach_pronominal_suffix_trans('ə'), children=[create_enclitic_copula_lemmatree()]),
        LemmaTree('.2MS', trans=attach_pronominal_suffix_trans('ux'), children=[create_enclitic_copula_lemmatree()]),
        LemmaTree('.2FS', trans=attach_pronominal_suffix_trans('ax'), children=[create_enclitic_copula_lemmatree()]),
        LemmaTree('.2PL', trans=attach_pronominal_suffix_trans('oxun'), children=[create_enclitic_copula_lemmatree()]),
        LemmaTree('.1S' , trans=attach_pronominal_suffix_trans('i'), children=[create_enclitic_copula_lemmatree()]),
        LemmaTree('.1PL', trans=attach_pronominal_suffix_trans('an'), children=[create_enclitic_copula_lemmatree()]),
    ]
    if annexable:
        for c in children:
            c.children.append(create_annexation_lemmatree(after_suffix=True))
    return LemmaTree('-GEN', group=True, children=children)


class SSuffix(Enum):
    _3MS = '3MS', '-∅',    '-∅ni'
    _3FS = '3FS', '-a',    '-ani'
    _3PL = '3PL', '-i',    '-ini'
    _2MS = '2MS', '-ət',   '-itən'
    _2FS = '2FS', '-at',   '-atən'
    _2PL = '2PL', '-itun', '-ituna'
    _1MS = '1MS', '-ən',   '-ina'
    _1FS = '1FS', '-an',   '-ana'
    _1PL = '1PL', '-ax',   '-axən'
    _3PL_Past = '3PL', '-e', ''


class LSuffix(Enum):
    _3MS = '3MS', '-lə'
    _3FS = '3FS', '-la'
    _3PL = '3PL', '-lun'
    _2MS = '2MS', '-lux'
    _2FS = '2FS', '-lax'
    _2PL = '2PL', '-loxun'
    _1S  = '1S',  '-li'
    _1PL = '1PL', '-lan'


def create_present_stem(root):
    c1, c2, c3 = root.split('-')
    return f'{c1}a{c2}ə{c3}-'


def attach_lsuffix_trans(suffix: LSuffix):
    def attach_ssufix(base):
        _, s = suffix
        if base[-2] == 'r':
            s = s.replace('l', 'r')
        return base.rstrip('-') + s.lstrip('-')
    return attach_ssufix


def assimilate_lsuffix(word: str):
    i = -1
    for s in LSuffix:
        _, s = s.value
        i = max(i, word.rfind(s.lstrip('-')))
    if i == -1 or word[i-1] != 'n':
        return None
    return word[:i] + 'n' + word[i+1:]


###############################################################################
# VERBS
# Started Oct 7
# Do not need to handle the attachment of the S suffix:
#  - assuming PRS S for all S will be given for all verbs
#  - assuming PST S for all S will be given for all verbs
###############################################################################

def attach_va(x: str, **kwargs):
    '''
    patəxva < patəx + va 
    ptəxva  < ptix- + va 
    dariva  < darə + va 
    '''
    x = x.rstrip('-')
    if x[-2] == 'i':
        x = x[:-2] + 'ə' + x[-1]
    if x[-1] == 'ə':
        x = x[:-1] + 'i'
    return x + 'va'

def attach_l_trans(l: str) -> str:
    def attach_l(x: str, **kwargs) -> str:
        # In final weak roots in which the past template ends in a vowel, the /ə/ of the 3ms suffix is occasionally elided, e.g. xzil̄́ ‘he saw’ (A 10:2) < xzílə.
        # pg 270
        '''
        x is the base
        ptəxlə  < ptix- + -lə
        +xdərrə < *⁺xdərlə < ⁺xdir- + -lə
        '''
        # strip hyphen if there
        x = x.rstrip('-')

        # get l suffix
        lə = l.lstrip('-')

        # shorten long vowel in preceeding closed syllable (for past type I verb stems)
        if x[-2] == 'i':
            x = x[:-2] + 'ə' + x[-1]

        # obligatorily assimilate l into r
        if x[-1] == 'r':
            lə = 'r' + lə.lstrip('l')
        return x + lə
    return attach_l

def assimilate_l_trans(prs: bool):
    def assimilate_l(x: str, **kwargs):
        '''
        cpənlə ~ cpənnə < cpin- + -lə
        '''
        i = x.rfind('l')

        # r assimilation already occured
        if i < x.rfind('rr'):
            return None

        # assimilate into 'n' or 't'
        assimilators = {'n', 't'} if prs else {'n'}
        if x[i-1] not in assimilators:
            return None
        
        return x[:i] + x[i-1] + x[i+1:]
    return assimilate_l

def create_lsuffix_lemmatree(prs: bool):
    # abbrev = '.DO' if prs else '.SUB'
    abbrev = '-L'
    return LemmaTree(abbrev, group=True, children=[
        LemmaTree('.3MS', trans=attach_l_trans('-lə'), children=[LemmaTree('.(ASSML)', trans=assimilate_l_trans(prs))]),
        LemmaTree('.3FS', trans=attach_l_trans('-la'), children=[LemmaTree('.(ASSML)', trans=assimilate_l_trans(prs))]),
        LemmaTree('.3PL', trans=attach_l_trans('-lun'), children=[LemmaTree('.(ASSML)', trans=assimilate_l_trans(prs))]),
        LemmaTree('.2MS', trans=attach_l_trans('-lux'), children=[LemmaTree('.(ASSML)', trans=assimilate_l_trans(prs))]),
        LemmaTree('.2FS', trans=attach_l_trans('-lax'), children=[LemmaTree('.(ASSML)', trans=assimilate_l_trans(prs))]),
        LemmaTree('.2PL', trans=attach_l_trans('-loxun'), children=[LemmaTree('.(ASSML)', trans=assimilate_l_trans(prs))]),
        LemmaTree('.1S', trans=attach_l_trans('-li'), children=[LemmaTree('.(ASSML)', trans=assimilate_l_trans(prs))]),
        LemmaTree('.1PL', trans=attach_l_trans('-lan'), children=[LemmaTree('.(ASSML)', trans=assimilate_l_trans(prs))]),
    ])

def create_va_lemmatree(prs: bool):
    return LemmaTree('-PST', group=not prs, trans=attach_va, children=[create_lsuffix_lemmatree(False)])

def create_compound_obj_lemmatree():
    children = [
        LemmaTree('.3MS', group=True, trans=attach_pronominal_suffix_trans('u'), children=[create_enclitic_copula_lemmatree(ə_elidable=True)]),
        LemmaTree('.3FS', group=True, trans=attach_pronominal_suffix_trans('o'), children=[create_enclitic_copula_lemmatree(ə_elidable=True)]),
        LemmaTree('.3PL', group=True, trans=attach_pronominal_suffix_trans('ə'), children=[create_enclitic_copula_lemmatree(ə_elidable=True)]),
        LemmaTree('.2MS', group=True, trans=attach_pronominal_suffix_trans('ux'), children=[create_enclitic_copula_lemmatree(ə_elidable=True)]),
        LemmaTree('.2FS', group=True, trans=attach_pronominal_suffix_trans('ax'), children=[create_enclitic_copula_lemmatree(ə_elidable=True)]),
        LemmaTree('.2PL', group=True, trans=attach_pronominal_suffix_trans('oxun'), children=[create_enclitic_copula_lemmatree(ə_elidable=True)]),
        LemmaTree('.1S' , group=True, trans=attach_pronominal_suffix_trans('i'), children=[create_enclitic_copula_lemmatree(ə_elidable=True)]),
        LemmaTree('.1PL', group=True, trans=attach_pronominal_suffix_trans('an'), children=[create_enclitic_copula_lemmatree(ə_elidable=True)]),
    ]
    return LemmaTree('-DO', group=True, children=children)
