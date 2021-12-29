from async_redis.funcs import Funcs

from async_redis.exceptions import ExceptionHandler
from async_redis.fields import (
    SortedSet,
    PkField ,
    HashField,
    StringField
    )
from copy import deepcopy


def comLambda(_name):

    return lambda _obj ,_tuple : getattr(Funcs() ,_name)(_obj ,_tuple) if _tuple else getattr(Funcs() ,_name)(_obj)


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)

        objMappings = dict()

        ls_pk = [{k: v} for k ,v in attrs.items() if isinstance(v, PkField)] 
        attrs['__pk__'] = {}

        if ls_pk:

            if len(ls_pk) > 1:

                raise AttributeError("The 'Model' can only have one 'PkFiled' attribute" )
                
            attrs['__pk__']['key'] = list(ls_pk[0].keys())[0]
            attrs['__pk__']['value'] = list(ls_pk[0].values())[0]   
            attrs.pop( list(ls_pk[0].keys())[0] )

            ls = []
            newAttrs= {}
            for k ,v in attrs.items():
                if type(v) in [StringField ,HashField ,SortedSet ]:
                    for _name in v.__lsfuncs__:

                        if _name not in ls:

                            newAttrs[_name] = comLambda(_name)
                            ls.append(_name)   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

                    objMappings[k] = v 
            
            attrs.update(newAttrs) 
            attrs['__objMappings__'] = objMappings.copy()

            return type.__new__(cls, name, bases, attrs)
            
        else:
            raise AttributeError("The 'Model' must have one 'PkFiled' attribute" )

    def __call__(self, *args, **kwrgs) :

        if not kwrgs:
            self._saveState = False
            self.wwwwww = 9
            
            return super().__call__(*args, **kwrgs)

        self._saveState = True

        total = deepcopy(self.__objMappings__)
        self.__valueMappings__ = {}
        if self.__pk__['key'] not in kwrgs:
            raise ExceptionHandler('Pk not found!')

        if kwrgs[self.__pk__['key']] == None or kwrgs[self.__pk__['key']] == '' :
            raise ExceptionHandler(f'type None or empty string is not valid for Pk')

        total.update({self.__pk__['key'] : self.__pk__['value'] })
        for k ,v in kwrgs.items():
            if k in total:

                self.__valueMappings__[k] = v
                # self.__typeCheck__(v ,total[k]) 
                setattr(self ,k ,kwrgs[k]) 

            else:
                raise ExceptionHandler(f'"{k}" argument is unknown ')
        z = super().__call__(*args, **kwrgs)
        return z

    def __typeCheck__(self ,pType ,value):
        if type(value) != pType.__annotations__['value'] :
            if type(value) == None:
                return
            raise ExceptionHandler(f"type '{value}' is not equal type with {pType.__annotations__['value']}")


class Model( metaclass= ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__()
