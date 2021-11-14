from async_redis import Model
from async_redis import (
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


class Favorit(Model):

        doctorId : str = PkFieldHash() 
        detail   : str = StringFieldHash() # patient mobile number

