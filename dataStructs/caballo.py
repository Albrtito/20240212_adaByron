from graphs import adjacentListGraph
import time

 
class BoardGraph(adjacentListGraph): 
    def __init__(self,vertices):
        super().__init__(vertices)
        self._visited = [False for i in range(64)]
        
    def computeHorseAdjacents(self,v:int):
        self.addEdge(v,v+8-2)
        self.addEdge(v,v+8+2)
        self.addEdge(v,v+16-1)
        self.addEdge(v,v-8-2)
        self.addEdge(v,v-8+2)
        self.addEdge(v,v-16+1)
        self.addEdge(v,v-16-1)
        self.addEdge(v,v+16+1)
    
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
    Chessboard = BoardGraph([i for i in range(64)])
    jumps = Chessboard.computeHorseJumpsR(3)
    print(jumps)
    print(len(jumps)) 
    
        
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))