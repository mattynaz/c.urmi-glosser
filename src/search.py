from lemmatree import LemmaTree


# class Trie:
#     def __init__(self):
#         pass

#     def insert(key, val):
#         pass

#     def search(key):
#         pass

def closeness(path: str, target: str, query: str) -> float:
    if not target.startswith(query):
        return 0
    depth = path.count(' ') + path.count('.') + path.count('-')
    return 1 / (1 + depth)


def search_lemmatree(lt: LemmaTree, query: str, path: str=''):
    matches = []
    path += lt.abbrev

    if not lt.group:
        score = closeness(path, lt.lemma, query)
        if score:
            matches.append((lt.abbrev, lt.lemma, score))

    for c in lt.children:
        for result in search_lemmatree(c, query, path=path):
            matches.append((
                lt.abbrev + result[0],
                result[1],
                result[2],
            ))

    return matches


def search_lexicon(query: str, lexicon):
    if not query:
        return []

    matches = []

    for lt in lexicon:
        matches.extend(search_lemmatree(lt, query))
    
    matches.sort(key=lambda x: x[-1], reverse=True)
    return matches
