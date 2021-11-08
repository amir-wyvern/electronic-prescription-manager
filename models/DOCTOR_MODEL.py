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


# class TaminDoctor(Model):

#         doctorId        = StringFieldHash(indexable=True)
#         nationalNumber  = StringFieldHash(indexable=True)
#         firstName       = StringFieldHash(indexable=True)
#         lastName        = StringFieldHash(indexable=True)
#         numberPhone     = StringFieldHash(indexable=True)
#         birthDate       = StringFieldHash()
#         username         = StringFieldHash(indexable= True)
#         password         = StringFieldHash(indexable= True)
        
#         taminContract   = StringFieldHash()
#         infoHash        = StringFieldHash()

# class SalamatDoctor(Model):

#         doctorId           = StringFieldHash(indexable=True)
#         nationalNumber     = StringFieldHash(indexable=True)
#         firstName          = StringFieldHash(indexable=True)
#         lastName           = StringFieldHash(indexable=True)
#         numberPhone        = StringFieldHash(indexable=True)
#         birthDate          = StringFieldHash()
#         username           = StringFieldHash(indexable= True)
#         password           = StringFieldHash(indexable= True)
#         پedicalCouncilCode = StringFieldHash(indexable= True)
#         salamatContract    = StringFieldHash()
#         infoHash           = StringFieldHash()


class NobanDoctor(Model):

        doctorId           = StringFieldHash(indexable=True)
        nationalNumber     = StringFieldHash(indexable=True)
        firstName          = StringFieldHash(indexable=True)
        lastName           = StringFieldHash(indexable=True)
        numberPhone        = StringFieldHash(indexable=True)
        birthDate          = StringFieldHash()
        nbnUsername       = StringFieldHash(indexable= True)
        nbnPassword       = StringFieldHash()
        medicalCouncilCode  = StringFieldHash(indexable= True)
        contractingLicense = StringFieldHash()

        salamatContract    = StringFieldHash()

        salamatUsername    = StringFieldHash(indexable= True)
        salamatPassword    = StringFieldHash()

        infoHash           = StringFieldHash()


class DoctorTmp(Model):

        pass

class DoctorSession(Model):

        sessionId              = StringField()
        accessNodes            = StringField() # []
        additionalProperties    = StringField() # []
        userId                  = StringField()
        contractingPartyLicense = StringField()
        twoStep                = StringField() # bool


        