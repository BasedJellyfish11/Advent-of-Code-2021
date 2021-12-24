using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace AdventOfCode05
{
    internal struct Segment
    {
        public int startX;
        public int startY;
        public int endX;
        public int endY;

        public override string ToString()
        {
            return $"{startX},{startY} -> {endX},{endY}";
        }
    }

    internal static class AdventOfCode05
    {
        private static List<(int, int)>? findIntegerPointsOfSegment(Segment segment)
        {
            // y = slope * x + n
            List<(int, int)> result = new();
            if (segment.startX == segment.endX)
            {
                result.AddRange
                    (Enumerable.Range(Math.Min(segment.startY, segment.endY), Math.Abs(segment.startY - segment.endY) + 1).Select(y => (segment.startX, y)));
                return result;
            }

            double slope = (segment.endY - segment.startY) / (double)(segment.endX - segment.startX);
            double n = -slope * segment.startX + segment.startY;

            // We are limiting lines to horizontal, vertical, and 45 degrees (in p2) for some reason in this problem haha yeah
            #if PART_1
            if (slope != 0)
                return null;
            #elif PART_2
            if (slope is not (0 or 1 or -1))
                return null;
            #endif

            int iterStart = Math.Min(segment.startX, segment.endX);
            int iterEnd = Math.Max(segment.startX, segment.endX);
            for (int x = iterStart; x <= iterEnd; ++x)
            {
                double y = slope * x + n;
                if (y % 1 == 0) // This %1 is leftover from calcing non 45 degree slopes too, but still wanting to make sure y is an int
                    result.Add((x, (int)y));
            }

            return result;
        }

        private static async Task Main()
        {
            IEnumerable<Segment> segments =
                (await File.ReadAllLinesAsync("../../input"))
                .Select(line => Regex.Match(line, @"^(\d+),(\d+) -> (\d+),(\d+)$", RegexOptions.Compiled))
                .Select(match => match.Groups.Values.Skip(1).Select(group => int.Parse(group.Value)).ToArray())
                .Select(groupValues => new Segment { startX = groupValues[0], startY = groupValues[1], endX = groupValues[2], endY = groupValues[3] });

            List<(int, int)> points = new(110000);
            foreach (Segment segment in segments)
                points.AddRange(findIntegerPointsOfSegment(segment) ?? new());
            
            Console.WriteLine(points.GroupBy(x => x).Count(y => y.Count() > 1));
        }
    }
}