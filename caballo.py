import time
from dataStructs.graphs import adjacentListGraph
import sys
sys.setrecursionlimit(10000)

import math

 
class BoardGraph(adjacentListGraph): 
    def __init__(self,vertices):
        super().__init__(vertices)
        self._visited = [False for i in range(len(self._vertices))]
        self._n = int(math.sqrt(len(self._vertices)))
    def computeHorseAdjacents(self,v:int):
        self.addEdge(v,v+self._n-1)
        self.addEdge(v,v+self._n-2)
        self.addEdge(v,v+self._n+2)
        self.addEdge(v,v+self._n+1)
        self.addEdge(v,v-self._n-2)
        self.addEdge(v,v-self._n+2)
        self.addEdge(v,v-self._n+1)
        self.addEdge(v,v-self._n-1)
        
    
    def computeHorseJumpsR(self,v:int,out = []): 
        """
        Recursive function
        v: initial position of the horse
        """
        self.computeHorseAdjacents(v)
        self._visited[v] = True
        out.append(v)

        for i in self._adjacents[v]:
            if self._visited[i] == False: 
                self.computeHorseJumpsR(i,out)
        return out




def main():
    Chessboard = BoardGraph([i for i in range(10000)])
    jumps = Chessboard.computeHorseJumpsR(3)
    print(jumps)
    print(len(jumps)) 
    """
    #Check all the jumps are valid and different
    for i in range(len(jumps)):
        for j in range(i+1,len(jumps)):
            if jumps[i] == jumps[j]:
                print("Error: repeated jump")
    """
    
        
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))