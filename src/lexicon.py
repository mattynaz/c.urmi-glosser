from lemmatree import LemmaTree
from partsofspeech import *

# This house is yours now. Why reminisce in it's ruins when you can reconstruct a home unshakable.





















###############################################################################
#### PRONOUNS                                                              ####
###############################################################################

independent_personal_pronouns = [
    LemmaTree('3MS', lemma='⁺ʾav,⁺ʾavun'),
    LemmaTree('3FS', lemma='ʾay,ayən'),
    LemmaTree('3PL', lemma='ʾani'),
    LemmaTree('2S',  lemma='ʾat,ʾatən'),
    LemmaTree('2PL', lemma='ʾaxtun,ʾaxtoxun,ʾaxnoxun'),
    LemmaTree('1S',  lemma='ʾana'),
    LemmaTree('1PL', lemma='ʾaxnan'),
]




















###############################################################################
#### VERBS                                                                 ####
###############################################################################

inflections = {
    'pres': {
        's_suff': {
            '3ms': 'patəx',
            '3fs': 'patxa',
            '3pl': 'patxi',
            '2ms': 'patxət',
            '2fs': 'patxat',
            '2pl': 'patxitun',
            '1ms': 'patxən',
            '1fs': 'patxan',
            '1pl': 'patxax',
        },
    },
    'pst': {
        'stem': 'ptix-',
        's_suff': {
            '3ms': 'ptəx-',
            '3fs': 'ptixa-',
            '3pl': 'ptixé-',
            '2ms': 'ptixət-',
            '2fs': 'ptixat-',
            '2pl': 'ptixitun-',
            '1ms': 'ptixən-',
            '1fs': 'ptixan-',
            '1pl': 'ptixax-',
        },
    },
    'rsp': {
        'ms': 'ptixa',
        'fs': 'ptəxta',
        'pl': 'ptixə',
    },
    'imper': {
        's':  'ptux',
        'pl': 'ptuxun',
    },
    'inf':
        'ptaxa',
    'prog':
        'bəptaxa',
    'vn':
        'ptaxta',
    'ap': {
        'ms': 'patxana',
        'fs': 'patxanta',
        'pl': 'patxanə',
    },
}

verbs = [
    Verb('open', inflections=inflections),
]




















###############################################################################
#### ADJECTIVES                                                            ####
###############################################################################

adjectives = [
    Adjective('pleasant', ms='basima', fs='basəmta', pl='basimə'),
    Adjective('smooth', ms='⁺č̭uvva', fs='⁺č̭uvvə', pl='⁺č̭uvvə'),
    Adjective('good', invar='⁺spay'),
]




















###############################################################################
#### NOUNS                                                                 ####
###############################################################################

nouns = [
    Noun('singer', ms='zamara', fs='zamarta', pl='zamarə'),
    Noun('bread', ms='laxma'),
    Noun('cat', fs='⁺k̭aṱu'),
    Noun('watermill', ms='ʾərxə', annexed='ʾərxiyyət'),
    Noun('gadfly', fs='dəbburta, dəbbur'),
]




















###############################################################################
#### PARTICLES                                                             ####
###############################################################################

