import sys
import hasher



def main():
    argc = len(sys.argv)
    hasher_object = hasher.Hasher()
    options = ''
    available_options = set('sm')
    guaranteed_algorithms = hasher.Hasher.algorithms_guarateed()
    
    inopt = False
    method = False

    try:
        if sys.argv[1].startswith('-'):
            inopt = True   
            options = set(each for each in sys.argv[1].strip('-'))
            options = options.intersection(available_options)

        if 'm' in options:
            method = True
            algorithm = sys.argv[2].strip('\'')
            hasher_object.set_algorithm(algorithm)
            
            if algorithm not in guaranteed_algorithms:
                print('Invalid/Not Available Algorithm. Defaulting to {}.'.format(hasher_object.algorithm))
            else:
                print('Using {}'.format(algorithm))

        string_or_file = True if 's' in options else False

        number_inputs = compute_number_inputs(inopt,method,argc)

        if number_inputs == 2:
            print("Two inputs detected, performing hash comparison")

            if string_or_file:
                result = hasher_object.compute_hash_string(sys.argv[argc-2]) == sys.argv[argc-1]
                return 'OK!' if result else 'NOT OK!'
            
            result = hasher_object.compute_hash_file(sys.argv[argc-2]) == sys.argv[argc-1]
            return "OK! Hashes match" if result else 'FAIL! Hash mismatch'

        elif number_inputs == 1:
            
            print("Single input detected, calculating hash")

            if string_or_file:
                return hasher_object.compute_hash_string(sys.argv[argc-1])
            
            return hasher_object.compute_hash_file(sys.argv[argc-1])
        else:
            print("Too many or not enough inputs. Exiting")
            return
        
    except FileNotFoundError:
        return "Cannot find the specified file: {}.".format(sys.argv[argc-1])
    except IndexError:
        return "TODO: HELP"


def compute_number_inputs(inopt,method,argc):
    if inopt and method and argc == 5 or \
             inopt and not method and argc == 4 or \
             not inopt and not method and argc == 3:
        return 2
    elif inopt and method and argc == 4 \
             or inopt and not method and argc == 3\
             or not inopt and not method and argc == 2:
        return 1
    else:
        return



if __name__ == '__main__':
    sys.exit(main())