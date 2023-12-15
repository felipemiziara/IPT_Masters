def dfs(node, adj, dp, vis):   
    #Marca o nó como visitado.
    vis[node] = True
    #Percorre todos os nós adjacentes.
    for i in range(0, len(adj[node])):  
        # Se não for visitado, faz uma nova busca em profundidade.
        if not vis[adj[node][i]]:
            dfs(adj[node][i], adj, dp, vis) 
        #Se visitado, coloca na tabela de distâncias a distância máxima
        # --- Entre o nó e seus adjacentes.
        dp[node] = max(dp[node], 1 + dp[adj[node][i]]) 
   
def addEdge(adj, u, v): 
    adj[u].append(v) 
   
def findLongestPath(adj, n): 
    dp = [0] * (n + 1) 
    # Vetor para maper as visitas 
    vis = [False] * (n + 1)
    # Faz uma busca em profundidade para cada nó não visitado.
    for i in range(1, n + 1):  
        if not vis[i]: 
            dfs(i, adj, dp, vis) 
    ans = 0
    # Pesquisa no vetor DP para encontrar o máximo distância.
    for i in range(1, n + 1):  
        ans = max(ans, dp[i])
    return ans 
  
# Driver Code 
if __name__ == "__main__": 
  
    n = 5
    adj = [[] for i in range(n + 1)]
   
    # Example-1 
    addEdge(adj, 1, 2) 
    addEdge(adj, 1, 3) 
    addEdge(adj, 3, 2) 
    addEdge(adj, 2, 4) 
    addEdge(adj, 3, 4) 
   
    print(findLongestPath(adj, n))