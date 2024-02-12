
# ADJACENT LIST IMPLEMENTATION
class node:
    """
    This class allows us to represent a tuple with an adjacent vertex
    and the weight associated (by default 1, for non-unweighted graphs)
    """
    def __init__(self,v,weight=None):
        self._v=v
        self._weight=weight
    
    def __str__(self):
        if self._weight!=None:
            return '('+str(self._v)+','+str(self._weight)+')'
        else:
            return str(self._v)


class adjacentListGraph():
    """This implementation is based on adjacency lists."""
    def __init__(self,vertices:list,directed=False):
        self._vertices =vertices
        self._adjacents=[]
        self._visited = []
        self._directed=directed

        for v in self._vertices:
            self._adjacents.append([])

        
    
    def addVertex(self,v):
        self._vertices.append(v)
        self._adjacents.append([])


    def addEdge(self,i,j,weight=None):
        """This function adds the edge (i,j)"""

        if not(0 <= i <= len(self._vertices)-1):
            return
        if not(0 <= j <= len(self._vertices)-1):
            return

        # Create the connection
        self._adjacents[i].append(j)
        if self._directed==False:
            self._adjacents[j].append(i)

