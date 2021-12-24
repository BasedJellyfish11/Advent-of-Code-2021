using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace AdventOfCode06
{
    internal static class AdventOfCode06
    {
        private const int DAYS_BETWEEN_BIRTHS = 7;
        private const int DAYS_BEFORE_FIRST_BIRTH = DAYS_BETWEEN_BIRTHS + 2;
        private const int ITERATIONS = 256;
        
        private static async Task Main()
        {
            IEnumerable<int> input = (await File.ReadAllLinesAsync("../../input"))
                                     .First().Split(',').Select(int.Parse);

            ulong[] lanternFish = new ulong[DAYS_BEFORE_FIRST_BIRTH];
            foreach (IGrouping<int, int> group in input.GroupBy(x => x))
            {
                lanternFish[group.Key] = Convert.ToUInt64(group.Count());
            }

            for (int i = 0; i < ITERATIONS; i++)
            {
                ulong next_iter = lanternFish[0];
                Array.Copy(lanternFish, 1, lanternFish, 0, lanternFish.Length - 1);
                lanternFish[^1] = next_iter;
                lanternFish[DAYS_BETWEEN_BIRTHS-1] += next_iter;
            }
            
            Console.WriteLine(lanternFish.Aggregate((x,y) => x+y));
        }
    }
}