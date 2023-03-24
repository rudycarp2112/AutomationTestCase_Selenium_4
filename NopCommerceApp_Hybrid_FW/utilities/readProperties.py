import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\RudyX\\PycharmProjects\\TestingProyect_begin\\NopCommerceApp_Hybrid_FW\\Configurations\\config.ini")

class ReadConfig():
    # Create 3 static methods for every variable we need to create a function
    @staticmethod #This manner we can call this method only calling the class and method instead of create an object of the class
    def getApplicationUrl():
        url=config.get("common info","base_url")
        return url

    @staticmethod
    def getUserEmail():
        name=config.get("common info","username")
        return name

    @staticmethod
    def getUserPassword():
        pwd=config.get("common info","password")
        return pwd