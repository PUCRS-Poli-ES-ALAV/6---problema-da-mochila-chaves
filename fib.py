import time
import sys

sys.setrecursionlimit(20000)

def fibo_rec(n, counter=None):
    if counter is None:
        counter = {'calls': 0}
    counter['calls'] += 1
    
    if n <= 1:
        return n, counter
    else:
        a, counter = fibo_rec(n - 1, counter)
        b, counter = fibo_rec(n - 2, counter)
        return a + b, counter

def fibo(n):
    iterations = 0
    f = [0] * (n + 1)
    f[0] = 0
    if n > 0:
        f[1] = 1
        for i in range(2, n + 1):
            iterations += 1
            f[i] = f[i-1] + f[i-2]
    return f[n], iterations

def memoized_fibo(n):
    counter = {'calls': 0}
    f = [-1] * (n + 1)
    return lookup_fibo(f, n, counter), counter['calls']

def lookup_fibo(f, n, counter):
    counter['calls'] += 1
    
    if f[n] >= 0:
        return f[n]
    if n <= 1:
        f[n] = n
    else:
        f[n] = lookup_fibo(f, n - 1, counter) + lookup_fibo(f, n - 2, counter)
    return f[n]

def benchmark(func, n, label):
    start_time = time.time()
    
    if func.__name__ == 'fibo_rec':
        result, count = func(n)
    else:
        result, count = func(n)
        
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"{label} para n={n}: tempo={execution_time:.6f} segundos, {count} {'chamadas' if func.__name__ != 'fibo' else 'iterações'}")
    return execution_time

def run_tests():
    print("\n=== Testes para n = 4, 8, 16, 32 ===")
    for n in [4, 8, 16, 32]:
        print(f"\nTestando para n = {n}")
        benchmark(fibo_rec, n, "Fibonacci recursivo")
        benchmark(fibo, n, "Fibonacci iterativo")
        benchmark(memoized_fibo, n, "Fibonacci com memoização")
    
    print("\n=== Testes adicionais para n = 128, 1000, 10000 ===")
    for n in [128, 1000, 10000]:
        print(f"\nTestando para n = {n}")
        if n <= 128: 
            benchmark(fibo_rec, n, "Fibonacci recursivo")
            benchmark(fibo, n, "Fibonacci iterativo")
            benchmark(memoized_fibo, n, "Fibonacci com memoização")
        else:
            print(f"Fibonacci recursivo para n={n}: não executado (muito lento)")
            benchmark(fibo, n, "Fibonacci iterativo")
            benchmark(memoized_fibo, n, "Fibonacci com memoização")

if __name__ == "__main__":
    run_tests()