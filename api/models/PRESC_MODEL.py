from async_redis.redis_orm import Model
from async_redis.fields import (
        HashField,
        PkField,
        StringField
        )


class TaminPresc(Model):

        prescId          : str = PkField() 
        patient	         : str = HashField(indexable= True) # patient national code
        mobile           : str = HashField(indexable= True) # patient mobile number
        prescTypeId      : str = HashField()                # prescription type find proper one from Prescription Type
        prescDate        : str = HashField()                # prescription date
        docId            : str = HashField()                # doctor valid id
        docMobileNo      : str = HashField(indexable= True) # doctor mobile number
        docNationalCode  : str = HashField(indexable= True) # doctor national code
        comments         : str = HashField()                # comment
        creatorType      : str = HashField()
        siamId           : str = HashField(indexable= True)
         
        noteDetailEprscs : str = HashField() 

        srvType	         : str = HashField()                # defines that current request is for dentist service
        srvCode	         : str = HashField()                # defines that current request is for dentist service
        srvQty	         : str = HashField() 

        # drug
        drugAmntId	 : str = HashField()                # defines that current request is for dentist service
        repeat	         : str = HashField()                # defines that current request is for dentist service
        drugInstId	 : str = HashField()    

        # para
        parGrpCode	 : str = HashField()                # defines that current request is for dentist service


class SalamatPresc(Model):      

        prescId          : str = PkField() 
        cpartySessionId	       : str = HashField()                # patient national code
        citizenSessionId       : str = HashField()                # patient mobile number
        samadCode              : str = HashField(indexable= True) # prescription type find proper one from Prescription Type
        
        subscriptions          : str = HashField()                # prescription date

        id                     : str = HashField()                # sub version ID of the written Presc
        serviceId              : str = HashField(indexable= True) # 
        consumption            : str = HashField()                # drug instruction
        shape	               : str = HashField()                # 
        consumptionInstruction : str = HashField()                # take syrup medicine instruction
        numberOfRequest        : str = HashField()                # 
        numberOfPeriod         : str = HashField()                # 
        description            : str = HashField()                # 
        checkCode	       : str = HashField()                # Check the rules and services of the drug (‫‪checkSubscription‬‬)
