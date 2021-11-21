from async_redis.redis_obj import redis

from models.DOCTOR_MODEL import DoctorSession
import aiohttp
import asyncio 

class URLS:

    SALAMAT_TEST = 'http://test.ihio.gov.ir/erx-core/v0/service/'
    SALAMAT_MAIN = 'https://webapi.ihio.gov.ir/erx-core/v1/service/'
    
    SALAMAT      = SALAMAT_TEST
 
    TAMIN_MAIN   = 'http://soa.tamin.ir/interface/epresc/'
    TAMIN_TEST   = 'http://soa.tamin.ir/interface/epresc/'

    TAMIN = TAMIN_TEST

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



class Pateint(URLS):

    async def getInfo(self ,national_number):


        tasks = [
                # self.request('get' , self.Tamin) ,
                self.request('get' , self.DoOpenCitizenSession ) ,
                ]

        result = await asyncio.gather(*tasks)


        # ================ check tamin and salamat and save it to redis ================
        pass
        # ===========================================================================



        """
        import uuid
        if not in redis :
            while redis.set(patient:uuid):
                pass
        """

        return result

    async def sendPresc(self ,data):
        
        # check insurance type and send presc
        pass


class Doctor():

    async def getSession(self ,username ,password):

        resp = salamatHandler.getSession(username ,password)
        obj = DoctorSession(
                            sessionId= resp['info']['sessionId'] ,
                            accessNodes=resp['info']['accessNodes'],
                            additionalProperties=resp['info']['additionalProperties'],
                            userId=resp['info']['userId'],
                            contractingPartyLicense=resp['info']['contractingPartyLicense'],
                            twoStep=resp['info']['twoStep'],
                            )
        obj.save()


    

