from async_redis.redis_orm import Model
from async_redis.fields import (
        StringField,
        HashField,
        SortedSet,
        PkField
        )


class FavoritDrug(Model):

        doctorId    : str = PkField() 
        jsonData    : str = SortedSet()


class FavoritExper(Model):

        doctorId    : str = PkField() 
        jsonData    : str = SortedSet()


class FavoritPhysio(Model):

        doctorId    : str = PkField() 
        jsonData    : str = SortedSet()

class FavoritImaging(Model):

        doctorId    : str = PkField() 
        jsonData    : str = SortedSet()

class FavoritService(Model):

        doctorId    : str = PkField() 
        jsonData    : str = SortedSet()

