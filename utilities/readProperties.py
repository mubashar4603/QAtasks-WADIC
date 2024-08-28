import configparser

config = configparser.RawConfigParser()
config.read("/home/anonymous/PycharmProjects/QAtask-WADIC/Configurations/config.ini")


class ReadConfig():
    @staticmethod
    def getAppURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getFname():
        fname = config.get('common info', 'fname')
        return fname

    @staticmethod
    def getLname():
        lname = config.get('common info', 'lname')
        return lname
    @staticmethod
    def getEmail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getCompany():
        cname = config.get('common info', 'cname')
        return cname



