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
            self.__redis = from_url(f'redis://{host}:{port}' ,decode_responses= True)
            logging.debug('connected to database')
    
    async def close(self) :

        if self.__redis :

            await self.__redis.close()
            logging.debug('closed connection to database')

    async def _set(self ,key ,value):

        return await self.__redis.set(key ,value)

    async def _hset(self ,key ,field ,value):

        return await self.__redis.hset(key ,field )

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


redis = Redis()