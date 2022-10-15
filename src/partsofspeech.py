from copy import deepcopy
from lemmatree import LemmaTree
from common import *
from typing import Union


# inflections:
#     pres:
#         stem:  'ʾá{1}ə{2}'
#         s_suff:
#             3ms:  'ʾá{1}ə{2}'
#             3fs:  'ʾá{1}{2}a'
#             3pl:  'ʾá{1}{2}i'
#             2ms:  'ʾá{1}{2}ət'
#             2fs:  'ʾá{1}{2}at'
#             2pl:  'ʾa{1}{2}ítun'
#             1ms:  'ʾá{1}{2}ən'
#             1fs:  'ʾá{1}{2}an'
#             1pl:  'ʾá{1}{2}ax'
#     pst:
#         stem: '{1}i{2}-'
#         s_suff:
#             3ms:  '{1}ə́{2}-'
#             3fs:  '{1}i{2}á-'
#             3pl:  '{1}i{2}é-'
#             2ms:  '{1}i{2}ə́t-'
#             2fs:  '{1}i{2}át-'
#             2pl:  '{1}i{2}ítun-'
#             1ms:  '{1}i{2}ə́n-'
#             1fs:  '{1}i{2}án-'
#             1pl:  '{1}i{2}áx-'


class Verb(LemmaTree):
    def __init__(self, definition: str, inflections: dict):
        # present
        children = [create_lsuffix_lemmatree(prs=True), create_va_lemmatree(prs=True)]
        children = [
            LemmaTree('-S.3MS', lemma=inflections['pres']['s_suff']['3ms'], children=deepcopy(children)),
            LemmaTree('-S.3FS', lemma=inflections['pres']['s_suff']['3fs'], children=deepcopy(children)),
            LemmaTree('-S.3PL', lemma=inflections['pres']['s_suff']['3pl'], children=deepcopy(children)),
            LemmaTree('-S.2MS', lemma=inflections['pres']['s_suff']['2ms'], children=deepcopy(children)),
            LemmaTree('-S.2FS', lemma=inflections['pres']['s_suff']['2fs'], children=deepcopy(children)),
            LemmaTree('-S.2PL', lemma=inflections['pres']['s_suff']['2pl'], children=deepcopy(children)),
            LemmaTree('-S.1MS', lemma=inflections['pres']['s_suff']['1ms'], children=deepcopy(children)),
            LemmaTree('-S.1FS', lemma=inflections['pres']['s_suff']['1fs'], children=deepcopy(children)),
            LemmaTree('-S.1PL', lemma=inflections['pres']['s_suff']['1pl'], children=deepcopy(children)),
        ]
        prs = LemmaTree('.PRS', group=True, children=children)

        # past
        children = [create_lsuffix_lemmatree(prs=False), create_va_lemmatree(prs=False)]
        children = [
            LemmaTree('-S.3MS', group=True, lemma=inflections['pst']['s_suff']['3ms'], children=deepcopy(children)),
            LemmaTree('-S.3FS', group=True, lemma=inflections['pst']['s_suff']['3fs'], children=deepcopy(children)),
            LemmaTree('-S.3PL', group=True, lemma=inflections['pst']['s_suff']['3pl'], children=deepcopy(children)),
            LemmaTree('-S.2MS', group=True, lemma=inflections['pst']['s_suff']['2ms'], children=deepcopy(children)),
            LemmaTree('-S.2FS', group=True, lemma=inflections['pst']['s_suff']['2fs'], children=deepcopy(children)),
            LemmaTree('-S.2PL', group=True, lemma=inflections['pst']['s_suff']['2pl'], children=deepcopy(children)),
            LemmaTree('-S.1MS', group=True, lemma=inflections['pst']['s_suff']['1ms'], children=deepcopy(children)),
            LemmaTree('-S.1FS', group=True, lemma=inflections['pst']['s_suff']['1fs'], children=deepcopy(children)),
            LemmaTree('-S.1PL', group=True, lemma=inflections['pst']['s_suff']['1pl'], children=deepcopy(children)),
            *deepcopy(children),
        ]
        pst = LemmaTree('.PST', group=True, lemma=inflections['pst']['stem'], children=children)

        # resultative participle
        children = [
            create_compound_obj_lemmatree(),
            create_enclitic_copula_lemmatree(ə_elidable=True),
        ]
        children = [
            LemmaTree('.MS', lemma=inflections['rsp']['ms'], children=deepcopy(children)),
            LemmaTree('.FS', lemma=inflections['rsp']['fs'], children=deepcopy(children)),
            LemmaTree('.PL', lemma=inflections['rsp']['pl'], children=deepcopy(children)),
        ]
        res = LemmaTree('.RES', group=True, children=children)

        # imperative
        children = [
            LemmaTree('.S', lemma=inflections['imper']['s'], children=[create_lsuffix_lemmatree(prs=False)]),
            LemmaTree('.PL', lemma=inflections['imper']['pl'], children=[create_lsuffix_lemmatree(prs=False)]),
        ]
        imp = LemmaTree('.IMP', group=True, children=children)

        # infinitive
        inf = LemmaTree('.INF', lemma=inflections['inf'])

        # progressive
        children = [
            create_compound_obj_lemmatree(),
            create_enclitic_copula_lemmatree(ə_elidable=True),
        ]
        prog = LemmaTree('.PROG', lemma=inflections['prog'], children=children)
        
        # verbal noun
        vn = LemmaTree('.VN', lemma=inflections['vn'])

        # active participle
        children = [
            create_annexation_lemmatree(),
            create_enclitic_copula_lemmatree(),
            create_pronominal_suffix_lemmatree(annexable=True),
        ]
        children = [
            LemmaTree('.MS', lemma=inflections['ap']['ms'], children=deepcopy(children)),
            LemmaTree('.FS', lemma=inflections['ap']['fs'], children=deepcopy(children)),
            LemmaTree('.PL', lemma=inflections['ap']['pl'], children=deepcopy(children)),
        ]
        aprt = LemmaTree('.APRT', group=True, children = children)

        children = [
            prs,
            pst,
            res,
            imp,
            inf,
            prog,
            vn,
            aprt,
        ]

        super().__init__(definition, group=True, children=children)


