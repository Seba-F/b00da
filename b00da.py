import math

class Node:

    def __init__ (self, Id):
        self.neighbors = {} ## aqui estan los vecinos y sus distancias
        self.id = Id
        self.visited = 0 # 0 es blanco, no visitado. 1 es negro, exploramos a partir de el, ya conocemos la dist minima.
        self.distance = math.inf
        self.parent = False # desde donde viene para el camino mas corto

    def __repr__(self):
        return "Neighbors: "+str(self.neighbors)


def dijkstra(graph, startNode, endNode):
    def smallestDistance(nextNodes): ## queremos explorar a partir del nodo con la distancia minima 
        smallestDistance = math.inf
        for node in nextNodes:
            if smallestDistance > node.distance:
                smallestDistance = node.distance
                smallestNode = node
        nextNodes.remove(smallestNode)
        return smallestNode
    
    startNode.distance = 0
    nextNodes = [startNode]
    while nextNodes: ## mientras quedan elementos por visitar
        currentNode = smallestDistance(nextNodes)
        currentNode.visited = 1
        if currentNode.id == endNode.id: # encontramos la distancia minima al nodo deseado
            return str(currentNode.distance)
        for reachableNodeId, reachableNodeDistance in currentNode.neighbors.items():  ## recorremos los nodos alcanzables desde el nodo actual
            reachableNode = graph[reachableNodeId]
            if reachableNode.visited == 0: ## todavia no se ha explorado a partir de este elemento
                distance = currentNode.distance + reachableNodeDistance
                if distance < reachableNode.distance: ## encontramos una ruta mas corta
                    reachableNode.parent = currentNode
                    reachableNode.distance = distance
                    if reachableNode not in nextNodes: ## no queremos elementos duplicados en la lista de nodos por revisar
                        nextNodes.append(reachableNode)

    return False ## it is not posible to reach the endNode


def minDistance(node_from, node_to, fileName = "data.txt"):
    graphNodes = createGraph(fileName)
    if (node_from == node_to):
        return "0. El nodo de origen es igual al de destino."
    if node_from not in graphNodes or node_to not in graphNodes:
        return "Los nodos de inicio o termino no estan bien especificados."
    distance = dijkstra(graphNodes, graphNodes[node_from], graphNodes[node_to])
    if distance:
        return distance ## ya es string
    else:
        return "No es posible alcanzar el nodo deseado."


def createGraph(fileName):
    graphNodes = {}  # diccionario cuya llave es el id del nodo.
    file = open(fileName, "r")
    for line in file:
        line = line.strip()
        nodeData = line.split(", ")
        ## Nos aseguramos que existan ambos nodos, unidos por esta distancia.
        if not nodeData[0] in graphNodes:
            graphNodes[nodeData[0]] = Node(nodeData[0])
        if not nodeData[1] in graphNodes:
            graphNodes[nodeData[1]] = Node(nodeData[1])

        if nodeData[1] in graphNodes[nodeData[0]].neighbors:
            ## if there are two path between 2 nodes keep the smallest
            if graphNodes[nodeData[0]].neighbors[nodeData[1]] > int(nodeData[2]):
                graphNodes[nodeData[0]].neighbors[nodeData[1]] = int(nodeData[2])
                graphNodes[nodeData[1]].neighbors[nodeData[0]] = int(nodeData[2])
        else:
            graphNodes[nodeData[0]].neighbors[nodeData[1]] = int(nodeData[2])
            graphNodes[nodeData[1]].neighbors[nodeData[0]] = int(nodeData[2]) 

    file.close()
    return graphNodes


if __name__ == "__main__":
    # graphNodes = createGraph("data.txt")

    # for element in graphNodes:
    #     print(element, "->", graphNodes[element])

    print(minDistance("TT", "B"))
