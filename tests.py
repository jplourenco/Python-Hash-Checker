import unittest
import hasher
import hashlib

class test_hashMD5(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(hasher.compute_string_md5(''), 'd41d8cd98f00b204e9800998ecf8427e')

    def test_lazy_dogs(self):
        self.assertEqual(hasher.compute_string_md5('The quick brown fox jumps over the lazy dog'), 
            '9e107d9d372bb6826bd81d3542a419d6')

        self.assertEqual(hasher.compute_string_md5('The quick brown fox jumps over the lazy dog.'),
            'e4d909c290d0fb1ca068ffaddf22cbd0')
    
    def test_anacondasha256(self):

        self.assertEqual(hasher.compute_file_sha256('C:\\Users\\Joao\\Downloads\\Anaconda3-4.1.1-Windows-x86_64.exe'),
            'b4889513dc574f9d6f96db089315d69d293f8b17635da4d2e6eee118dc105f38')
    
    def test_hasher_class_default(self):
        
        #Invalid, non-string  input should default to sha256
        h1 = hasher.Hasher()
        h2 = hasher.Hasher("3232")
        h3 = hasher.Hasher([])

        self.assertEqual(h1.algorithm,'sha256')
        self.assertEqual(h2.algorithm,'sha256')
        self.assertEqual(h3.algorithm,'sha256')
    
    def test_hasher_class_guarateed_algorithms(self):

        self.assertEqual(hasher.Hasher.algorithms_guarateed(), hashlib.algorithms_guaranteed)
    
    def test_hasher_class_every_algorithm(self):
        h1 = hasher.Hasher()
        hasher_list = []
        for each in h1.algorithms_guarateed():
            hasher_list.append(hasher.Hasher(each))
        
        self.assertEqual(list(map(lambda x: x.algorithm, hasher_list)),list(hashlib.algorithms_guaranteed))
    
    def test_hasher_string(self):

        h1 = hasher.Hasher('md5')
        self.assertEqual(h1.compute_hash_string(''),'d41d8cd98f00b204e9800998ecf8427e')
        
    def test_hasher_file(self):

        h1 = hasher.Hasher()
        self.assertEqual(h1.compute_hash_file('C:\\Users\\Joao\\Downloads\\Anaconda3-4.1.1-Windows-x86_64.exe'),
        'b4889513dc574f9d6f96db089315d69d293f8b17635da4d2e6eee118dc105f38')

if __name__ == '__main__':
    unittest.main()