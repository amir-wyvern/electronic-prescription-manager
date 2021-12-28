
class Instr :

    SET = 'SET'
    GET = 'GET'
    HSET = 'HSET'
    HGET = 'HGET'
    

class StringField(object):

    def __init__(self ,indexable= False):

        # self.__instr__ = 
        self.__indexable__ = indexable
        self.__lsfuncs__   = ['save' ,'getItem' ,'search']
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__)


class HashField(object):

    def __init__(self ,indexable= False):

        self.__indexable__ = indexable
        self.__lsfuncs__ = ['save' ,'getItem' ,'search'] 

    def __str__(self):
        return '<%s>' % (self.__class__.__name__)

class PkField(object):

    def __init__(self ,indexable= False):

        self.__indexable__ = indexable
        self.__lsfuncs__ = ['save' ,'getItem' ,'search']

    def __str__(self):
        return '<%s>' % (self.__class__.__name__)

class SortedSet(object):

    def __init__(self ,indexable= False):

        self.__indexable__ = indexable
        self.__lsfuncs__ = ['addFavorit' ,'getFavorit']

    def __str__(self):
        return '<%s>' % (self.__class__.__name__)