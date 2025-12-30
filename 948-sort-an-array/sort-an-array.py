class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr: List[int]) -> List[int]:
            if len(arr) > 1:
                mid = len(arr) // 2
                lh = arr[:mid]
                rh = arr[mid:]
                merge_sort(lh)
                merge_sort(rh)
                i = j = k = 0
                while i < len(lh) and j < len(rh):
                    if lh[i] < rh[j]:
                        arr[k] = lh[i]
                        i += 1
                    else:
                        arr[k] = rh[j]
                        j += 1
                    k += 1
                while i < len(lh):
                    arr[k] = lh[i]
                    i += 1
                    k += 1
                while j < len(rh):
                    arr[k] = rh[j]
                    j += 1
                    k += 1
            return arr
        res = merge_sort(nums)
        return res