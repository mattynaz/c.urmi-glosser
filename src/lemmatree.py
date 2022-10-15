from typing import Callable, List


class LemmaTree:
    def __init__(
        self,
        abbrev: str,
        group: bool = False,
        trans: Callable[[str], str] = None,
        lemma: str = None,
        children: List = []
    ):
        self.abbrev: str = abbrev
        if lemma and ', ' in lemma:
            variants = lemma.split(', ')
            children = [
                LemmaTree(f'.[VARIANT_{i}]', group, trans, lemma, children)
                for i, lemma in enumerate(variants)
            ]
            group = True
            trans = lemma = None

        self.group: bool = group
        self.trans: Callable[[str], str] = trans
        self.lemma: str = lemma
        self.children: List[LemmaTree] = children

    def load(self, path: str = ''):
        children_to_remove = []
        path += self.abbrev

        for c in self.children:
            if type(c) == tuple:
                print(c)
            if c.lemma != None:
                c.load(path=path)
            elif c.trans == None and (c.group or c.trans == ...):
                c.lemma = self.lemma
                c.load(path=path)
            elif c.trans == None:
                children_to_remove.append(c)
            else:
                c.lemma = c.trans(self.lemma, path=path)
                if c.lemma == None:
                    children_to_remove.append(c)
                else:
                    c.load(path=path)

        for c in children_to_remove:
            self.children.remove(c)
    
    
    def __pprint(self, indent_level):
        # print indenting
        print('    '*indent_level, end='')
        
        # print abbreviation
        print(f'{self.abbrev: <4}  ', end='')

        # print lemma
        if self.group:
            print('<group>')
        elif self.lemma:
            print(self.lemma)
        else:
            print('<not loaded>')

        for c in self.children:
            c.__pprint(indent_level+1,)

    def pprint(self):
        self.__pprint(0)

    def __repr__(self):
        return f"<Word '{'(group)' if self.group else self.lemma}'>"
