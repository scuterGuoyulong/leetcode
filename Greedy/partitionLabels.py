class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        """错误的思路，但是也能通过109/118的用例。但是错误在每次判断不是一个子串的时候是用子串后面的第一个字符来判断。但是可以子串中的字符会出现在后面第二个
        导致了出错。正确的做法应该是每次把子串内的字符的最后位置都找出来更新最长长度"""
        n = len(s)
        dict = {}
        first_dict = {}
        for i in range(n):
            if s[i] not in dict:
                dict[s[i]] = [i]
                first_dict[s[i]] = i
            else:
                dict[s[i]].append(i)

        nums = dict[s[0]]
        i = nums[-1]
        end_nums = nums[-1]
        print(i)
        start_num = nums[0]

        ans = []
        while i < n:
            i += 1
            if i == n:
                ans.append(end_nums - nums[0] + 1)
                break

            if first_dict[s[i]] <= end_nums:
                i = dict[s[i]][-1]
                end_nums = max(i, end_nums)
            else:
                ans.append(i - nums[0])
                nums = dict[s[i]]
                end_nums = nums[-1]
                print(end_nums)
        return ans

"""贪心，记录每个碎片最小的长度"""
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s)
        last_pos = {}
        for i,c in enumerate(s):
            last_pos[c]=i

        res=[]
        start=0
        current_end=0

        for i,c in enumerate(s):
            current_end=max(current_end,last_pos[i])

            if i==current_end:
                res.append(current_end-start)
                start=i+1

        return res
