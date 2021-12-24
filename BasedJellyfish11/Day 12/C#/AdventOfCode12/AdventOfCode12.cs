using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace AdventOfCode12
{
    internal static class AdventOfCode12
    {
        private static readonly HashSet<IList<string>> paths = new();
        private static readonly HashSet<IList<string>> paths_p2 = new();

        private static async Task Main()
        {
            Dictionary<string, HashSet<string>> graph = new();
            string[] input = await File.ReadAllLinesAsync("../../../../../input");

            // Build the graph. C# has no real graphs so I'm using a Dictionary<node, paths>
            foreach (string path in input)
            {
                string[] entryExitPair = path.Split('-');
                if (graph.ContainsKey(entryExitPair[0]))
                    graph[entryExitPair[0]].Add(entryExitPair[1]);
                else
                    graph.Add(entryExitPair[0], new HashSet<string> { entryExitPair[1] });

                if (graph.ContainsKey(entryExitPair[1]))
                    graph[entryExitPair[1]].Add(entryExitPair[0]);
                else
                    graph.Add(entryExitPair[1], new HashSet<string> { entryExitPair[0] });

            }

            FindPaths(graph, "start", "end", new List<string>(){"start"});
            FindPaths2(graph, "start", "end", new List<string>(){"start"});
            Console.WriteLine(paths.Count);
            Console.WriteLine(paths_p2.Count);

        }

        private static void FindPaths(IReadOnlyDictionary<string, HashSet<string>> graph, string currentNode, string endNode, IList<string> currentPath)
        {
            if (currentNode == endNode)
            {
                paths.Add(currentPath);
                return;
            }

            foreach (string nextPossibleNode in graph[currentNode])
            {
                if(currentPath.Contains(nextPossibleNode) && nextPossibleNode.ToLower() == nextPossibleNode)
                    continue;
                List<string> nextIter = new(currentPath) { nextPossibleNode };
                FindPaths(graph, nextPossibleNode, endNode, nextIter);
            }
        }
        
        private static void FindPaths2(IReadOnlyDictionary<string, HashSet<string>> graph, string currentNode, string endNode, IList<string> currentPath)
        {
            if (currentNode == endNode)
            {
                paths_p2.Add(currentPath);
                return;
            }

            foreach (string nextPossibleNode in graph[currentNode])
            {
                if(nextPossibleNode == "start")
                    continue;
                
                bool visitedSmallCaveTwice = currentPath.GroupBy(x => x).Any(y => y.Key.ToLower() == y.Key && y.Count() > 1);
                if(visitedSmallCaveTwice && currentPath.Contains(nextPossibleNode) && nextPossibleNode.ToLower() == nextPossibleNode)
                    continue;
                
                List<string> nextIter = new(currentPath) { nextPossibleNode };
                FindPaths2(graph, nextPossibleNode, endNode, nextIter);
            }
        }
    }
}