adverbs = [
    Adverb('here', lemma='laxxa, ʾaxxa'),
    Adverb('nearby', lemma='laxxanə'),
    Adverb('around here', 'laxxananə'),
    Adverb('from here', lemma='m-axxa'),
    Adverb('to here', lemma='l-a-yba'),
    Adverb('there (medium)', lemma='⁺tamma'),
    Adverb('around there', lemma='⁺tammanə'),
    Adverb('around there', lemma='⁺tammananə'),
    Adverb('there (far)', lemma='⁺tammo'),
    Adverb('there (far)', lemma='⁺tammoha, ⁺tammoxa'),
    Adverb('there (absent)', lemma='⁺tama'),
    Adverb('around there', lemma='⁺tamananə'),
    Adverb('above', lemma='⁺ʾullul, ⁺lal'),
    Adverb('upwards', lemma='⁺ʾal-⁺ʾullul, ⁺lal'),
    Adverb('below', lemma='ʾəltəx, ⁺ʾultux'),
    Adverb('underneath', lemma='xut'),
    Adverb('downwards', lemma='⁺ʾal-ʾəltəx, ⁺ʾal-ʾultux'),
    Adverb('outside', lemma='vaddar, ⁺ʾal-vaddar'),
    Adverb('inside', lemma='ɟavay'),
    Adverb('behind', lemma='⁺baray'),
    Adverb('backwards', lemma='la-⁺bara'),
    Adverb('this side', lemma='ʾa-ɟiba, ʾa-yba'),
    Adverb('that side', lemma='ʾo-ɟiba, ʾo-yba'),
    Adverb('in the middle', lemma='pi-palɟa'),
    Adverb('in front', lemma='k̭am'),
    Adverb('forwards', lemma='la-k̭ama'),
    Adverb('forwards', lemma='k̭amay'),
    Adverb('on its head', lemma='rišaxta'),
    Adverb('upside down', lemma='riša rišaxta, riš-rišaxta'),
    Adverb('face downwards, flatwise', lemma='pummaxta'),
    Adverb('on his back', lemma='⁺ʾal-ɟarmət ⁺xasu'),
    Adverb('directly', lemma='xa-riša'),
    Adverb('now', lemma='ʾadiyya, ʾadi'),
    Adverb('today', lemma='ʾudyu'),
    Adverb('tonight', lemma='ʾad-lelə'),
    Adverb('at first', lemma='k̭amay'),
    Adverb('yesterday', lemma='k̭udmə, k̭udmət ⁺vərrə'),
    Adverb('tomorrow', lemma='k̭udmə, k̭udmət ʾatə'),
    Adverb('the day before yesterday', lemma='m-k̭am-k̭udmə'),
    Adverb('the day after tomorrow, the day before yesterday', lemma='yuma-xina'),
    Adverb('in the morning, tomorrow morning', lemma='k̭edamta'),
    Adverb('early morning', lemma='k̭edamta jaldə'),
    Adverb('in the evening, last night', lemma='⁺berašə'),
    Adverb('last night', lemma='k̭udmə ⁺berašə'),
    Adverb('tomorrow morning', lemma='k̭udmə moriša'),
    Adverb('early', lemma='jaldə'),
    Adverb('formerly, first', lemma='derranɟ'),
    Adverb('afterwards', lemma='⁺xarta'),
    Adverb('afterwards', lemma='⁺bara'),
    Adverb('this year', lemma='ʾa-šita'),
    Adverb('last year', lemma='bazzuynə'),
    Adverb('last year', lemma='šət-⁺vərra'),
    Adverb('never', lemma='həc-⁺dana'),
    Adverb('never', lemma='ʾaslan'),
    Adverb('at this time', lemma='b-da-⁺dana'),
    Adverb('at that time', lemma='b-de-⁺dana'),
    Adverb('suddenly', lemma='xa-b-xa'),
    Adverb('suddenly', lemma='xa-b-xa-ɟa'),
    Adverb('sometimes', lemma='xa-xa-ɟa'),
    Adverb('sometimes', lemma='xacma ɟa'),
    Adverb('at that time', lemma='ʾe-ɟa'),
    Adverb('always', lemma='hammaša'),
    Adverb('ever', lemma='har'),
    Adverb('from now onwards', lemma='⁺madəlbarə'),
    Adverb('again', lemma='mədrə'),
    Adverb('where', lemma='ʾica', copula_base = 'ce-'),
    Adverb('whence', lemma='m-ica'),
    Adverb('when', lemma='ʾiman, diman'),
    Adverb('at what time', lemma='ʾəm-⁺dana'),
    Adverb('how', lemma='dax, daxi'),
    Adverb('how', lemma='mujjur, mujjurra'),
    Adverb('how much', lemma='cma'),
    Adverb('why', lemma='k̭a-mudi, k̭a-mu, k̭am'),
    Adverb('like this', lemma='atxa'),
    Adverb('quickly', lemma='jaldə'),
    Adverb('slowly', lemma='nixa'),
    Adverb('very slowly', lemma='nixunta'),
    Adverb('well', lemma='⁺spay'),
    Adverb('well', lemma='jəns'),
    Adverb('badly', lemma='xərba'),
    Adverb('hard', lemma='k̭əšya'),
    Adverb('strongly', lemma='xelana'),
]

