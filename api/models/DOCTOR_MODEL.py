from async_redis.redis_orm import Model
from async_redis.fields import (
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


class NobanDoctor(Model):

        doctorId           = StringFieldHash(indexable=True)
        nationalNumber     = StringFieldHash(indexable=True)
        firstName          = StringFieldHash(indexable=True)
        lastName           = StringFieldHash(indexable=True)
        fullName           = StringFieldHash(indexable=True)
        numberPhone        = StringFieldHash(indexable=True)
        birthDate          = StringFieldHash()
        medicalCouncilCode = StringFieldHash(indexable= True)
        contractingLicense = StringFieldHash()
        salamatContract    = StringFieldHash()
        taminContract      = StringFieldHash()

        salamatUsername    = StringFieldHash(indexable= True)
        salamatPassword    = StringFieldHash()

        infoHash           = StringFieldHash()


class DoctorSession(Model):

        sessionId               = StringField()
        accessNodes             = StringField() # []
        additionalProperties    = StringField() # []
        userId                  = StringField()
        contractingPartyLicense = StringField()
        twoStep                 = StringField() # bool


        