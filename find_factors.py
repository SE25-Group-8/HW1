def find_factors(x):
    arr = []

    for i in range(1, x + 1):
        if ( x % i ) == 0:
            arr.append(i)
            
    return arr

if __name__=="__main__":
    print(find_factors(10))

