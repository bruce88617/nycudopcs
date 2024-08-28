"""
Example 4: Combine with class
"""

from jobs_thread import multithread1

arr1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

test1 = multithread1(arr1)
test1.run()
print(test1.get_data())

