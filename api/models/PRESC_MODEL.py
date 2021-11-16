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


class TaminPresc(Model):

        prescId          : str = PkFieldHash() 
        patient	         : str = StringFieldHash(indexable= True) # patient national code
        mobile           : str = StringFieldHash(indexable= True) # patient mobile number
        prescTypeId      : str = StringFieldHash()                # prescription type find proper one from Prescription Type
        prescDate        : str = StringFieldHash()                # prescription date
        docId            : str = StringFieldHash()                # doctor valid id
        docMobileNo      : str = StringFieldHash(indexable= True) # doctor mobile number
        docNationalCode  : str = StringFieldHash(indexable= True) # doctor national code
        comments         : str = StringFieldHash()                # comment
        creatorType      : str = StringFieldHash()
        siamId           : str = StringFieldHash(indexable= True)
         
        noteDetailEprscs : str = StringFieldHash() 

        srvType	         : str = StringFieldHash()                # defines that current request is for dentist service
        srvCode	         : str = StringFieldHash()                # defines that current request is for dentist service
        srvQty	         : str = StringFieldHash() 

        # drug
        drugAmntId	 : str = StringFieldHash()                # defines that current request is for dentist service
        repeat	         : str = StringFieldHash()                # defines that current request is for dentist service
        drugInstId	 : str = StringFieldHash()    

        # para
        parGrpCode	 : str = StringFieldHash()                # defines that current request is for dentist service


class SalamatPresc(Model):      

        cpartySessionId	       : str = StringFieldHash()                # patient national code
        citizenSessionId       : str = StringFieldHash()                # patient mobile number
        samadCode              : str = StringFieldHash(indexable= True) # prescription type find proper one from Prescription Type
        
        subscriptions          : str = StringFieldHash()                # prescription date

        id                     : str = StringFieldHash()                # sub version ID of the written Presc
        serviceId              : str = StringFieldHash(indexable= True) # 
        consumption            : str = StringFieldHash()                # drug instruction
        shape	               : str = StringFieldHash()                # 
        consumptionInstruction : str = StringFieldHash()                # take syrup medicine instruction
        numberOfRequest        : str = StringFieldHash()                # 
        numberOfPeriod         : str = StringFieldHash()                # 
        description            : str = StringFieldHash()                # 
        checkCode	       : str = StringFieldHash()                # Check the rules and services of the drug (‫‪checkSubscription‬‬)