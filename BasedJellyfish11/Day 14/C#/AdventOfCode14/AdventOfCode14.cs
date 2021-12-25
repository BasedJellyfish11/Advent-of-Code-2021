using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace AdventOfCode14
{
    internal static class AdventOfCode14
    {
        private const int REPETITIONS = 40;
        
        private static async Task Main()
        { 
            // Parse the input
            string[] input = await File.ReadAllLinesAsync("../../../../../input");
            Dictionary<string, string> instructions = 
                input.Skip(2).Select(line => line.Split(" -> "))
                     .ToDictionary(kvPair => kvPair[0], kvPair => kvPair[1]);

            // Create the needed data structures
            Dictionary<char, long> characterCounts = new();
            Dictionary<string, long> pairCounts = new();

            // Populate the structures with the initial template
            string template = input[0];
            characterCounts.Add(template[0], 1);
            foreach ( (char first, char second) in template.Zip(template.Skip(1)))
            {
                if (characterCounts.ContainsKey(second))
                    characterCounts[second]++;
                else
                    characterCounts.Add(second, 1);

                string pair = string.Concat(first, second);
                if (pairCounts.ContainsKey(pair))
                    pairCounts[pair]++;
                else
                    pairCounts.Add(pair, 1);

            }
            
            // Start the repetitions
            for (int repetitions = REPETITIONS; repetitions > 0; --repetitions)
            {
                // The pairs that are on the instructions will all disappear and lead to two new pairs.
                // However, we need to know how many of them there were prior to this step to know how many new pairs spawn
                Dictionary<string, long> copy = new(pairCounts);
                pairCounts = pairCounts.ToDictionary
                (
                    pair => pair.Key,
                    pair => instructions.ContainsKey(pair.Key) ? 0 : pair.Value
                );
                
                foreach ( (string key, long value) in copy)
                {
                    if(!instructions.ContainsKey(key))
                        continue;
                    
                    char newChar = instructions[key][0];
                    string newPair1 = string.Concat(key[0], newChar);
                    string newPair2 = string.Concat(newChar, key[1]);
                    
                    if(pairCounts.ContainsKey(newPair1))
                        pairCounts[newPair1] += value;
                    else
                        pairCounts.Add(newPair1, value);
                    if(pairCounts.ContainsKey(newPair2))
                        pairCounts[newPair2] += value;
                    else
                        pairCounts.Add(newPair2, value);

                    if (characterCounts.ContainsKey(newChar))
                        characterCounts[newChar] += value;
                    else
                        characterCounts.Add(newChar, value);

                }
            }

            Console.WriteLine(characterCounts.Values.Max() - characterCounts.Values.Min());
        }
    }
}