quantifiers = [
    Quantifier('much', lemma='⁺raba, ⁺roba'),
    Quantifier('all', lemma='cullə'),
    Quantifier('every', lemma='cul, cu'),
    Quantifier('a few', lemma='cma, xacma'),
    Quantifier('slightly, a little', lemma='xač̭č̭a'),
    Quantifier('very little', lemma='xač̭č̭unta'),
    Quantifier('so much', lemma='⁺ʾuxča'),
    Quantifier('none', lemma='həč'),
]

prepositions = [
    Preposition(
        'between',
        annexation_base='⁺ʾaralləġ, ⁺ʾaralləġġ-',
        pronominal_suffix_base='⁺ʾaralġ-',
    ),
    Preposition(
        'like',
        proclitic='ʾax-,max-',
    ),
    Preposition(
        'upon;to',
        proclitic='⁺ʾal-',
        pronominal_suffix_base='⁺ʾall-',
    ),
    Preposition(
        'to',
        proclitic='la-,l-',
    ),
    Preposition(
        'above,over',
        annexation_base='⁺ʾullul, ⁺ulluyl-',
        pronominal_suffix_base='⁺ʾulluyl-',
    ),
    Preposition(
        'under',
        annexation_base='ʾəltəx, ʾəltix-',
        pronominal_suffix_base='ʾəltix-',
    ),
    Preposition(
        'with,by,on,in',
        proclitic='b-', # handle coallescing!
        pronominal_suffix_base='biyy-',
    ),
    Preposition(
        'behind,after',
        uninflected='⁺bar',
        pronominal_suffix_base='⁺bar-',
    ),
    Preposition(
        'opposite',
        annexation_base='bark̭uyl-',
        pronominal_suffix_base='bark̭ul-, bark̭uyl-',
    ),
    Preposition(
        'concerning,about',
        annexation_base='baz-',
        pronominal_suffix_base='baz-',
    ),
    Preposition(
        'between',
        proclitic='bəl-',
        pronominal_suffix_base='bil-',
    ),
    Preposition(
        'concerning,about',
        proclitic='but-',
    ),
    Preposition(
        'near,with,at the home of',
        proclitic='cəs-',
        pronominal_suffix_base='cəsl-',
    ),
    Preposition(
        'against',
        annexation_base='dark̭ul-, dark̭uyl-',
        pronominal_suffix_base='dark̭ul-, dark̭uyl-',
    ),
    Preposition(
        'without',
        uninflected='d-la',
    ),
    Preposition(
        'until, up to',
        proclitic='hal',
    ),
    Preposition(
        'until, up to',
        annexation_base='ɟav-',
        proclitic='ɟu-, ɟa-',
        pronominal_suffix_base='ɟav-',
    ),
    Preposition(
        'to',
        proclitic='k̭a-',
        pronominal_suffix_base='k̭at-',  # CONTRACTIONS
    ),
    Preposition(
        'before, in front of',
        annexation_base='k̭am-',
        proclitic='k̭am-',
        pronominal_suffix_base='k̭am-',
    ),
    Preposition(
        'before, in front of',
        annexation_base='k̭amayt-',
        pronominal_suffix_base='k̭amayt-',
    ),
    Preposition(
        'around',
        annexation_base='marzan-, marzanan-',
        pronominal_suffix_base='marzan-, marzanan-',
    ),
    Preposition(
        'from;with',
        proclitic='mən-, m-',
        pronominal_suffix_base='mənn-',
    ),
    Preposition(
        'around',
        annexation_base='⁺xadərvan-',
        pronominal_suffix_base='⁺xadərvan-',
    ),
    Preposition(
        'under',
        proclitic='xut-',
        pronominal_suffix_base='xut-',
    )
]

