from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.times = times
        self.result = [None] * (n+1)
        self.visited = [False] * (n+1)
        self.dict_time = {}

        self.__create_dict_time(n)
        self.__visit_node(k, 0)

        max_val = 0
        for i in range(1, len(self.result)):
            if self.result[i] is None:
                return -1
            elif self.result[i] > max_val:
                max_val = self.result[i]
        return max_val

    def __visit_node(self, cur, time_take):
        self.visited[cur] = True
        self.__save_result(cur, time_take)

        u = cur
        for v,w in self.dict_time[u]:
            if self.visited[v] == False:
                self.__visit_node(v, time_take + w)
        self.visited[cur] =False
        

    def __save_result(self, k, time):
        if self.result[k] == None or self.result[k] > time:
            self.result[k] = time
        return self.result[k]

    def __create_dict_time(self, n):
        for i in range(n+1):
            self.dict_time[i] = []
        for u,v,w in self.times:
            self.dict_time[u].append([v, w])

Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,2]], n = 3, k = 1)
# Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
# Solution().networkDelayTime(times = [[1,2,1],[2,1,3]], n = 2, k = 2)
