"""
Peak Finding problems
Complexity: O(log(n))
"""

class OneDPeakFinder(object):
    def __init__(self, arr):
        self.arr = arr

    def exhausted_peak_finding(self):
        n = len(self.arr)
        # check first and last elements is a peaks?
        if n >= 2:
            if self.arr[0] >= self.arr[1]:
                return 0
            if self.arr[n - 1] >= self.arr[n - 2]:
                return n - 1
        for i in range(0, n):
            if self.arr[i - 1] <= self.arr[i] <= self.arr[i + 1]:
                return i

    def peak_finder(self):
        n = len(self.arr)
        low, high = 0, n // 2
        mid = (low + high) // 2
        # peak = -1
        steps = 0
        print('steps = ', steps, ': low = ', low, 'mid = ', mid, 'high = ', high)
        while high > low:
            steps += 1
            if self.arr[mid] < self.arr[mid - 1]:
                high = mid - 1
            elif self.arr[mid] < self.arr[mid + 1]:
                low = mid + 1
            else:
                # peak = mid
                break
            mid = (low + high) // 2
            print('steps = ', steps, ': low = ', low, 'mid = ', mid, 'high = ', high)
        return mid


# arr = [3, 4, 0, -9, 122]
# arr = [1, 12, -33, 0, 29]
# peak_finder = OneDPeakFinder(arr)
# peak_id = peak_finder.peak_finder()
# print('id = ', peak_id, ' - peak = ', peak_finder.arr[peak_id])
# print('peak = ', arr[peak_finder.exhausted_peak_finding()])


class TwoDPeakFinding(OneDPeakFinder):
    def __init__(self):
        pass

    def GreedyAscent(self):
        pass
