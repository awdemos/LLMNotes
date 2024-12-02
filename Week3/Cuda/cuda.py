import numpy as np
from timeit import default_timer as timer

def MultiplyMyVectors(a, b, c):
    return a * b * c

def main():
    N = 64000000  # size per declared array

    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.ones(N, dtype=np.float32)

    start = timer()  # start my timer
    result = MultiplyMyVectors(A, B, C)
    vectormultiply_time = timer() - start

    print("C[:6] = " + str(result[:6]))
    print("C[-6:] = " + str(result[-6:]))
    print("This multiplication took %f seconds" % vectormultiply_time)

if __name__ == "__main__":
    main()
