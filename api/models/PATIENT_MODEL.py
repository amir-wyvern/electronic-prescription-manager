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

class NobanPatient(Model):

        patientId      = PkFieldHash()
        nationalNumber = StringFieldHash(indexable=True)
        firstName      = StringFieldHash(indexable=True)
        lastName       = StringFieldHash(indexable=True)
        fullName       = StringFieldHash(indexable=True)
        numberNphone   = StringFieldHash(indexable=True)
        birthDate      = StringFieldHash()
        insurance      = StringFieldHash()
        subInsurance   = StringFieldHash()
        exDate         = StringFieldHash()

        infoHash       = StringFieldHash()


class PatientSession(Model):
        
        cpartySessionId = PkFieldHash()
        nationalNumber  = StringFieldHash(indexable= True)
        numberPhone     = StringFieldHash(indexable= True)

