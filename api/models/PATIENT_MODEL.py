from async_redis.redis_orm import Model
from async_redis.fields import (
        HashField,
        PkField,
        StringField
        )


class Patient(Model):

        patientId      = PkField()
        nationalNumber = HashField(indexable= True)
        firstName      = HashField(indexable= True)
        lastName       = HashField(indexable= True)
        fullName       = HashField(indexable= True) 
        numberPhone    = HashField(indexable= True)
        birthDate      = HashField()
        insurance      = HashField()
        subInsurance   = HashField()
        exDate         = HashField()

        infoHash       = HashField()


class PatientSession(Model):
        
        cpartySessionId = PkField()
        nationalNumber  = HashField(indexable= True)
        numberPhone     = HashField(indexable= True)

