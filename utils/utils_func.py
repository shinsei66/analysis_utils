import sys


def is_prime(num:int) -> bool:
    '''
    >>> is_prime(1)
    False
    >>> is_prime(3)
    True
    Args:
    num : Any integers
    Return:
    Judge result that whether the num is a prime number
    '''
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
  
    return True


def main():
    name = sys.argv[1]
    print('Hello World, I\'m {}!'.format(name))

if __name__ == '__main__':
    main()
