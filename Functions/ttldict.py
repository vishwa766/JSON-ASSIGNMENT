import threading
import time

class TTLDict(dict):

    def __init__(self, ttl):
        self._ttl = ttl
        self.__map = {}
        self._flag = True
        self._t = threading.Thread(target=self._collect)
        self._t.setDaemon(True)
        self._t.start()

    def _collect(self):


        while self._flag:
            now = time.time()
            keys = self.__map.keys()
            
            for key in list(self):
                val = self.__map[key]
                diff = now - val
                if diff>self._ttl:
                   
                    del self[key]
                    
                    del self.__map[key]

    def _set(self, key):
        self.__map[key] = time.time()
        
    def __setitem__(self, key, value):
       
        self._set(key)
      
        return dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        
        val = dict.__getitem__(self, key)
        return val  

    def __del__(self):
        self._flag = False
        self._t.join()
