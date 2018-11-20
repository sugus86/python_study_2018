# -*- coding: utf-8 -*-

class _const:
    class ConstError(TypeError) :
        pass

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise Exception(self.ConstError,"constant reassignment error!")
        self.__dict__[key] = value

import sys
print(__name__)
#sys.modules[__name__] = _const()
