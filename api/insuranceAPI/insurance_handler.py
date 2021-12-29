from pydantic.fields import T
from async_redis.redis_obj import redis

import aiohttp
import asyncio 

import json

from models.SERVICE_MODEL import (
    TaminDrugs ,
    TaminDrugAmnt,
    TaminExper,
    TaminPhysio,
    TaminImaging,
    TaminService
    )

class TaminUrls:
    
    TAMIN_TEST = 'https://ep-test.tamin.ir/api/'
    TAMIN_MAIN   = 'http://soa.tamin.ir/interface/epresc/' 

    TAMIN = TAMIN_TEST

    TAMIN_SERVICES = { 
        'drug' : '1',
        'exper' : '2', # experimentation
        'radiology' : '3',
        'sono' : '4', # sonography
        'speech' : '10' , # speechTherapy
        'ctScan' : '5',
        'mri' : '6',
        'nuclearMedicine' : '7', 
        'radiotherapy' : '8',
        'audiometry' : '9',
        'angiography' : '11',
        'comServces' : '12' ,# Services complementary to diagnostic measures
        'physiotherapy' : '13',
        'boneDensitometry' :'14',
        'dialysis' : '15',
        'visit' : '16',
        'AncillaryServices' : '17'
    }

    TAMIN_SERVICE_DRUG      = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['drug']
    TAMIN_SERVICE_EXPER     = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['exper']
    TAMIN_SERVICE_RADIOLOGY = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['radiology']
    TAMIN_SERVICE_SP        = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['speech']
    TAMIN_SERVICE_CT        = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['ctScan']
    TAMIN_SERVICE_MRI       = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['mri']
    TAMIN_SERVICE_NMEDICINE = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['nuclearMedicine']
    TAMIN_SERVICE_RADIOTH   = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['radiotherapy']
    TAMIN_SERVICE_AUDIOTH   = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['audiometry']
    TAMIN_SERVICE_ANGIOTH   = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['angiography']
    TAMIN_SERVICE_COMSRVC   = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['comServces']
    TAMIN_SERVICE_PHTH      = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['physiotherapy']
    TAMIN_SERVICE_BONEDE    = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['boneDensitometry']
    TAMIN_SERVICE_DIALYSIS  = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['dialysis']
    TAMIN_SERVICE_VISIT     = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['visit']
    TAMIN_SERVICE_ANSRVC    = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['AncillaryServices']
    TAMIN_SERVICE_SONO      = TAMIN + 'ws-services?serviceType=' + TAMIN_SERVICES['sono']

    TAMIN_DRUG_AMNT         = TAMIN + 'ws-drug-amount'
    TAMIN_DRUG_INST         = TAMIN + 'ws-drug-instruction'


