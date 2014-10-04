from pixie.vm.object import Object, Type
from pixie.vm.primitives import nil, true, false


class Keyword(Object):
    _type = Type(u"Keyword")

    def __init__(self, name):
        self._name = name

    def type(self):
        return Keyword._type


class KeywordCache(object):
    def __init__(self):
        self._cache = {}

    def intern(self, nm):
        kw = self._cache.get(nm, None)

        if kw is None:
            kw = Keyword(nm)
            self._cache[nm] = kw

        return kw

_kw_cache = KeywordCache()

def keyword(nm):
    return _kw_cache.intern(nm)

