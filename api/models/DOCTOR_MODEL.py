from async_redis.redis_orm import Model
from async_redis.fields import (
        HashField,
        PkField,
        StringField
        )


class NobanDoctor(Model):

        doctorId           = PkField()
        nationalNumber     = HashField(indexable=True)
        firstName          = HashField(indexable=True)
        lastName           = HashField(indexable=True)
        fullName           = HashField(indexable=True)
        numberPhone        = HashField(indexable=True)
        birthDate          = HashField()
        medicalCouncilCode = HashField(indexable= True)
        contractingLicense = HashField()
        salamatContract    = HashField()
        taminContract      = HashField()

        docFavorits         = HashField()

        salamatUsername    = HashField(indexable= True)
        salamatPassword    = HashField()

        infoHash           = HashField()


class DoctorSession(Model):

        userId                  = PkField()
        sessionId               = StringField()
        accessNodes             = StringField() # []
        additionalProperties    = StringField() # []
        contractingPartyLicense = StringField()
        twoStep                 = StringField() # bool


        