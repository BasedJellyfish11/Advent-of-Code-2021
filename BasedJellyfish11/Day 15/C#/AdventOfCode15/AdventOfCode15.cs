using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace AdventOfCode15
{
    internal static class AdventOfCode15
    {
        private static async Task Main()
        { 
            // Parse the input
            #if !PART2
            int[][] input = (await File.ReadAllLinesAsync("../../../../../input"))
                            .Select(x => x.ToCharArray().Select(y=> Convert.ToInt32(char.GetNumericValue(y))).ToArray())
                            .ToArray();


            #else
            int[][] input = (await File.ReadAllLinesAsync("../../../../../input2"))
                    .Select(x => x.ToCharArray().Select(y=> Convert.ToInt32(char.GetNumericValue(y))).ToArray())
                    .ToArray();
            #endif

            Dictionary<Node, HashSet<Node>> graph = new();

            for (int i = 0; i < input.Length; i++)
            {
                for (int j = 0; j < input[i].Length; j++)
                {
                    Node node = new((i, j), input[i][j]);
                    HashSet<Node> adjacentNodes = new();
                    if (i != 0)
                        adjacentNodes.Add(new Node((i - 1, j), input[i - 1][j]));

                    if (i + 1 != input.Length)
                        adjacentNodes.Add(new Node((i + 1, j), input[i + 1][j]));

                    if (j != 0)
                        adjacentNodes.Add(new Node((i, j - 1), input[i][j - 1]));
                    if (j + 1 != input[i].Length)
                        adjacentNodes.Add(new Node((i, j + 1), input[i][j + 1]));
                    
                    graph.Add(node, adjacentNodes);
                }
            }

            PriorityQueue<AStarNode, int> queue = new();
            Node endNode = new((input.Length-1, input[0].Length-1), 0);
            AStarNode startNode = new(new Node((0, 0), 0), endNode, 0);
            queue.Enqueue(startNode, 0);
            
            Console.WriteLine(AStar(graph, endNode, queue, new Dictionary<Node, int>{{startNode.node, 0}}).CurrentCost);
        }
        
        private static AStarNode AStar(IReadOnlyDictionary<Node, HashSet<Node>> graph, Node endNode, PriorityQueue<AStarNode, int> priorityQueue, Dictionary<Node, int> lowestNodeCosts)
        {
            // Dequeue the node with the lowest F
            AStarNode poppedNode;
            while (!(poppedNode = priorityQueue.Dequeue()).node.Equals(endNode))
            {
                HashSet<Node> neighbors = graph[poppedNode.node];
                foreach (AStarNode newNode in neighbors.Select
                (
                    neighbor => new AStarNode(neighbor, endNode, poppedNode.CurrentCost + neighbor.cost, new HashSet<Node>(poppedNode.previousNodes) { neighbor })
                ))
                
                {
                    if (newNode.node.Equals(endNode))
                        return newNode;
                    if (lowestNodeCosts.ContainsKey(newNode.node))
                    {
                        if (lowestNodeCosts[newNode.node] <= newNode.CurrentCost) continue;
                        lowestNodeCosts[newNode.node] = newNode.CurrentCost;

                    }
                    else
                        lowestNodeCosts.Add(newNode.node, newNode.CurrentCost);
                
                    priorityQueue.Enqueue(newNode, newNode.EstimatedCost);
                }
            }
            poppedNode = priorityQueue.Dequeue();
            
            return poppedNode;
        }

        private readonly struct Node
        {
            public readonly (int, int) coords;
            public readonly int cost;

            public Node((int, int) coords, int cost)
            {
                this.coords = coords;
                this.cost = cost;
            }

            public override int GetHashCode()
            {
                return coords.GetHashCode();
            }

            public override bool Equals(object obj)
            {
                return obj is Node newNode && newNode.coords.Equals(coords);
            }

            public override string ToString()
            {
                return coords.ToString();
            }
        }

        private readonly struct AStarNode
        {
            public readonly Node node;
            private readonly Node endNode;
            public readonly HashSet<Node> previousNodes;
            public readonly int CurrentCost;
            private int HeuristicCost => Math.Abs(node.coords.Item1 - endNode.coords.Item1) + Math.Abs(node.coords.Item2 - endNode.coords.Item2);
            public  int EstimatedCost => CurrentCost + HeuristicCost;

            public AStarNode(Node node, Node endNode, int currentCost, HashSet<Node> previousNodes = null)
            {
                this.node = node;
                this.endNode = endNode;
                CurrentCost = currentCost;
                this.previousNodes = previousNodes ?? new HashSet<Node> { node };
            }

            public override string ToString()
            {
                return $"{node.ToString()}, {CurrentCost}";
            }
        }
    }
}