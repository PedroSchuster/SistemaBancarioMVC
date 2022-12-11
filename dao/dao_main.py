import collections
import pickle


class DAO():
    def __init__(self, datasource = ''):
        self.__datasource = datasource
        self.__cache = collections.defaultdict(list)
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()
    
    def __dump (self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load (self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add (self, key, obj):
        self.__cache[key].append(obj)
        self.__dump()

    def get_list (self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass
    
    def get_one (self, index, key):
        return self.__cache[key][index]

    def remove (self, index, key):
        try:
            #ultimo_valor = self.__cache[key][-1]
            #self.__cache[key][-1] = self.__cache[key][index]
            #self.__cache[key][index] = ultimo_valor

            self.__cache[key].pop(index)
            
            self.__dump()
        except KeyError:
            pass
    
    def modify (self, index, key, obj):
        try:
            self.__cache[key][index] = obj
        except KeyError:
            pass