class Adjective(LemmaTree):
    def __init__(
        self,
        definition: str,
        ms: Union[str, None] = None,
        fs: Union[str, None] = None,
        pl: Union[str, None] = None,
        invar: Union[str, None] = None,
    ):
        children = [
            LemmaTree('.MS', lemma=ms, children=[create_annexation_lemmatree(), create_enclitic_copula_lemmatree()]),
            LemmaTree('.FS', lemma=fs, children=[create_annexation_lemmatree(), create_enclitic_copula_lemmatree()]),
            LemmaTree('.PL', lemma=pl, children=[create_annexation_lemmatree(), create_enclitic_copula_lemmatree()]),
            LemmaTree('.INVAR', lemma=invar, children=[create_annexation_lemmatree(), create_enclitic_copula_lemmatree()]),
        ]
        super().__init__(definition, group=True, children=children)
    
    def __repr__(self):
        return f"<Adj '{self.abbrev}'>"


class Noun(LemmaTree):
    def __init__(
        self,
        definition: str,
        ms: Union[str, None] = None,
        fs: Union[str, None] = None,
        pl: Union[str, None] = None,
        annexed: Union[str, None] = None,
    ):
        children = [
            create_annexation_lemmatree(lemma=annexed),
            create_enclitic_copula_lemmatree(),
            create_pronominal_suffix_lemmatree(annexable=True),
        ]
        children = [
            LemmaTree('.MS', lemma=ms, children=deepcopy(children)),
            LemmaTree('.FS', lemma=fs, children=deepcopy(children)),
            LemmaTree('.PL', lemma=pl, children=deepcopy(children)),
        ]
        super().__init__(definition, group=True, children=children)
    
    def __repr__(self):
        return f"<Noun '{self.abbrev}'>"


class Adverb(LemmaTree):
    def __init__(
        self,
        definition: str,
        lemma: str,
        copula_base: str = None,
    ):
        children = [create_enclitic_copula_lemmatree()]
        if copula_base:
            children = LemmaTree('.(copula base)', lemma=copula_base, children=children)
        super().__init__(definition, lemma=lemma, children=children)

    def __repr__(self):
        return f"<Adverb '{self.abbrev}'>"


class Quantifier(LemmaTree):
    def __init__(self, definition: str, lemma: str):
        children = [create_enclitic_copula_lemmatree()]
        super().__init__(definition, lemma=lemma, children=children)

    def __repr__(self):
        return f"<Quantifier '{self.abbrev}'>"


class Preposition(LemmaTree):
    def __init__(
        self,
        definition: str,
        uninflected: str = None,
        proclitic: str = None,
        annexation_base: str = None,
        pronominal_suffix_base: str = None,
    ):
        self.uninflected = uninflected
        self.proclitic = proclitic
        self.annexation_base = annexation_base
        self.pronominal_suffix_base = pronominal_suffix_base
        children = [
            LemmaTree('.(uninflected)', lemma=uninflected),
            LemmaTree('.(proclitic)', lemma=proclitic),
            LemmaTree('.(annexation_base)', lemma=annexation_base, children=[create_annexation_lemmatree()]),
            LemmaTree('.(pronominal_suffix_base)', lemma=pronominal_suffix_base, children=[create_pronominal_suffix_lemmatree()]),
        ]

        super().__init__(definition, group=True, children=children)
    
    def __repr__(self):
        return f"<Preposition '{self.abbrev}'>"


class UninflectedParticle(LemmaTree):
    def __init__(self, definition: str, lemma: str):
        super().__init__(definition, lemma=lemma)
    
    def __repr__(self):
        return f"<UninflectedParticle '{self.abbrev}'>"
