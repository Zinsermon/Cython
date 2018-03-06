import example_cython
import Example
import timeit

#### ==================== proper Function name ,    setup is equal all import from Function and number is how many iteration ====###
cy = timeit.timeit('''example_cython.Function(50000)''',setup='import example_cython',number=100)
py = timeit.timeit('''Example.Function(50000)''',setup='import Example', number=100)

print(cy, py)
print('Cython is {}x faster'.format(py/cy))
