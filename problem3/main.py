def prime_number(nu):
    if nu == 1 or nu== 0 :
        return False
    elif nu > 1:
        for i in range (2, nu ) :
            if nu % i == 0 :
                return "Not Prime"
        else :
            return "Prime"

if __name__ == '__main__':
    print(prime_number(11)) # "Prime"
    print(prime_number(13)) # "Prime"
    print(prime_number(17)) # "Prime"
    print(prime_number(20)) # "Not Prime"
    print(prime_number(35)) # "Not Prime"