class TaminHandler(TaminUrls):

    async def getDrugs(self ,clause):

        resp = await TaminDrugs().getItem(({'srvCode': '0000090011'},))
        if not resp:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.TAMIN_SERVICE_DRUG) as response:
                    data = await response.json()

                    
            for item in data['data']['list']:

                name = ''
                if item['srvName']:
                    name = str(item['srvName'])

                srvType = ''
                if item['srvType']['srvType']:
                    srvType = str(item['srvType']['srvType'])

                srvTypeDes = ''
                if item['srvType']['srvTypeDes']:
                    srvTypeDes = str(item['srvType']['srvTypeDes'])

                status = ''
                if item['srvType']['status'] :
                    status = str(item['srvType']['status'])

                srvBimSw = ''
                if item['srvBimSw'] :
                    srvBimSw = str(item['srvBimSw'])
                
                gSrvCode = ''
                if item['gSrvCode']:
                    gSrvCode= item['gSrvCode']

                wsSrvCode = ''
                if item['wsSrvCode']:
                    wsSrvCode= item['wsSrvCode']

                parGrpCode = '' 
                if item['parTarefGrp'] and 'parGrpCode' in item['parTarefGrp'] and item['parTarefGrp']['parGrpCode']:
                    parGrpCode= item['parTarefGrp']['parGrpCode']

                parGrpDesc = ''
                if item['parTarefGrp'] and 'parGrpDesc' in item['parTarefGrp'] and item['parTarefGrp']['parGrpDesc']:
                    parGrpDesc= item['parTarefGrp']['parGrpDesc']

                await TaminDrugs(
                            srvCode= str(item['srvCode']),
                            srvName= name,
                            srvType= srvType,
                            srvTypeDes= srvTypeDes,
                            status= status,
                            srvBimSw= srvBimSw,
                            gSrvCode= gSrvCode,
                            wsSrvCode= wsSrvCode,
                            parGrpCode= parGrpCode,
                            parGrpDesc= parGrpDesc
                            ).save(None)

        respClause = await TaminDrugs().search(('srvName' ,clause ,'set'))
        if respClause: 
            lsNew = []
            for name ,_id in respClause:
                lsNew.append((' '.join(name.split(':')[2:]) ,_id))
            
            respClause = lsNew

        return respClause

    async def getDrugAmnt(self):
        
        nameClass = 'TaminDrugAmnt'.lower() + ':all'

        resp = await redis._hgetall(nameClass)
        if not resp:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.TAMIN_DRUG_AMNT) as response:
                    data = await response.json()


            dic ={}
            for item in data['data']['list']:
                dic[str(item['drugAmntId'])] = json.dumps(item)

            await redis._hset(nameClass ,dic)

        newLs = []
        resp = await redis._hgetall(nameClass)
        for _id ,jsonData in resp.items():
            try:
                data = json.loads( jsonData )

                newLs.append({'id':_id ,'name':data['drugAmntConcept'].split('-')[0]})
            except:
                pass

        return newLs

    async def getDrugInst(self):

        nameClass = 'TaminDrugInst'.lower() + ':all'

        resp = await redis._hgetall(nameClass)
        if not resp:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.TAMIN_DRUG_INST) as response:
                    data = await response.json()


            dic ={}
            for item in data['data']['list']:
                dic[str(item['drugInstId'])] = json.dumps({'drugInstConcept':item['drugInstConcept'],
                                                           'drugInstId':str(item['drugInstId']),
                                                            'drugInstCode':item['drugInstCode']}    )

            await redis._hset(nameClass ,dic)

        newLs = []
        resp = await redis._hgetall(nameClass)
        for _id ,jsonData in resp.items():
            try:
                data = json.loads( jsonData )

                newLs.append({'id':_id ,'name':data['drugInstConcept']})
            except:
                pass

        return newLs

    async def getExper(self ,clause):
        
        resp = await TaminExper().getItem(({'srvCode': '030246-300'},))
        
        if not resp:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.TAMIN_SERVICE_EXPER) as response:
                    data = await response.json()

                    
            for item in data['data']['list']:
               
                name = ''
                if item['srvName']:
                    name = str(item['srvName'])

                srvType = ''
                if item['srvType']['srvType']:
                    srvType = str(item['srvType']['srvType'])

                srvTypeDes = ''
                if item['srvType']['srvTypeDes']:
                    srvTypeDes = str(item['srvType']['srvTypeDes'])

                status = ''
                if item['srvType']['status'] :
                    status = str(item['srvType']['status'])

                srvBimSw = ''
                if item['srvBimSw'] :
                    srvBimSw = str(item['srvBimSw'])
                
                gSrvCode = ''
                if item['gSrvCode']:
                    gSrvCode= item['gSrvCode']

                wsSrvCode = ''
                if item['wsSrvCode']:
                    wsSrvCode= item['wsSrvCode']

                parGrpCode = '' 
                if item['parTarefGrp'] and 'parGrpCode' in item['parTarefGrp'] and item['parTarefGrp']['parGrpCode']:
                    parGrpCode= item['parTarefGrp']['parGrpCode']

                parGrpDesc = ''
                if item['parTarefGrp'] and 'parGrpDesc' in item['parTarefGrp'] and item['parTarefGrp']['parGrpDesc']:
                    parGrpDesc= item['parTarefGrp']['parGrpDesc']

                await TaminExper(
                            srvCode= str(item['srvCode']),
                            srvName= name,
                            srvType= srvType,
                            srvTypeDes= srvTypeDes,
                            status= status,
                            srvBimSw= srvBimSw,
                            gSrvCode= gSrvCode,
                            wsSrvCode= wsSrvCode,
                            parGrpDesc= parGrpDesc,
                            parGrpCode= parGrpCode
                            ).save(None)

        respClause = await TaminExper().search(('srvName' ,clause ,'set'))
        if respClause: 
            lsNew = []
            for name ,_id in respClause:
                lsNew.append((' '.join(name.split(':')[2:]) ,_id))
            
            respClause = lsNew

        return respClause
        
    async def getPhysio(self ,clause):
        
        resp = await TaminPhysio().getItem(({'srvCode': '030246-300'},))
        
        if not resp:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.TAMIN_SERVICE_PHTH) as response:
                    data = await response.json()

                    
            for item in data['data']['list']:
                name = ''
                if item['srvName']:
                    name = str(item['srvName'])

                srvType = ''
                if item['srvType']['srvType']:
                    srvType = str(item['srvType']['srvType'])

                srvTypeDes = ''
                if item['srvType']['srvTypeDes']:
                    srvTypeDes = str(item['srvType']['srvTypeDes'])

                status = ''
                if item['srvType']['status'] :
                    status = str(item['srvType']['status'])

                srvBimSw = ''
                if item['srvBimSw'] :
                    srvBimSw = str(item['srvBimSw'])
                
                gSrvCode = ''
                if item['gSrvCode']:
                    gSrvCode= item['gSrvCode']

                wsSrvCode = ''
                if item['wsSrvCode']:
                    wsSrvCode= item['wsSrvCode']

                parGrpCode = '' 
                if item['parTarefGrp'] and 'parGrpCode' in item['parTarefGrp'] and item['parTarefGrp']['parGrpCode']:
                    parGrpCode= item['parTarefGrp']['parGrpCode']

                parGrpDesc = ''
                if item['parTarefGrp'] and 'parGrpDesc' in item['parTarefGrp'] and item['parTarefGrp']['parGrpDesc']:
                    parGrpDesc= item['parTarefGrp']['parGrpDesc']


                await TaminPhysio(
                            srvCode= str(item['srvCode']),
                            srvName= name,
                            srvType= srvType,
                            srvTypeDes= srvTypeDes,
                            status= status,
                            srvBimSw= srvBimSw,
                            gSrvCode= gSrvCode,
                            wsSrvCode= wsSrvCode,
                            parGrpCode= parGrpCode,
                            parGrpDesc= parGrpDesc
                            ).save(None)

        respClause = await TaminPhysio().search(('srvName' ,clause ,'set'))
        if respClause: 
            lsNew = []
            for name ,_id in respClause:
                lsNew.append((' '.join(name.split(':')[2:]) ,_id))
            
            respClause = lsNew

        return respClause
    
    async def getImaging(self ,clause):

        resp = await TaminImaging().getItem(({'srvCode': '036260-800'},))
        
        if not resp:
            async with aiohttp.ClientSession() as session:
                for url in [
                                self.TAMIN_SERVICE_CT ,
                                self.TAMIN_SERVICE_MRI ,
                                self.TAMIN_SERVICE_SONO,
                                self.TAMIN_SERVICE_NMEDICINE,
                                self.TAMIN_SERVICE_RADIOTH
                                ]:

                    async with session.get(url) as response:
                        data = await response.json()
                        
                    for item in data['data']['list']:

                        name = ''
                        if item['srvName']:
                            name = str(item['srvName'])

                        srvType = ''
                        if item['srvType']['srvType']:
                            srvType = str(item['srvType']['srvType'])

                        srvTypeDes = ''
                        if item['srvType']['srvTypeDes']:
                            srvTypeDes = str(item['srvType']['srvTypeDes'])

                        status = ''
                        if item['srvType']['status'] :
                            status = str(item['srvType']['status'])

                        srvBimSw = ''
                        if item['srvBimSw'] :
                            srvBimSw = str(item['srvBimSw'])
                        
                        gSrvCode = ''
                        if item['gSrvCode']:
                            gSrvCode= item['gSrvCode']

                        wsSrvCode = ''
                        if item['wsSrvCode']:
                            wsSrvCode= item['wsSrvCode']

                        parGrpCode = '' 
                        if item['parTarefGrp'] and 'parGrpCode' in item['parTarefGrp'] and item['parTarefGrp']['parGrpCode']:
                            parGrpCode= item['parTarefGrp']['parGrpCode']

                        parGrpDesc = ''
                        if item['parTarefGrp'] and 'parGrpDesc' in item['parTarefGrp'] and item['parTarefGrp']['parGrpDesc']:
                            parGrpDesc= item['parTarefGrp']['parGrpDesc']


                        await TaminImaging(
                                    srvCode= str(item['srvCode']),
                                    srvName= name,
                                    srvType= srvType,
                                    srvTypeDes= srvTypeDes,
                                    status= status,
                                    srvBimSw= srvBimSw,
                                    gSrvCode= gSrvCode,
                                    wsSrvCode= wsSrvCode,
                                    parGrpCode= parGrpCode,
                                    parGrpDesc= parGrpDesc
                                    ).save(None)

        respClause = await TaminImaging().search(('srvName' ,clause ,'set'))

        if respClause: 
            lsNew = []
            for name ,_id in respClause:
                lsNew.append((' '.join(name.split(':')[2:]) ,_id))
            
            respClause = lsNew

        return respClause

    async def getService(self ,clause):

        resp = await TaminService().getItem(({'srvCode': '0000901121'},))
        
        if not resp:
            async with aiohttp.ClientSession() as session:
                for url in [
                                self.TAMIN_SERVICE_SP ,
                                self.TAMIN_SERVICE_AUDIOTH ,
                                self.TAMIN_SERVICE_ANGIOTH,
                                self.TAMIN_SERVICE_DIALYSIS,
                                self.TAMIN_SERVICE_ANSRVC
                                ]:

                    async with session.get(url) as response:
                        data = await response.json()
                        
                    for item in data['data']['list']:

                        name = ''
                        if item['srvName']:
                            name = str(item['srvName'])

                        srvType = ''
                        if item['srvType']['srvType']:
                            srvType = str(item['srvType']['srvType'])

                        srvTypeDes = ''
                        if item['srvType']['srvTypeDes']:
                            srvTypeDes = str(item['srvType']['srvTypeDes'])

                        status = ''
                        if item['srvType']['status'] :
                            status = str(item['srvType']['status'])

                        srvBimSw = ''
                        if item['srvBimSw'] :
                            srvBimSw = str(item['srvBimSw'])
                        
                        gSrvCode = ''
                        if item['gSrvCode']:
                            gSrvCode= item['gSrvCode']

                        wsSrvCode = ''
                        if item['wsSrvCode']:
                            wsSrvCode= item['wsSrvCode']

                        parGrpCode = '' 
                        if item['parTarefGrp'] and 'parGrpCode' in item['parTarefGrp'] and item['parTarefGrp']['parGrpCode']:
                            parGrpCode= item['parTarefGrp']['parGrpCode']

                        parGrpDesc = ''
                        if item['parTarefGrp'] and 'parGrpDesc' in item['parTarefGrp'] and item['parTarefGrp']['parGrpDesc']:
                            parGrpDesc= item['parTarefGrp']['parGrpDesc']


                        await TaminService(
                                    srvCode= str(item['srvCode']),
                                    srvName= name,
                                    srvType= srvType,
                                    srvTypeDes= srvTypeDes,
                                    status= status,
                                    srvBimSw= srvBimSw,
                                    gSrvCode= gSrvCode,
                                    wsSrvCode= wsSrvCode,
                                    parGrpCode= parGrpCode,
                                    parGrpDesc= parGrpDesc
                                    ).save(None)

        respClause = await TaminService().search(('srvName' ,clause ,'set'))

        if respClause: 
            lsNew = []
            for name ,_id in respClause:
                lsNew.append((' '.join(name.split(':')[2:]) ,_id))
            
            respClause = lsNew

        return respClause

