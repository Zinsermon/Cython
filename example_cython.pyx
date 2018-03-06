cpdef int Function( int x):
    cdef int j=0
    cdef int i=0
    for i in range(x):
        j+=1
    return j
