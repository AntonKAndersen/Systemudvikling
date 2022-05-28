class ClassMethods(object):
    '''
    ClassMethods bruges som systemets model og det er her alt fra databasen læses ind i når programmet startes.
    '''
    list_anmodninger: list = []
    @classmethod
    def add_anmodning(cls,anmodning):
        cls.list_anmodninger.append(anmodning)

    @classmethod
    def get_anmodninger(cls):
        return cls.list_anmodninger

    list_skema: list = []
    @classmethod
    def add_skema(cls,skema):
        cls.list_skema.append(skema)

    @classmethod
    def get_skema(cls):
        return cls.list_skema

    list_bruger: list = []
    @classmethod
    def add_bruger(cls, bruger):
        cls.list_bruger.append(bruger)

    @classmethod
    def get_bruger(cls):
        return cls.list_bruger

    list_login: list = []
    @classmethod
    def add_login(cls, login):
        cls.list_login.append(login)

    @classmethod
    def get_login(cls):
        return cls.list_login