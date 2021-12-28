from async_redis.redis_orm import Model
from async_redis.fields import (
                                HashField,
                                PkField,
                                StringField
                                )


{
'srvName': ' CYTARABINE INJECTION, POWDER, FOR SOLUTION  100MG',
'srvCode': '0000052393', 
'srvType': {
            'srvType': '01', 
            'srvTypeDes': None, 
            'status': None
            }, 

'srvBimSw': '1',
'gSrvCode': None, 
'wsSrvCode': '52393', 
'parTarefGrp': None
}


class TaminDrugs(Model):

        srvCode     = PkField() 
        srvName     = HashField(indexable=True)
        srvType     = HashField()
        srvTypeDes  = HashField()
        status      = HashField()
        srvBimSw    = HashField() 
        gSrvCode    = HashField()
        wsSrvCode   = HashField(indexable=True)
        parTarefGrp = HashField()


class TaminDrugAmnt(Model):

        pkAll = PkField()
        drugAmntCode = HashField()

        # drugAmntId = PkField()
        # drugAmntCode = HashField()
        # drugAmntSumry = HashField()
        # drugAmntLatin = HashField(indexable= True)
        # drugAmntConcept = HashField(indexable= True)
