class SparseSet:
    def __init__(self, maxVal, capacity):
        self.sparse = [-1] * (maxVal + 1)  # 0+maxval
        self.dense = [0] * capacity
        self.maxVal = maxVal
        self.capacity = capacity
        self.n = 0
    
    def Search(self, x):
        if x > self.maxVal:
            return -1
        if self.sparse[x] < self.n and self.dense[self.sparse[x]] == x:
            return self.sparse[x]  # cuz index of x in dense)
        return -1
            
    def Insert(self, x):
        if x > self.maxVal:  # maximum already defined 
            return -1
        if self.n >= self.capacity:
            return -1
        if self.Search(x) == -1:
            self.dense[self.n] = x
            self.sparse[x] = self.n
            self.n += 1

    def Delete(self, x):
        index = self.Search(x)
        if index == -1:
            return

        tmp = self.dense[self.n - 1]
        self.dense[self.sparse[x]] = tmp
        self.sparse[tmp] = self.sparse[x]
        self.n -= 1

    def Clear(self):
        self.n = 0

    def Intersection(self, set2):
        min_n = min(self.n, set2.n)
        maxVal_of_two = max(self.maxVal, set2.maxVal)
        iSet = SparseSet(maxVal_of_two, min_n)

        if self.n < set2.n:
            for i in range(self.n):
                if set2.Search(self.dense[i]) != -1:
                    iSet.Insert(self.dense[i])
        else:
            for i in range(set2.n):
                if self.Search(set2.dense[i]) != -1:
                    iSet.Insert(set2.dense[i])

        return iSet
    
    def Union(self, set2):
        MaxVal_of_twoU = max(self.maxVal, set2.maxVal)
        maxCapU = self.n + set2.n
        uSet = SparseSet(MaxVal_of_twoU, maxCapU)

        for i in range(self.n):
            uSet.Insert(self.dense[i])

        for i in range(set2.n):
            if uSet.Search(set2.dense[i]) == -1:
                uSet.Insert(set2.dense[i])

        return uSet
    
    def SetDif(self, set2):
        MaxVal_Diff = max(self.maxVal, set2.maxVal)
        MaxCap_Diff = self.n
        DiffSet = SparseSet(MaxVal_Diff, MaxCap_Diff)
        for i in range(self.n):
            if set2.Search(self.dense[i]) == -1:
                DiffSet.Insert(self.dense[i])
        return DiffSet
    
    def IsSubSet(self, set2):
        for i in range(self.n):
            if set2.Search(self.dense[i]) == -1:
                return False
        return True   

    def SymDif(self, set2):
        uSet = self.Union(set2)
        iSet = self.Intersection(set2)
        SymDif = uSet.SetDif(iSet)
        
        return SymDif
    
    def __str__(self):
        return '{' + ', '.join(map(str, self.dense[:self.n])) + '}'
    

