class ClassMethods(object):
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