uninflected_particles = [
    UninflectedParticle('ʾaġallan', lemma='at least'),
    UninflectedParticle('ʾăɟar', lemma='if'),
    UninflectedParticle('ʾalbal', lemma='immediately'),
    UninflectedParticle('ʾanɟa', lemma='if'),
    UninflectedParticle('ʾaslan', lemma='fundamentaly; at all'),
    UninflectedParticle('ʾaxči', lemma='only; but'),
    UninflectedParticle('ʾay', lemma='oh!'),
    UninflectedParticle('ʾaynbo', lemma='alas!'),
    UninflectedParticle('ʾazbar', lemma='by heart'),
    UninflectedParticle('balcət', lemma='perhaps'),
    UninflectedParticle('bălə', lemma='yes'),
    UninflectedParticle('bas,ba', lemma='but,however;then'),
    UninflectedParticle('bina', lemma='huh?'),
    UninflectedParticle('buš', lemma='more'),
    UninflectedParticle('c̭am,c̭əm', lemma='little,lacking'),
    UninflectedParticle('čəm', lemma='very'),
    UninflectedParticle('čuncət', lemma='because'),
    UninflectedParticle('ʾəllaci', lemma='especially'),
    UninflectedParticle('ʾən', lemma='if'),
    UninflectedParticle('habas', lemma='in vain'),
    UninflectedParticle('hal', lemma='until, up to'),
    UninflectedParticle('halbát,halbatta', lemma='of course,surely'),
    UninflectedParticle('har', lemma='just,certainly'),
    UninflectedParticle('hatman', lemma='absolutely'),
    UninflectedParticle('hatta', lemma='even'),
    UninflectedParticle('həč', lemma='none,nothing,never'),
    UninflectedParticle('hi', lemma='yes'),
    UninflectedParticle('ʾina', lemma='but'),
    UninflectedParticle('ʾita,ʾitar', lemma='then,afterwards,therefore'),
    UninflectedParticle('jəd', lemma=''),
    UninflectedParticle('k̭oma', lemma=''),
    UninflectedParticle('la', lemma=''),
    UninflectedParticle('măɟar', lemma=''),
    UninflectedParticle('masalan', lemma=''),
    UninflectedParticle('mədrə', lemma=''),
    UninflectedParticle('məjjət', lemma=''),
    UninflectedParticle('naɟəstan,mən-naɟəstan', lemma=''),
    UninflectedParticle('săbab,sab', lemma=''),
    UninflectedParticle('tacla', lemma=''),
    UninflectedParticle('tarsa', lemma=''),
    UninflectedParticle('ʾu', lemma=''),
    UninflectedParticle('ʾup', lemma=''),
    UninflectedParticle('xu', lemma=''),
    UninflectedParticle('ya', lemma=''),
    UninflectedParticle('ya,yan', lemma=''),
    UninflectedParticle('yanət,yan', lemma=''),
    UninflectedParticle('yuxsa', lemma=''),
    UninflectedParticle('zəl', lemma=''),
    UninflectedParticle('zoda,buš-zoda', lemma=''),
    UninflectedParticle('⁺amma', lemma=''),
    UninflectedParticle('⁺ʾanjaġ', lemma=''),
    UninflectedParticle('⁺ʾāx', lemma=''),
    UninflectedParticle('⁺ʾaxər', lemma=''),
    UninflectedParticle('⁺barabar', lemma=''),
    UninflectedParticle('⁺baram', lemma=''),
    UninflectedParticle('⁺hala,⁺halam', lemma=''),
    UninflectedParticle('⁺hana', lemma=''),
    UninflectedParticle('⁺ʾof', lemma=''),
    UninflectedParticle('⁺sevay', lemma=''),
    UninflectedParticle('⁺tammam', lemma=''),
    UninflectedParticle('⁺ṱuvva', lemma=''),
    UninflectedParticle('⁺vay', lemma=''),
    UninflectedParticle('⁺yanə,yanə', lemma=''),
]

enclitic_particles = [
    '꞊da',
    '꞊ət',
    '꞊zə',
]




















###############################################################################
#### LEXICON                                                               ####
###############################################################################

lexicon = verbs + adjectives + nouns

for lt in lexicon:
    lt.load()
