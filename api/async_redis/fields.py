from .exceptions import ExceptionHandler

class Instr :

    SET = 'SET'
    GET = 'GET'
    HSET = 'HSET'
    HGET = 'HGET'


class Field(object):

    def __init__(self, value ,intr ,indexable): #, column_type):

        self.value = value
        self.__instr__ = intr
        self.__indexable__ = indexable

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.value)


class FieldHash(object):

    def __init__(self, value ,intr ,indexable): #, column_type):

        self.value = value
        self.__instr__ = intr
        self.__indexable__ = indexable

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.value)


class StringFieldHash(FieldHash):

    value: str 
    def __init__(self, value: str = '' ,indexable: bool = False):

        if isinstance(value , str) and isinstance(indexable , bool):
            super(StringFieldHash, self).__init__(value ,Instr.SET ,indexable)

        else :
            raise ExceptionHandler('The value field must be a string')


class PkFieldHash(FieldHash):

    value: str
    def __init__(self, value: str = ''):

        if isinstance(value , str) : 
            super(PkFieldHash, self).__init__(value ,Instr.SET ,indexable= False )

        else :
            raise ExceptionHandler('The value field must be a string')


class IntegerFieldHash(FieldHash):

    value: int
    def __init__(self, value: int = 0 ,indexable: bool = False):

        if isinstance(value , int) and isinstance(indexable , bool):
            super(IntegerFieldHash, self).__init__(value ,Instr.SET ,indexable)

        else :
            raise ExceptionHandler('The value field must be a integer')


class ListFieldHash(FieldHash):

    value: list
    def __init__(self, value: list = [] ,indexable : bool = False):

        if isinstance(value , list) and isinstance(indexable , bool):
            super(ListFieldHash, self).__init__(value ,Instr.SET ,indexable)
        else :
            raise ExceptionHandler('The value field must be a list')


class DictFieldHash(FieldHash):

    value: dict
    def __init__(self, value: dict = {} ,indexable: bool = False):

        if isinstance(value , dict) and isinstance(indexable , bool):
            super(DictFieldHash, self).__init__(value ,Instr.SET ,indexable)
        else :
            raise ExceptionHandler('The value field must be a dict')


class StringField(Field):

    value: str 
    def __init__(self, value: str = '' ,indexable: bool = False):

        if isinstance(value , str) and isinstance(indexable , bool):
            super(StringField, self).__init__(value ,Instr.SET ,indexable)
        else :
            raise ExceptionHandler('The value field must be a string')
