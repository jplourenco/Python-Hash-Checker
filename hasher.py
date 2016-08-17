
import hashlib
import io


class Hasher(object):

    def __init__(self, algorithm=None):
        self.set_algorithm(algorithm)

    def set_algorithm(self, algorithm=None):
        if type(algorithm) == str and algorithm in hashlib.algorithms_guaranteed:
            self.hashfun = hashlib.new(algorithm)
        else: 
            self.hashfun = hashlib.sha256() #defaults to sha256
        
        self.algorithm = self.hashfun.name

    def update(self,data):
        self.hashfun.update(data)

    def hexdigest(self):
        return self.hashfun.hexdigest()

    def compute_hash_string(self,data):
        
        self.update(data.encode('utf-8'))
        return self.hexdigest()
    
    def compute_hash_file(self, path, sizbuf=4096):

        with open(path,'rb') as fd:
            breader = io.BufferedReader(fd)
            while(breader.peek() != b''):
                self.update(breader.read(sizbuf))
        return self.hexdigest()
    
    
    @staticmethod
    def algorithms_guarateed():
        return hashlib.algorithms_guaranteed

    

    