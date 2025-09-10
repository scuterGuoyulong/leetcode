class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        "都是错误的思路"
        # min_egde = float('inf')
        # max_edge=0
        # for interval in intervals:
        #     for num in interval:
        #         max_edge =max(max_edge,num)
        #         min_egde = min(min_egde, num)
        # len = max_edge -min_egde+1
        # nums=len*[0]
        # for interval in intervals:
        #     for i in range(interval[1]-intervals[0]):
        #         nums[interval[0]+i]=1
        # ans=[]
        # for i in range(len):
        #     if nums[i]==1:
        #         if i-1<0 or nums[i-1]==0:
        #             interval=[nums[i],nums[i]]
        #         if i+1>len-1 or nums[i+1]==0:
        #             interval[1]=nums[i]
        #             ans.append(interval)
        # return ans

        # dict={}
        # for interval in intervals:
        #     if interval[0] not in dict:
        #         dict[interval[0]]=-1
        #     else:
        #         if dict[interval[0]] == 1:
        #             dict[interval[0]] == 0
        #     if interval[1] not in dict:
        #         dict[interval[1]] = 1
        #     else:
        #         if dict[interval[1]] == -1:
        #             dict[interval[1]] == 0
        # nums=[]
        # for interval in intervals:
        #     if dict[interval[0]] !=0:
        #         nums.append(interval[0])
        #     if dict[interval[1]] !=0:
        #         nums.append(interval[1])
        # nums.sort()
        # ans=[]
        #
        # interval = []
        # count=0
        # for num in nums:
        #     count+=1
        #     interval.append(num)
        #     if count/2==0:
        #         ans.append(interval)
        #         interval=[]
        # return ans
        if not  intervals:
            return []
        intervals.sort(key= lambda x: x[0])
        merged=[intervals[1]]
        for current in intervals[1:]:
            last = merged[-1]
            if current[0]<=last[1]:
                merged[-1]=[last[0],max(last[1],current[1])]
            else:
                merged.append(current)
        return merged
