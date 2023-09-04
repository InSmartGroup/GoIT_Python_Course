import numpy as np
import time

# print(np.__version__)  # numpy version

# ar = np.array(1)
# print(ar, type(ar), 'Dimensions:', ar.ndim, 'it\'s scalar')  # 0 dimension, it's a scalar
#
# ar = np.array(range(5))
# print(ar, type(ar), 'Dimensions:', ar.ndim, 'it\'s a vector')  # 1 dimension, it's a vector
#
# ar = np.array([range(5)])
# print(ar, type(ar), 'Dimensions:', ar.ndim, 'it\'s a matrix')  # 2 dimensions, it's a matrix
#
# ar = np.array([[range(5)]])
# print(ar, type(ar), 'Dimensions:', ar.ndim, 'it\'s a 3d plane')  # 3 dimensions, it's a 3d plane
#
# ar = np.array([[[[range(5)]]]])
# print(ar, type(ar), 'Dimensions:', ar.ndim, 'it\'s a hyper-plane')  # 4+ dimension, it's a hyper-plane

# # let's compare numpy and lists productivity
# start = time.time()
# py_list = [i for i in range(100000000)]
# end = time.time()
# print(end - start)  # it takes Python 7.896150350570679 seconds
#
# start = time.time()
# np_array = np.arange(0, 100000000)  # it takes numpy 0.17189574241638184 seconds
# end = time.time()
# print(end - start)
# print(np_array)
