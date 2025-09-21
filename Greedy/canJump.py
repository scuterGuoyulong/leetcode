class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        "超时的暴力算法"
        # n=len(nums)
        # if n==1:
        #     return True
        # cans=[False]*n
        # cans[0] = True
        #
        # for i in range(n-1):
        #     if cans[i]==True:
        #         for j in range(nums[i]+1):
        #             print(j)
        #             if i+j>=n:
        #                 break
        #             cans[i+j]=True
        # return cans[n-1]
        "On^2级别的BFS算法，居然没有超时"
        # # BFS
        # n = len(nums)
        # if n == 1:
        #     return True  # 起点即终点
        #
        # from collections import deque
        # queue = deque()
        # visited = [False] * n  # 标记已访问的节点，避免重复处理
        #
        # # 初始化：起点入队
        # queue.append(0)
        # visited[0] = True
        #
        # while queue:
        #     i = queue.popleft()  # 取出当前位置
        #     max_reach = i + nums[i]  # 当前位置能跳到的最远下标
        #
        #     # 若当前位置的最大可达范围已覆盖终点，直接返回True
        #     if max_reach >= n - 1:
        #         return True
        #
        #     # 将当前位置能到达的所有未访问节点入队
        #     for j in range(i + 1, max_reach + 1):
        #         if j < n and not visited[j]:
        #             visited[j] = True
        #             queue.append(j)
        #
        # # 队列为空仍未到达终点，返回False
        # return False
        "贪心算法，遍历数组，每次维护能到达的最远距离"
        n=len(nums)

        max_reach = nums[0]
        for i in range(1,n):
            if i>max_reach:
                return False

            max_reach=max(max_reach,i+nums[i])
            if max_reach>=n-1:
                return True
        return True

