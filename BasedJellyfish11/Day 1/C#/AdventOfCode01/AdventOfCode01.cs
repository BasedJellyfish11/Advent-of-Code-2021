using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace AdventOfCode01
{
    internal static class AdventOfCode01
    {
        private static async Task Main()
        {
            // Copy pasting the input is annoying sue me
            int[] enumerable = (await File.ReadAllLinesAsync("input")).Select(int.Parse).ToArray();

            uint result = 0;
            for (int i = 0; i < enumerable.Length-3; ++i)
                if (enumerable[i..(i + 3)].Sum() < enumerable[(i + 1)..(i + 4)].Sum())
                    ++result;

            Console.WriteLine(result);
            
            /*
             * Task one was something like
             
                for (int i = 1; i < enumerable.Length; ++i)
                {
                    if (enumerable[i] > enumerable[i-1])
                        ++result;
                }
             */
        }
    }
}