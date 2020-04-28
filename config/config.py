class config():

    # database://user:password@host:port/databasename
    DEBUG =True
    SECRET_KEY ='chegyufgowuhf'



class Development(config):
    # database://user:password@host:port/databasename
    SQLALCHEMY_DATABASE_URI= 'postgresql:postgres:123456@127.0.0.1:5432/inventory_management_system'
 

class Production(config):
    SQLALCHEMY_DATABASE_URI='postgres://zqgtjktttrhkai:084fd839350946db1d97269c132c0f717a5dc954b6380c3172d407387de6cc0e@ec2-52-201-55-4.compute-1.amazonaws.com:5432/d5agpncjn4ork6'
    SECRET_KEY='secretcode'

    