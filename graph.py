import heapq as hq

class Node:
    def __init__(self):
        pass

class Edge:

    def __init__(self,edge,cost=1):
        self.node_from=edge[0]
        self.node_to=edge[1]
        self.cost=cost

    def add_node(self,node):
        self.nodes.append(node)



class myGraph:

    def __init__(self):

        self.adj={}
        self.nodes={}


    def add_edge(self,edge,cost):
        if len(edge)==1:
            edge=list(edge)


        u,v=edge[0],edge[1]

        if u not in self.nodes:
            self.adj[u] = {}
            self.nodes[u] = {}

        if v not in self.nodes:
            self.adj[v] = {}
            self.nodes[v] = {}


        # add the edge
        self.adj[u][v] = cost
        self.adj[v][u] = cost

    #|edges|本のtuppleにしたほうが良いかも
    def get_edges_from(self,node):

        return [(self.adj[node][nn],node,nn) for nn in self.adj[node]]


    #def nodes():

    def _add(self,edges,add_edges):
        for e in add_edges:
            hq.heappush(edges,e)
        return edges

    def prim(self):
        g=self

        T=[list(g.nodes)[0]]
        E=[]

        cost=0

        edges_nouse=self._add([],g.get_edges_from(T[0]))

        while True:
            print(edges_nouse)
            while True:
                try:
                    v=hq.heappop(edges_nouse)
                except:
                    return E,cost
                if not(v[1] in T):
                    to=v[1]
                    break
                elif not(v[2] in T):
                    to=v[2]
                    break

            cost+=v[0]
            T.append(to)
            E.append(v)

            es=g.get_edges_from(to)
            self._add(edges_nouse,es)


    def bermn_ford(self,start):

        nodes=self.nodes
        edges=self.edges
        dists={}
        for n in nodes:
            dists[n]=False
        dists[start]=0


        for i in range(len(nodes)):
            update=False
            for k in range(len(edges)):
                e=edges[k]
                if not dists[e.node_to]:
                    dists[e.node_to]=dists[e.node_from]+e.cost
                    update=True
                #最長の場合は符号変更
                elif dists[e.node_to]>dists[e.node_from]+e.cost:
                    dists[e.node_to]=dists[e.node_from]+e.cost
                    update=True


            if i==len(nodes)-1:
                return False

            if not update:
                break

        return dists

    '''
     def dijkstra(self,start, goal=None):

        N = len(self.adj)          # グラフのノード数
        dist = [float('inf') for i in range(N)] # 始点から各頂点までの最短距離を格納する
        prev = [float('inf') for i in range(N)]

        dist[start] = 0
        visited = []

        s=0
        avtx=1
        koho=[]
        heapq.heappush(koho,(0,start))

        aaa=[]
        vtx=self.vtx[:]
        for i,v in enumerate(vtx):
            vtx[i]=self.xy_to_n(vtx[i][0],vtx[i][1])
        vtx.remove(start)

        vmaxval=float('inf')
        while len(koho)!=0:

            d,mini=heapq.heappop(koho)
            if dist[mini]<d:
                continue


            #tt=time.time()
            if mini in vtx:
                avtx+=1
                vtx.remove(mini)
                print(vmaxval)
                vmaxval=0
                for v in vtx:
                    if vmaxval<dist[v]:
                        vmaxval=dist[v]

            sss=self.get_around(mini)
            tm+=time.time()-tt
            for k in self.get_around(mini):
                tt=time.time()
                #0.09
                ardd=self.get_edge_data(mini,k)
                tm+=time.time()-tt
                if not ardd:
                    continue

                #tt=time.time()
                # 0.12sec
                if vmaxval>=dist[k] and dist[k]>dist[mini]+ardd:# and not(k in visited):
                    dist[k]=dist[mini]+self.get_edge_data(mini,k)
                    heapq.heappush(koho,(dist[k],k))
                    prev[k]=mini
                #tm+=time.time()-tt

            #tm+=time.time()-tt
            #if s%100==0:
            #    koho=heapq.nsmallest(1000,koho)
            #    dd=list(map(lambda x:x[1],heapq.nsmallest(1000,koho,key=lambda x:x[1])))
            #    heapq.heapify(dd)
            s+=1

        print(tm)
        #input()
        return dist
    '''

    def show(self):

        import networkx as nx
        import matplotlib.pyplot as plt
        G=nx.Graph()

        for e in self.edges:

            G.add_edge(e.node_from,e.node_to,weight=e.cost)
            #print(e.node_from,e.node_to,e.cost)

        pos=nx.spring_layout(G)
        #nx.draw_networkx_edges(G,pos=pos,edgelist=G.edges())
        edge_weight=dict([((u,v,),int(d['weight'])) for u,v,d in G.edges(data=True)])

        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_weight)
        #nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_nodes(G,pos)
        nx.draw_networkx_edges(G,pos)
        nx.draw_networkx_labels(G,pos)
        #plt.axis('off')
        #nx.draw(G,with_labels=True)
        plt.show()






def spaceinput():
    return list(map(int,input().split(" ")))

if __name__=="__main__":
    g=myGraph()
    vv,ee=spaceinput()
    for i in range(ee):
        ss=spaceinput()
        g.add_edge((ss[0],ss[1]),ss[2])

    print(g.prim())
