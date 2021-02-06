import timeit

import gc
import tracemalloc

from pympler import muppy

class IntHolder:

    def __init__(self, the_int):
        self._the_int = the_int

class Holder:

    def __init__(self):
        self._my_dict = {}
        for i in range(10000000):
            self._my_dict[i] = IntHolder(i)

    @property
    def my_dict(self):
        return self._my_dict

def get_holder():
    return Holder()

# tracemalloc.start()

start = timeit.default_timer()

holder = get_holder()

muppy.print_summary()

end = timeit.default_timer()

print('Setup time: {0} seconds'.format(end - start))

start = timeit.default_timer()

gc.collect()

all_objects = gc.get_objects()

end = timeit.default_timer()

print('Object collection time: {0} seconds'.format(end - start))

start = timeit.default_timer()

for o in all_objects:
    gc.get_referents(o)
    # tracemalloc.get_object_traceback(o)

end = timeit.default_timer()

print('Referent collection time: {0} seconds'.format(end - start))

print('{0} objects found'.format(len(all_objects)))
print('Dict size: {0}'.format(len(holder.my_dict)))
print('Bytes used by tracemalloc: {0}'.format(tracemalloc.get_tracemalloc_memory()))

# tracemalloc.stop()

input('Press any key to terminate')