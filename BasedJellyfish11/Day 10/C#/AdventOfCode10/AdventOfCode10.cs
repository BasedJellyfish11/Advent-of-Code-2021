using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace AdventOfCode10
{
    internal static class AdventOfCode10
    {
        private static async Task Main()
        {
            Dictionary<char, char> characterRelation = new()
            {
                { '{', '}' },
                { '(', ')' },
                { '[', ']' },
                { '<', '>' },
            };

            Dictionary<char, int> characterScore = new()
            {
                { ')', 3 },
                { ']', 57 },
                { '}', 1197 },
                { '>', 25137 },
            };

            Dictionary<char, int> autocompleteScore = new()
            {
                { '(', 1 },
                { '[', 2 },
                { '{', 3 },
                { '<', 4 },
            };

            string[] input = await File.ReadAllLinesAsync("../../../../../input");
         
            int errorScore = 0;
            List<long> completionScores = new();
            Stack<char> characterStack = new();
            
            foreach (string line in input)
            {
                bool corrupted = false;
                characterStack.Clear();
            
                foreach (char character in line)
                {
                    
                    if(characterRelation.ContainsKey(character))
                        characterStack.Push(character);
                
                    else
                    {
                        try
                        {
                            char poppedChar = characterStack.Pop();
                            if (characterRelation[poppedChar] == character) 
                                continue;
                            
                            errorScore += characterScore[character];
                            corrupted = true;
                        }
                        catch (InvalidOperationException)
                        {
                            corrupted = true;
                            errorScore += characterScore[character];
                        }
                    }
                }
                
                if(corrupted)
                    continue;
                completionScores.Add(characterStack.Aggregate<char, long>(0, (current, character) => current * 5 + autocompleteScore[character]));

            }
            
            Console.WriteLine(errorScore);
            completionScores = completionScores.OrderBy(x => x).ToList();
            Console.WriteLine(completionScores[completionScores.Count/2]);
        }
    }
}