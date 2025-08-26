import numpy


class Solution(object):
    def twosum_wrong(self,nums,target):
        # 排序之后破坏了原本的位置次序
        nums.sort()
        i=0
        j=len(nums)-1
        while i<=j:
            print(j)
            if nums[j]>=target:
                j-=1
            else:
                if nums[j]+nums[i]<target:
                    i+=1
                elif nums[i]+nums[j]==target:
                    print(i,j)
                    print(nums[i])
                    break
                else:
                    j-=1
        return i,j

    def twosum(self,nums,target):
        num_dict={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in num_dict:
                return num_dict[complement],i
            num_dict[num]=i
        return None

    def groupAnagrams_wrong(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        def IsEqual(a, b):
            hash_a = {}
            for i, ch in enumerate(a):
                if ch in hash_a:
                    hash_a[ch] += 1
                else:
                    hash_a[ch] = 1
            for i, ch in enumerate(b):
                if ch in hash_a:
                    hash_a[ch] -= 1
                else:
                    return False

            for key in hash_a:
                if hash_a[key] != 0:
                    return False

            return True
        strss=[]
        ones=numpy.ones_like(strs)
        for i,str in enumerate(strs):
            str_hash=[]

            for i in range(len(str)):
                if ones[i]!=0:
                    str_hash.append(strs[i])
                for j in range(i+1,len(str)):
                    if IsEqual(strs[i],strs[j]):
                        str_hash.append(strs[j])
                        ones[j]=0
                strss.append(str_hash)
        return strss

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        all_str={}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in all_str:
                all_str[sorted_s].append(s)
            else:
                all_str[sorted_s]=[s]

        r=all_str.values()
        return list(all_str.values())

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_res = 1
        res = 1
        all_dict = {}
        nums = sorted(nums)
        # for num in nums:
        #     all_dict[num]=1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                res += 1
                if res > max_res:
                    max_res = res
            elif nums[i] == nums[i - 1]:
                res = res
            else:
                res = 1
        if len(nums) == 0:
            max_res = 0

        return max_res

    def longestConsecutive_revise(self,nums):
        if len(nums)==0:
            return 0
        max_len=1
        num_set=set(nums)
        for num in num_set:
            if num-1 not in num_set:
                current_num=num
                current_len=1
                while current_num+1 in num_set:
                    current_num+=1
                    current_len+=1
                max_len=max(max_len,current_len)

        return max_len

    def moveZero_revise(self,nums):
        j=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        for k in range(j,n):
            nums[k]=0
        return nums
    def maxArea_revise(self,height):
        n=len(height)
        i,j=0,n-1
        max_area=0
        while i<j:
            h=min(height[i],height[j])
            w=j-i
            area=h*w
            max_area=max(max_area,area)
            if height[i]<height[j]:
                k=i+1
                while height[k]<=height[i]:
                    k+=1
                i=k
            else:
                k=j-1
                while height[k]<=height[j]:
                    k-=1
                j=k
        return max_area
    def longestConsecutive_byhash(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums_set=set(nums)

        max_len=1

        for num in nums_set:
            if num-1 not in nums_set:
                current_len=1
                current_num=num
                while current_num+1 in nums_set:
                    current_len+=1
                    current_num+=1

                max_len=max(max_len,current_len)

        return max_len

    def moveZeroesbyBubble(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]!=0:
                j=i
                while j>0 and nums[j-1]==0:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    j -= 1

    def moveZeroes(self,nums):
        """双指针法，一个指针用来遍历数组，一个用来记录非零元素应该存放的位置"""
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        return nums

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j=0,len(height)-1
        max_area=0
        while i<j:
            h=min(height[i],height[j])
            w=j-i
            area=h*w
            if area>max_area:
                max_area=area
            if height[i]<height[j]:
                k = i
                k += 1

                while height[k+1]<height[i] and k<j:
                    k+=1
                i=k
            else:
                k =j- 1

                while height[k-1]<height[j]:
                    k-=1
                j=k
        return max_area

    def threeSumbyHash(self, nums):
        """
        用哈希需要考虑的边界值太多，不划算
        """
        ans=[]
        hash_list={}
        for num in nums:
            if num in hash_list:
                hash_list[num]+=1
            else:
                hash_list[num]=1

        unique_nums=sorted(hash_list.keys())
        n=len(unique_nums)
        for i in range(n):
            for j in range(i,n):
                key=unique_nums[i]
                key2=unique_nums[j]
                target=0-key-key2
                if target in hash_list:
                    if key2==key==target:
                        if hash_list[key]>=3:
                            ans.append([key,key2,target])
                    elif key2==key:
                        if hash_list[key]>=2 and target>=key:
                            ans.append([key,key2,target])
                    elif target>key2:
                        ans.append([key,key2,target])
        return ans

    def threeSum_revise(self,nums):
        n=len(nums)
        nums=sorted(nums)
        ans=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    k=left+1
                    while nums[k]==nums[left] and k<right:
                        k+=1
                    left=k
                    k=right-1
                    while nums[k]==nums[right] and k>left:
                        k-=1
                    right=k
                else:
                    if sum>0:
                        right-=1
                    else:
                        left+=1
        return ans


    def threeSum(self,nums):
        """用双指针，i遍历数组，每次视为i固定，其他两个指针移动"""
        nums=sorted(nums)
        ans=[]
        n=len(nums)
        for i in range(n):
            if nums[i]>0:
                break
            if i>=0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum==0:
                    ans.append([nums[i],nums[left],nums[right]])

                    k=left+1
                    while nums[k]==nums[left] and k<right:
                        k+=1
                    left=k
                    z=right-1
                    while nums[z]==nums[right] and left<z:
                        z-=1
                    right=z
                else:
                    if sum>0:
                        right-=1
                    else:
                        left+=1
        return ans

    def trapByMyself(self, height):
        """
        仅能通过三分之二的用例，需要考虑的边界情况过于复杂
        """
        n=len(height)
        if n <=2:
            return 0
        sum=0
        i=1
        while i<n-1:

            left=i-1 # i=2 ,l=1, r=3
            right=i+1
            if height[left]>height[i] and height[right]>height[i]:
                k=left
                while k>=0:
                    if height[k]>height[left]:
                        if height[left]==min(height[left],height[right]):
                            left=k
                    k-=1

                z=right
                while z<=n-1:
                    if height[z]>height[right]:
                        if height[right]==min(height[left],height[right]):
                            right=z
                    z+=1
                h=min(height[left],height[right])
                d=right-left-1
                drops=h*d
                for j in range(left+1,right):
                    drops-=height[j]
                sum+=drops
                i=right+1
            else:
                i+=1
                continue

        return sum

    def trap_revise(self,height):
        n=len(height)
        if n<=2:
            return 0
        left=[0]*n
        right=[0]*n
        left[0]=height[0]
        right[n-1]=height[n-1]
        for i in range(1,n):
            left[i]=max(left[i-1],height[i])
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],height[i])

        sum=0
        for i in range(0,n):
            sum+=max(0,min(left[i],right[i])-height[i])
        return sum
    def trap(self, height):
        n=len(height)
        if n<=2:
            return 0

        left=[0]*n
        right=[0]*n
        left[0] =height[0]
        for i in range(1,n):
            left[i] =max(left[i-1],height[i])
        right[n-1]=height[n-1]

        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],height[i])

        sum=0
        for i in range(n):
            h=min(left[i],right[i])-height[i]
            sum+=h
        return sum

    def lengthOfLongestSubstring_revise(self, s):
        n=len(s)
        left,right=0,0
        hash_list={}
        ans=0
        while right<=n:
            if s[right] not in hash_list or hash_list[s[right]]==0:
                ans+=1
                right+=1
                hash_list[s[right]]=1
            else:
                while hash_list[s[right]]!=1:
                    ans-=1
                    hash_list[s[left]]=0
                    left+=1
        return  ans
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_list={}
        i=j=0
        n=len(s)
        hash_list[s[0]]=1
        j+=1
        if n==0:
            return 0
        max_len=1
        sub_len=1
        while i<n and j<n and i<=j:
            if s[j] not in hash_list or hash_list[s[j]]==0:
                sub_len+=1
                max_len=max(max_len,sub_len)
                hash_list[s[j]]=1
                j+=1
            else:
                hash_list[s[j]]+=1
                while s[i]!=s[j]:
                    sub_len-=1
                    hash_list[s[i]]-=1
                    i+=1
                if s[i]==s[j]:
                    hash_list[s[i]]-=1
                    i+=1
                    sub_len-=1
                j+=1
                sub_len=j-i

        return max_len

    def findAnagramsByme_revise(self,s,p):
        """
        超出时间限制
        :param s:
        :param p:
        :return:
        """
        len_s=len(s)
        len_p=len(p)
        hash_p={}
        hash_s={}
        for i in range(len_p):
            if p[i] not in hash_p:
                hash_p[p[i]]=1
            else:
                hash_p[p[i]]+=1
        ans=[]
        i=0
        while i<(len_s-len_p+1):
            hash_p_copy=hash_p.copy()
            match=True
            for j in range(i,i+len_p):
                if s[j] not in hash_p_copy:
                    i=j
                    match=False
                    break
                else:
                    hash_p_copy[s[j]]-=1
                    if hash_p_copy[s[j]]<0:
                        match=False
                        break
            if match:
                ans.append(i)
            i+=1
        return ans

    def findAnagramsByme(self, s, p):
        """
        缺点是时间复杂度太高，优点是简单
        """
        p="".join(sorted(p))
        len_s=len(s)
        len_p=len(p)
        ans=[]
        for i in range(len_s-len_p):
             if i+len_p <=len_s:
                sub_s="".join(sorted(s[i:i+len_p]))
                if sub_s==p:
                    ans.append(i)

        return ans

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_s=len(s)
        len_p=len(p)
        ans=[]
        p_table=[0]*26
        for i in range(len_p):
            p_table[ord(p[i])-ord('a')]+=1
        table=[0]*26
        j=0
        for i in range(len_s-len_p+1):

            while j-i+1<=len_p:
                table[ord(s[j])-ord('a')]+=1
                j+=1
            if table==p_table:
                ans.append(i)
            table[ord(s[i])-ord('a')]-=1
        return ans

    def subarraySum_revise(self,nums,k):
        "只对全是正整数的数组正确，但是数组中存在负数，因此还是要用前缀和的方法"
        n=len(nums)
        left=right=0
        ans=0
        sum=nums[right]
        while right<n and left<=right:
            if sum==k:
                ans+=1

                right+=1
                if right>=n:
                    break
                sum += nums[right]

            else:
                if sum <k:
                    right+=1
                    if right >= n:
                        break
                    sum += nums[right]
                else:
                    sum-=nums[left]
                    left+=1
        return ans

    def subarraySum_revise_correct(self, nums, k):
        prefix_dict={0:1}
        curr_sum=0
        ans=0
        for num in nums:
            curr_sum+=num
            target=curr_sum-k
            if target in prefix_dict:
                ans+=prefix_dict[target]
            if curr_sum not in prefix_dict:
                prefix_dict[curr_sum]=1
            else:
                prefix_dict[curr_sum]+=1
        return ans
    def subarraySumByme(self, nums, k):
        """
        两层循环，时间超时
        """
        ans=0

        n=len(nums)
        for i in range(n):
            win_sum = 0

            for j in range(i+1,n+1):
                win_sum+=nums[j-1]

                if win_sum==k:
                    ans+=1

        return ans

    def subarraySum(self, nums, k):
        """用前缀和加上哈希表"""
        prefix_count={0:1}
        curr_count=0

        ans=0
        for num in nums:
            curr_count+=num

            target=curr_count-k

            if target in prefix_count:
                ans+=prefix_count[target]

            if curr_count in prefix_count:
                prefix_count[curr_count]+=1
            else:
                prefix_count[curr_count]=1
        return ans

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        "超出时间限制"
        # if k==1:
        #     return nums
        # res=[]
        # n=len(nums)
        # left=0
        # right=k-1
        # hash_win={}
        # max_in_win=0
        # for i in range(k):
        #     if nums[i] not in hash_win:
        #         hash_win[nums[i]]=1
        #     else:
        #         hash_win[nums[i]]+=1
        #     max_in_win=max(max_in_win,nums[i])
        # res.append(max_in_win)
        # for i in range(1,n-k+1):
        #     hash_win[nums[left]]-=1
        #     if hash_win[nums[left]]==0:
        #         del hash_win[nums[left]]
        #         max_in_win=max(hash_win.keys())
        #     left+=1
        #     right+=1
        #     if nums[right] in hash_win:
        #         hash_win[nums[right]]+=1
        #     else:
        #         hash_win[nums[right]]=1
        #         max_in_win=max(max_in_win,nums[right])
        #     res.append(max_in_win)
        # return res
        from collections import deque
        q=deque()
        n=len(nums)
        res=[]

        for right in range(n):
            # 维护队列的顺序
            while q and nums[right]>=nums[q[-1]]:
                q.pop()
            q.append(right)

            # 移除旧的元素
            while q[0]<=right-k:
                q.popleft()

            # 队首就是最大值
            if right>=k-1:
                res.append(nums[q[0]])
        return res
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict_t = {}
        valid_t = 0
        for i in t:
            # print(i)
            if i in dict_t:
                dict_t[i] += 1
            else:
                dict_t[i] = 1
                valid_t += 1
        ans = ""
        min_len = len(s) + 1
        left = 0
        right = 0
        n = len(s)
        dict_substr = {}
        len_t = len(t)
        valid = 0
        while right < n and left <= right:
            if s[right] in dict_substr:
                dict_substr[s[right]] += 1
            else:
                dict_substr[s[right]] = 1
            if s[right] in dict_t and dict_substr[s[right]] == dict_t[s[right]]:
                valid += 1
            while valid == valid_t:
                substr = s[left:right + 1]
                sub_len = right + 1 - left
                if sub_len < min_len:
                    ans = substr
                    min_len = sub_len
                dict_substr[s[left]] -= 1
                if s[left] in dict_t and dict_substr[s[left]] < dict_t[s[left]]:
                    valid -= 1
                left += 1
                while left <= right and s[left] not in dict_t:
                    dict_substr[s[left]] -= 1
                    left += 1

            right += 1
        return ans


# nums=[3,2,4]
# target=6
# s=Solution()
# r=s.twosum(nums,target)
# print(r)
#
# strs=["eat","tea","tan","ate","nat","bat"]
# r=s.groupAnagrams(strs)
# print(s)
#
# nums=[100,4,200,1,3,2]
# r=s.longestConsecutive(nums)
# print(s)
#
# nums=[0,1,0,3,12]
# r=s.moveZeroes(nums)
# print(r)
#
# height=[1,8,6,2,5,4,8,3,7]
# r=s.maxArea(height)
# print(r)
#
# nums=[2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
# r=s.threeSum(nums)
# print(r)
#
# nums=[0,1,0,2,1,0,1,3,2,1,2,1]
# r=s.trap(nums)
# print(r)
#
# str="pwwkew"
# r=s.lengthOfLongestSubstring(str)
# print(r)
#
# str="abab"
# p="ab"
#
# r=s.findAnagrams(str,p)
# print(r)
#
# nums=[1,1,1]
# k=2
#
# r=s.subarraySum(nums,k)
# print(r)
# nums=[0,-1]
# r=s.longestConsecutive_revise(nums)
# print(r)
s=Solution()
nums=[0]
r=s.moveZero_revise(nums)
print(r)