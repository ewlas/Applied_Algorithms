import math
import random


class Graph:
    def __init__(self, VerticeNum):
        self.VerticeNum = VerticeNum
        self.adjMatrix = []
        for i in range(VerticeNum):
            self.adjMatrix.append([0 for i in range(VerticeNum)]) 
    
    def mat_to_list(self):
        adj_list = [[] for i in range(self.VerticeNum)]
        for i in range(self.VerticeNum):
            adj_list[i] = []
            for j in range(self.VerticeNum):
                if self.adjMatrix[i][j] != 0:
                    adj_list[i].append([j, self.adjMatrix[i][j]])
        return adj_list
    def list_to_mat(self):
        adj_mat = []
        for i in range(self.VerticeNum):
            adj_mat.append([0 for i in range(self.VerticeNum)]) 
        for i in range(self.VerticeNum):
            for j in range(self.VerticeNum):
                if self.adjMatrix[i][j] != 0:
                    adj_mat[i][j] = self.adjMatrix[i][j]
        return adj_mat
                    
    def __str__(self):
        return '{' + ',\n'.join(map(str, self.adjMatrix[:self.VerticeNum])) + '}'

class Unoriented_Graph(Graph):

    def add_vertice(self):
        self.VerticeNum += 1
        self.adjMatrix.append([0 for i in range(self.VerticeNum)]) 
        for i in range(self.VerticeNum - 1): #bez last ryadka povnogo
            self.adjMatrix[i].append(0)
    def add_edge(self, v1, v2):
        if v1 == v2:
            self.adjMatrix[v1-1][v2-1] = 0 #ne index, a elem treba
        else:
            self.adjMatrix[v1-1][v2-1] = 1
            self.adjMatrix[v2-1][v1-1] = 1
    def del_vertice(self, vert):
        if self.adjMatrix[vert-1] == []:
            raise IndexError("No such vertice to delete (out of range)")
        else:
            del self.adjMatrix[vert-1]
            for i in range(self.VerticeNum-1):
                del self.adjMatrix[i][vert-1] 
        self.VerticeNum -= 1
    def del_edge(self, v1, v2):
        if self.adjMatrix[v1-1][v2-1] == 0:
            print(f"No edge between {v1} and {v2}")
        else:
            self.adjMatrix[v1-1][v2-1] = 0
            self.adjMatrix[v2-1][v1-1] = 0
    def erdors_renyi(self, prob):
        for i in range(self.VerticeNum):
            for j in range(self.VerticeNum):
                if random.uniform(0, 1) < prob:
                    self.add_edge(i+1, j+1)

                    
class Oriented_Graph(Graph):
    
    def add_vertice(self):
        self.VerticeNum += 1
        self.adjMatrix.append([0 for i in range(self.VerticeNum)]) 
        for i in range(self.VerticeNum - 1): 
            self.adjMatrix[i].append(0)
    def add_edge(self, v1, v2):
        if v1 == v2:
            self.adjMatrix[v1-1][v2-1] = 0 
        else:
            self.adjMatrix[v1-1][v2-1] = 1
    def del_vertice(self, vert):
        if self.adjMatrix[vert-1] == []:
            raise IndexError("No such vertice to delete (out of range)")
        else:
            del self.adjMatrix[vert-1]
            for i in range(self.VerticeNum-1):
                del self.adjMatrix[i][vert-1] 
        self.VerticeNum -= 1

    def del_edge(self, v1, v2):
        if self.adjMatrix[v1-1][v2-1] == 0:
            print(f"No edge between {v1} and {v2}")
        else:
            self.adjMatrix[v1-1][v2-1] = 0

    def erdors_renyi(self, prob):
        for i in range(self.VerticeNum):
            for j in range(self.VerticeNum):
                if random.uniform(0, 1) < prob:
                    self.add_edge(i+1, j+1)

class Weighted_Graph(Graph):
    def add_vertice(self):
        self.VerticeNum += 1
        self.adjMatrix.append([0 for i in range(self.VerticeNum)]) 
        for i in range(self.VerticeNum - 1):
            self.adjMatrix[i].append(0)
    def add_edge(self, v1, v2, weight):
        if v1 == v2:
            self.adjMatrix[v1-1][v2-1] = 0
        else:
            self.adjMatrix[v1-1][v2-1] = weight
    def del_vertice(self, vert):
        if self.adjMatrix[vert-1] == []:
            raise IndexError("No such vertice to delete (out of range)")
        else:
            del self.adjMatrix[vert-1]
            for i in range(self.VerticeNum-1):
                del self.adjMatrix[i][vert-1] 
        self.VerticeNum -= 1

    def del_edge(self, v1, v2):
        if self.adjMatrix[v1-1][v2-1] == math.inf:
            print(f"No edge between {v1} and {v2}")
        else:
            self.adjMatrix[v1-1][v2-1] = 0
    def erdors_renyi(self, prob):
        for i in range(self.VerticeNum):
            for j in range(self.VerticeNum):
                if random.uniform(0, 1) < prob:
                    self.add_edge(i+1, j+1, int(random.uniform(1, 100)))

       

graph = Weighted_Graph(3)
graph.erdors_renyi(0.5)
print(graph)
