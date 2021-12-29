from aioredis import from_url
import logging

class Redis ():

    """
    This class prevents the creation of several different objects and connections to the Redis server
    And all requests are sent to the Redis server 
    """

    _instance = None
    def __new__(cls ,*args , **kwargs):

        if not cls._instance :

            cls._instance = super().__new__(cls ,*args ,**kwargs)
            cls.__redis = None

        return cls._instance

    def connect(self ,host ,port):

        if not self.__redis:
            self.__redis = from_url(f'redis://{host}' ,decode_responses= True)
            logging.debug('connected to database')
    
    async def close(self) :

        if self.__redis :

            await self.__redis.close()
            logging.debug('closed connection to database')

    async def _set(self ,key ,value):

        return await self.__redis.set(key ,value)

    async def _hset(self ,key ,mapping ):
       
        return await self.__redis.hset(key  ,mapping= mapping )

    async def _sadd(self ,key ,field):

        return await self.__redis.sadd(key ,field )

    async def _zadd(self ,key ,mapping):

        return await self.__redis.zadd(key ,mapping= mapping) 

    async def _zrevrangebyscore(self ,key ,min ,max ,start ,num ,withscores= False):

        return await self.__redis.zrevrangebyscore(key ,min ,max ,start ,num ,withscores= False)

    async def _smembers(self ,key):

        return await self.__redis.smembers(key )

    async def _srem(self ,key ,members):

        return await self.__redis.srem(key ,members)

    async def _get(self ,key):
        
        return await self.__redis.get(key)

    async def _exists(self ,key):
        
        return await self.__redis.exists(key)

    async def _hget(self ,key ,fields):

        return await self.__redis.hget(key ,fields)

    async def _hgetall(self ,key):

        return await self.__redis.hgetall(key) 

    async def _zscan(self ,key ,match ,cursor= 0):

        return await self.__redis.zscan(name= key ,match= match,cursor= cursor)

    async def _scan(self ,match ,_cursor=0 ,_type= None ,count= None):
        return await self.__redis.scan(match= match ,_type= _type ,count= count ,cursor= _cursor)

    async def _iterScan(self ,match ,_type= None ,count= None):
        return self.__redis.scan_iter(match ,_type= _type ,count= count)

redis = Redis()


