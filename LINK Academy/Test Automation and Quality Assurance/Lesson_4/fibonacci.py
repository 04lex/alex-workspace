import time

# # Creati un program care sa calculeze elementul cu numarul n din sirul lui Fibonacci

# fibonacci(0) = 1 
# fibonacci(1) = 1 
# fibonacci(2) = 2 
# fibonacci(3) = 3 
# fibonacci(4) = 5 
# fibonacci(5) = 8 
# fibonacci(6) = 13 
# fibonacci(7) = 21

### DECORATOR  (vede printul si intoarce rezultatul)

def timeit(func):
    def new_func(n):
        start_fib_v1 = time.time()
        rezultat = func(n)
        stop_fib_v1 = time.time()
        print("Functia a rulat in", (stop_fib_v1 - start_fib_v1) * 1000 )
        return rezultat
    return new_func



### DEZVOLTARE / PROGRAMARE

@timeit
def fibonacci_v1(n):
    print(f"Calculeaza f({n}) = f({n-1}) + f({n-2})")
   
    # # 2
    if n < 0:
        raise ValueError("N nu poate fi negativ.")
    elif n in (0, 1):
        return 1
    else:
        return fibonacci_v1(n - 1) + fibonacci_v1(n - 2)
    

@timeit
def fibonacci_v2(n):
    values = [1, 1]

    if n < 0:
        raise ValueError("N nu poate fi negativ.")
    elif n < len(values):
        return values[n]
    else:
        for _ in range(2, n + 1):
            values.append(values[-1] + values[-2])
        return values[n]
    

if __name__ == "__main__":
    fibonacci_v1(20)

    print( )

    fibonacci_v2(20)    


    # print(fibonacci_v1(20))

