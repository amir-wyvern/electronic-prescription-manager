from async_redis.redis_obj import redis
from async_redis.exceptions import ExceptionHandler
import json

class Funcs:    
    
    @staticmethod
    async def save(self ):
        
        if not self._saveState:
            raise ExceptionHandler(f'{self.__class__.__name__}() ,You have not any argument, so you can not use the "save" method')

        main_key = self.__class__.__name__.lower()

        if self.__pk__ : 

            main_key += ':{0}:{1}'.format( self.__pk__['key'],getattr(self ,self.__pk__['key']) ) 

        dic = {}
        objDict = self.__objMappings__
        objDict.update({self.__pk__['key'] : self.__pk__['value']})

        if self.__valueMappings__ :
            for k ,v in self.__valueMappings__.items(): 
                
                if objDict[k].__indexable__ and v not in [None ,'']:
                    table_name = self.__class__.__name__.lower()
                    pk_value = getattr(self ,self.__pk__['key'])
                    await redis._sadd(f'{table_name}:{k}:{v}' ,pk_value )

                dic[k] = v
            await redis._hset(main_key ,dic )
        
        return True

    @staticmethod
    async def getItem(self, _tuple):

        kwrgs = _tuple[0]
        ls_instr = []
        ls_fin = []
        main_key = self.__class__.__name__.lower()

        if self.__pk__ and self.__pk__['key'] in kwrgs.keys():
            data = await redis._hgetall('{0}:{1}:{2}'.format(main_key ,self.__pk__['key'] ,kwrgs[self.__pk__['key']] ))
            ls_fin.append(data)

        else:

            for k ,v in kwrgs.items() :

                if k in self.__objMappings__.keys() :
                    data = await redis._smembers('{0}:{1}:{2}'.format(main_key ,k ,v) )
                    data = list(data)
                    ls_instr.append(data)
                
                else:
                    raise ExceptionHandler(f'key {k} not found')

            temp = None
            for ls_result in ls_instr:
                if not temp:
                    temp = ls_result
                    continue
                temp = list(set(temp).intersection(set(ls_result)))

            for req in temp :
                data = await redis._hgetall('{0}:{1}:{2}'.format(main_key ,self.__pk__['key'] ,req) )
                data[self.__pk__['key']] = req
                ls_fin.append(data)

        return ls_fin

    @staticmethod
    async def getHItem(self ,_tuple):

        key ,field = _tuple
        main_key = self.__class__.__name__.lower()

        mainMatch = main_key + ':' + key 
        # await redis.hg

    @staticmethod
    async def search(self ,_tuple): 

        subKey ,match ,_type = _tuple

        main_key = self.__class__.__name__.lower()
        match ='*' + '*'.join(match.split(' ')) + '*'
        mainMatch = main_key + ':' + subKey + ':' + match
        
        resSearch = await redis._iterScan(mainMatch ,_type= _type ,count=500)

        num = 0
        lsResult= []
        async for i in resSearch:
            lsResult.append(i)  
            num += 1
            if num == 10:
                break

        ls = []
        for item in lsResult:
            ls.append(list(await redis._smembers(item))[0])

        return list(zip(lsResult ,ls))

    @staticmethod
    async def addFavorit(self):
        
        if not self._saveState:
            raise ExceptionHandler(f'{self.__class__.__name__}() ,You have not any argument, so you can not use the "save" method')

        main_key = self.__class__.__name__.lower()

        if self.__pk__ : 

            main_key += ':{0}:{1}'.format( self.__pk__['key'] ,getattr(self ,self.__pk__['key']) ) 

        dic = {}

        objDict = self.__objMappings__
        # objDict.update({self.__pk__['key'] : self.__pk__['value']})

        if self.__valueMappings__ :
            for k ,v in self.__objMappings__.items(): 
                v = json.dumps(self.__valueMappings__[k] )
                dic[v] = 1
            
            await redis._zadd(main_key ,dic )
        
        return True 

    @staticmethod
    async def getFavorit(self ,_tuple):
        
        num = _tuple[0]

        if not self._saveState:
            raise ExceptionHandler(f'{self.__class__.__name__}() ,You have not any argument, so you can not use the "save" method')

        main_key = self.__class__.__name__.lower()

        if self.__pk__ : 

            main_key += ':{0}:{1}'.format( self.__pk__['key'] ,getattr(self ,self.__pk__['key']) ) 

            result = await redis._zrevrangebyscore(main_key ,min='+inf' ,max= 0 ,start= 0 ,num= num )
            ls= []
            for item in result:
                try:
                    ls.append(json.loads(item))
                except:
                    pass

            return ls