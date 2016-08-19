import sys
import hasher
from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument('inputs', metavar='inputs', nargs='+')
parser.add_argument('-s','--string',action = 'store_true', help = 'String inputs')
parser.add_argument('-a','--alg', help = 'Select hashing algorithm. Defaults to SHA-256')

def main():
    
    parse = parser.parse_args()
    hasher_object = hasher.Hasher(parse.alg)

    try:

        if len(parse.inputs) == 2:
            print("Two inputs detected, performing hash comparison:")

            if parse.string:
                result = hasher_object.compute_hash_string(parse.inputs[0]) == parse.inputs[1]
                return 'OK!' if result else 'NOT OK!'
            
            result = hasher_object.compute_hash_file(parse.inputs[0]) == parse.inputs[1]
            return "OK! Hashes match" if result else 'FAIL! Hash mismatch'

        elif len(parse.inputs) == 1:
            print("Single input detected, calculating hash")

            if parse.string:
                return hasher_object.compute_hash_string(parse.inputs[0])
            
            return hasher_object.compute_hash_file(parse.inputs[0])
        else:
            print("Too many inputs. Exiting")
            return
        
    except FileNotFoundError:
        return "Cannot find the specified file: {}.".format(parse.inputs[0])

if __name__ == '__main__':
    sys.exit(main())