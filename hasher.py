
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

    

def compute_string_md5(s):
    m = hashlib.md5(s.encode('utf-8'))
    return m.hexdigest()

def compute_string_sha256(s):
    m = hashlib.sha256(s.encode('utf-8'))
    return m.hexdigest()

def compute_file_md5(path, sizbuf=4096):
    m = hashlib.md5()

    with open(path,'rb') as fd:
        breader = io.BufferedReader(fd)
        while(breader.peek() != b''):
            m.update(breader.read(sizbuf))

    return m.hexdigest()

def compute_file_sha256(path, sizbuf=4096):
    m = hashlib.sha256()
 
    with open(path,'rb') as fd:
        breader = io.BufferedReader(fd)
        while(breader.peek() != b''):
            m.update(breader.read(sizbuf))

    
    return m.hexdigest()

def compare_sha256(file, computed_hash):
    pass
    