
class UnionFind:
    def __init__(self,size):
        # -nが木のroot
        #親ノードの位置を格納
        self.table=[-1 for i in range(size)]

    def _find(self,x):
        while self.table[x]>=0:
            x=self.table[x]
        return x

    def find(self,x):
        if self.table[x]<0:
            return x
        self.table[x]=self.find(self.table[x])
        return self.table[x]


    def union(self,x,y):
        s1=self.find(x)
        s2=self.find(y)
        if s1!=s2:
            if self.table[s1]>=self.table[s2]:
                self.table[s1]+=self.table[s2]
                self.table[s2]=s1
            else:
                self.table[s2]+=self.table[s1]
                self.table[s1]=s2
            return True
        return False

    def get_ntree(self):
        res=0
        for c in self.table:
            if c<0:
                res+=1
        return res
    
    def is_same(self,x,y):
        return self.find(x)==self.find(y)

    def get_nclass(self):
        done=[]
        for x in range(len(self.table)):
            if x in done:
                continue
            while self.table[x]>=0:
                done.append(x)
                x=self.table[x]
            





if __name__ == '__main__':

    import random

    size=10
    data = [(random.randint(0, size - 1), random.randint(0, size - 1)) for _ in range(size)]

    print(data)
    uf=UnionFind(size)

    print(uf.table)

    uf.union(4,5)
    uf.union(5,6)

    print(uf.table)
