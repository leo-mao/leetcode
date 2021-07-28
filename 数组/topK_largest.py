class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
        ## 这道题我用冒泡排序，把前kk个大的数字排序oo排出来即可，oo（n*k），当然这种方法显然会超时，所以我们不用
        # for i in range(k):
        #     for j in range(len(nums)-i-1):
        #         if nums[j] > nums[j+1]:
        #             tmp = nums[j]
        #             nums[j] = nums[j+1]
        #             nums[j+1] = tmp
        # print(nums[len(nums)-k])
        # return nums[len(nums)-k]
        ## 用快排来求TopK
        ## 按照算法导论的写法来写快排，与75题的位置交换有异曲同工之妙
    #     return self.qsort(nums, 0, len(nums)-1, len(nums)-k)

    # def qsort(self, nums, l, r, idx):
    #     q = self.partition(nums, l, r)
    #     # print(f"q: {q} idx: {idx}")
    #     if q == idx:
    #         return nums[q]
    #     elif q > idx: # 此时只排k位于左侧，右半边就可以放弃了
    #         # idx始终是绝对坐标，故不变
    #          return self.qsort(nums, l, q-1, idx)
    #     elif q < idx:
    #         return self.qsort(nums, q+1, r, idx)  

    # def partition(self, nums, l, r):
    #     nums[r],  nums[(l+r)//2] = nums[(l+r)//2], nums[r] # 随机化pivot
    #     x = nums[r]
    #     # print(f"l:{l}, r:{r}, x:{x}")
    #     i = l - 1
    #     for j in range(l, r):# r 是pivot
    #         if nums[j] <= x:
    #             i += 1
    #             nums[i], nums[j] = nums[j], nums[i]
    #     # 当前i所在位置是最后一个小于等于pivot x的,那么i+1便是大于x=nums[r]的，所以我们只要交换i+1与r的位置，那么此前num[r]上的数值便来到了正确的位置
    #     nums[i+1], nums[r] = nums[r], nums[i+1]
    #     return i+1
    def findKthLargest(self, nums, k) -> int:
        self.build_max_heap(nums)
        print(nums)
        sorted = self.heap_sort(nums)

        print(sorted)
        return sorted[k-1]

    def max_heapify(self, nums, i):
        l = ((i+1) << 1) - 1
        r = (i+1) << 1
        largest = i
        # print(f'l:{l} r:{r}')
        if l < len(nums) and nums[l] > nums[i]:
            largest = l
        if r < len(nums) and nums[r] > nums[largest]:
            largest = r
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.max_heapify(nums, largest)                
        # print(f'l:{l} r:{r} largest:{largest}')

    def build_max_heap(self, nums):
        # print(f"in build max, len(nums) {len(nums)//2-1}")
        for i in range(len(nums)//2 - 1, -1, -1):
            self.max_heapify(nums, i)
    
    def heap_sort(self, nums):
        sorted = []
        for i in range(len(nums)-1, 0, -1):
            sorted.append(nums[0])
            nums[0] = nums[i]
            del nums[i]
            self.max_heapify(nums, 0)
        sorted.append(nums[0])
        return sorted


def main():
    s = Solution()
    # nums = [3,2,3,1,2,4,5,5,6]
    nums = [0]
    s.findKthLargest(nums, 1)

if __name__ == '__main__':
    main()