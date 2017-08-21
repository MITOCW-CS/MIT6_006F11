"""
    Insertion sort
    Complexity: O(n^2)
"""


def insertion_sort(L):
    for j in range(1, len(L)):
        key = L[j]
        i = j - 1
        while i >= 0 and L[i] > key:
            L[i + 1] = L[i]
            i -= 1
        L[i + 1] = key


mList = [102, 0, -33, 0, 321, -85]
insertion_sort(mList)

for i in range(1, len(mList)):
    assert mList[i] >= mList[i - 1]

print(mList)

