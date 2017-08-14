# Insertion Sort
# Complexity: O(nlog(n))
# Pseudo-code: CLRS
# !!! NOTE: In python array start at index [0]

import random


def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence A[1..j-1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
# l = [12, -3, 33, 0]
# insertion_sort(l)
# print(l)
def gen_array(size):
    arr = []
    for i in range(0, size):
        x = random.randint(-100, 100)
        arr.append(x)
    return arr

def check(A):
    for i in range(1, len(A)):
        if A[i] < A[i - 1]:
            print("!", A[i],">", A[i - 1], "at: ", i)
            return "FAILED!"
    return "PASSED!"

""""""
a_list = gen_array(5)
insertionSort(a_list)
print(a_list)
print(check(a_list))
exit(0)


#
# def insertion_sort(A):
#     for j in range(1, len(A)):
#         key = A[j]
#         i = j
#         while i > 0 and A[i - 1] > key:
#             A[i] = A[i - 1]
#             i = i - 1
#         A[i] = key
#
#
# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# insertion(a_list)
# print(a_list)