class SalamatUrls:
    pass

class URLS:

    SALAMAT_TEST = 'http://test.ihio.gov.ir/erx-core/v0/service/'
    SALAMAT_MAIN = 'https://webapi.ihio.gov.ir/erx-core/v1/service/'
    
    SALAMAT      = SALAMAT_TEST
 

    DoOpenUserSession             = SALAMAT + 'auth/session/cparty/open'
    FetchAgentDailyToken          = SALAMAT + 'auth/token/fetch'
    DoOpenCitizenSession          = SALAMAT + 'auth/session/citizen/open'
    FetchUserInfoBySessionId      = SALAMAT + 'auth/session/fetch/userinfo'
    DoCheckOTP                    = SALAMAT + 'auth/otp/check'
    FetchCitizenInformation       = SALAMAT + 'citizen/fetch'
    DoGenerateSamadCode           = SALAMAT + 'samad/electronic/generate'
    FetchSamadCodeList            = SALAMAT + 'samad/ordered/search'
    FetchSamadCodeListForDeliveredPrescription = SALAMAT + 'samad/delivered/search'
    DoGeneratePaperSamadCode      = SALAMAT + 'samad/paper/generate'
    QuickSearchService            = SALAMAT + 'search/quick'
    FetchGenericCodeByIRCCode     = SALAMAT + 'product/fetch'
    SearchIrcProductByGenericCode = SALAMAT + 'search/irc/generic'
    QuickSearchIRCProduct         = SALAMAT + 'product/search/quick/irc'
    QuickSearchGenericProduct     = SALAMAT + 'product/search/quick/generic'
    FetchCoFamilyProductByGenericCode = SALAMAT + 'product/irc/cofamily/fetch/generic'
    FetchCoFamilyServiceByServiceNN = SALAMAT + 'service/cofamily/fetch/servicenn'
    DoSavePrescription            = SALAMAT + 'prescription/save'
    FetchPrescriptionInfoBySamadCode = SALAMAT + 'prescription/fetch/samad'
    DetchPrescriptionInfoByPrintCode = SALAMAT + 'prescription/fetch/printcode'
    DoDeliveredPrescription       = SALAMAT + 'prescription/deliver'
    FetchPartnerInfoByPrintCode   = SALAMAT + 'partner/fetch'
    CheckSubscription             = SALAMAT + 'subscription/check'
    CheckSubscriptionPrice        = SALAMAT + 'subscription/price/check'
    FetchDeliveredPrescriptionByTrackingCode = SALAMAT + 'prescription/delivered'
    DoUpdatePrescription          = SALAMAT + 'prescription/update'
    PartnerInfo                   = SALAMAT + 'partner/search'
    DoSendPrescriptionToDeliverQueue = SALAMAT + 'deliver/queue/prescription/send'
    FetchDeliverQueue             = SALAMAT + 'deliver/queue/fetch'
    FetchSubPartnerInfoByPartnerId = SALAMAT + 'partner/fetch/partnerid'


