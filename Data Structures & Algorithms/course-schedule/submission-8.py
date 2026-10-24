class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        initDict = { i:[] for i in range(numCourses)}

        for v,k in prerequisites:
            initDict[k].append(v)

        def dfs(node, visited):
            
            visited.add(node)
            neighbors = initDict[node]

            for neigh in neighbors:
                print(visited)
                if (neigh in visited):
                    return False
    
                if (dfs(neigh, visited)):
                    val = initDict[node]
                    val.remove(neigh)
                else:
                    return False
                    
            visited.remove(node)
            return True






            

            



        for i in range(numCourses):
            visited = set()
            if (not dfs(i, visited)):
                return False

        return True

