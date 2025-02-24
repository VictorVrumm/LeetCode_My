import java.util.*;

public class leetcode# {
    // Mapa para armazenar o caminho do Bob
    private Map<Integer, Integer> bobPath;
    // Array de visitados para controle na busca
    private boolean[] visited;
    // Lista de adjacência representando a árvore
    private List<List<Integer>> tree;
    
    public int mostProfitablePath(int[][] edges, int bob, int[] amount) {
        int n = amount.length, maxIncome = Integer.MIN_VALUE;
        tree = new ArrayList<>();
        bobPath = new HashMap<>();
        visited = new boolean[n];
        Queue<int[]> nodeQueue = new LinkedList<>();
        nodeQueue.add(new int[] { 0, 0, 0 }); // Inicializa a fila com o nó raiz (0)
        
        // Inicializa a lista de adjacência da árvore
        for (int i = 0; i < n; i++) {
            tree.add(new ArrayList<>());
        }

        // Preenche a estrutura da árvore a partir das arestas
        for (int[] edge : edges) {
            tree.get(edge[0]).add(edge[1]);
            tree.get(edge[1]).add(edge[0]);
        }

        // Encontra o caminho do Bob até a raiz
        findBobPath(bob, 0);
        Arrays.fill(visited, false); // Reseta o array de visitados
        
        // BFS para calcular o caminho mais lucrativo
        while (!nodeQueue.isEmpty()) {
            int[] node = nodeQueue.poll();
            int sourceNode = node[0], time = node[1], income = node[2];

            // Verifica se Bob já passou pelo nó e ajusta o lucro
            if (!bobPath.containsKey(sourceNode) || time < bobPath.get(sourceNode)) {
                income += amount[sourceNode];
            } else if (time == bobPath.get(sourceNode)) {
                income += amount[sourceNode] / 2;
            }

            // Se for um nó folha (exceto a raiz), atualiza o máximo de lucro
            if (tree.get(sourceNode).size() == 1 && sourceNode != 0) {
                maxIncome = Math.max(maxIncome, income);
            }
            
            // Adiciona os nós adjacentes na fila para continuar a BFS
            for (int adjacentNode : tree.get(sourceNode)) {
                if (!visited[adjacentNode]) {
                    nodeQueue.add(new int[] { adjacentNode, time + 1, income });
                }
            }

            visited[sourceNode] = true; // Marca o nó como visitado
        }
        return maxIncome;
    }

    // Método recursivo para encontrar o caminho do Bob até a raiz
    private boolean findBobPath(int sourceNode, int time) {
        bobPath.put(sourceNode, time);
        visited[sourceNode] = true;

        if (sourceNode == 0) {
            return true; // Chegou na raiz
        }

        // Continua a busca para encontrar o caminho do Bob
        for (int adjacentNode : tree.get(sourceNode)) {
            if (!visited[adjacentNode]) {
                if (findBobPath(adjacentNode, time + 1)) {
                    return true;
                }
            }
        }
        bobPath.remove(sourceNode); // Remove o nó se não fizer parte do caminho do Bob
        return false;
    }

    public static void main(String[] args) {
        // Exemplo de teste
        int[][] edges = { {0, 1}, {1, 2}, {1, 3}, {3, 4} };
        int bob = 3;
        int[] amount = { -2, 4, 2, -4, 6 };

        Solution sol = new Solution();
        int result = sol.mostProfitablePath(edges, bob, amount);
        System.out.println("Resultado: " + result); // Exibe o resultado final
    }
}
