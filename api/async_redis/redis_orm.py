from .redis_obj import redis
from ..logs import Logger
from .exceptions import ExceptionHandler
from .fields import (
    Field ,
    FieldHash,
    Instr ,
    PkFieldHash ,
    StringFieldHash ,
    IntegerFieldHash ,
    ListFieldHash ,
    DictFieldHash ,
    StringField
    )

logger= Logger()

class ModelMetaclass(type):

    def __call__(self, *args, **kwrgs) :

        if not kwrgs:
            self._saveState = False
            return super().__call__(*args, **kwrgs)

        self._saveState = True

        total = {**self.__mappings__ ,**self.__mappings_hash__}
        if self.__pk__:

            if len(total)+1 != len(kwrgs):
                raise ExceptionHandler(f'{self.__name__}() takes {len(kwrgs)} positional argument but {len(total)} were given')

            if not self.__pk__['key'] in kwrgs:
                raise ExceptionHandler('No value with "PkFieldHash" type found')

            self.__pk__['value'] = kwrgs[self.__pk__['key']]

            for k ,v in total.items():
                if k in kwrgs:
                    self.__typeCheck__(v ,kwrgs[k])
                    setattr(self ,k ,kwrgs[k]) 

                else:
                    raise ExceptionHandler(f'"{k}" argument is unknown ')

        else:

            if len(total) != len(kwrgs):
                raise ExceptionHandler(f'{self.__name__}() takes {len(kwrgs)} positional argument but {len(total)} were given')

            for k ,v in total.items():
                if k in kwrgs:
                    setattr(self ,k ,kwrgs[k]) 

                else:
                    raise ExceptionHandler(f'"{k}" argument is unknown ')
            

        return super().__call__(*args, **kwrgs)

    def __new__(cls, name, bases, attrs):
        
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)

        mappings_hash = dict()
        mappings = dict()
        ls_pk = [{k: v} for k ,v in attrs.items() if isinstance(v, PkFieldHash)]
    
        attrs['__pk__'] = {}
        if ls_pk:
            
            if len(ls_pk) > 1:

                raise AttributeError("The 'Model' can only have one 'PkFiled' attribute" )
                
            attrs['__pk__']['key'] = list(ls_pk[0].keys())[0]
            attrs['__pk__']['value'] = list(ls_pk[0].values())[0]   
            attrs.pop( list(ls_pk[0].keys())[0] )

        for k, v in attrs.items():
            if isinstance(v, FieldHash):                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                mappings_hash[k] = v

            elif isinstance(v, Field):                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                mappings[k] = v 
        

        for k in mappings_hash.keys():
            attrs.pop(k)

        attrs['__mappings_hash__'] = mappings_hash
        attrs['__mappings__'] = mappings
      
        return type.__new__(cls, name, bases, attrs)

    def __typeCheck__(self ,pType ,value):
        
        if type(value) != pType.__annotations__['value']:
            raise ExceptionHandler(f"type '{value}' is not equal type with {pType.__annotations__['value']}")


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):

        try:
            return self[key]    

        except KeyError:

            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self ,key ,value):

        self[key] = value

    def save(self):

        if not self._saveState:
            raise ExceptionHandler(f'{self.__class__.__name__}() ,You have not any argument, so you can not use the "save" method')


        main_key = self.__class__.__name__.lower()

        if self.__pk__ : 

            main_key += ':' + self.__pk__['value']

        list_instr = []
        ls_fields = []
        instr = 'redis.call({})'
        str_eval = []

        if self.__mappings_hash__ :
            for k, v in self.__mappings_hash__.items():
                if v.__indexable__:
                    
                    table_name = self.__class__.__name__.lower()
                    pk_value = self.__pk__['value'] 
                    str_eval.append(f'redis.call("SADD" ,{table_name}:{k}:{getattr(self ,k)} ,{pk_value})')
                    list_instr.append( f'SADD {table_name}:{k}:{getattr(self ,k)} {pk_value}' )

                ls_fields.append(f'{k} {getattr(self ,k)}')

            val = ' '.join(ls_fields)
            str_eval.append(f'redis.call("HSET" ,{main_key} ,{val})')
            list_instr.append('HSET ' + main_key + ' ' + ' '.join(ls_fields)) 

        for k, v in self.__mappings__.items():

            key = main_key + ':' + k
            str_eval.append(f'redis.call("{v.__instr__}" ,{key} ,{getattr(self ,k)})')
            list_instr.append( f'{v.__instr__} {key} {getattr(self ,k)}' )

        print(str_eval)
        print(list_instr)

        # for inst in list_instr:
        #     if inst.startswith('SET'):
        #         await redis._set()

    def find(self, **kwrgs):
        
        ls_instr = []
        main_key = self.__class__.__name__.lower()

        for k ,v in kwrgs.items() :
            if k in self.__mappings__.keys() :
                ls_instr.append(f'SMEMBERS {main_key}:{k}:{v}')
            
            else:
                raise ExceptionHandler(f'key {k} not found')

        print(ls_instr)

