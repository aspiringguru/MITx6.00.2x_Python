#
def fastFib(x, memo):
    assert type(x) == int and x >= 0 and type(memo) == dict
    if x == 0 or x == 1:
        return 1
    if x in memo:
        return memo[x]
    result = fastFib(x-1, memo) + fastFib(x-2, memo)
    memo[x] = result
    return result

def testFastFib(n):
    assert type(n) == int and n >=  0
    for i in range(n):
        print ('fib of', i, '=', fastFib(i, {}))

def fib(x):
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def testFib(n):
    assert type(n) == int and n >=  0
    for i in range(n):
        print ('fib of', i, '=', fib(i)) 


from timeit import default_timer as timer
# timer added to show speed increase
start = timer()
testFib(5)
end = timer()
testFib5 = end - start
start = timer()
testFib(32)
end = timer()
testFib32 = end - start
start = timer()
testFastFib(32)
end = timer()
testFastFib32 = end - start

print "testFib5=", testFib5
print "testFib32=", testFib32
print "testFastFib32=", testFastFib32

