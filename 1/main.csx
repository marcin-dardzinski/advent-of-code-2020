#!/usr/bin/env dotnet-script

using System.Collections.Generic;

var xs = File.ReadLines("input.txt").Select(x => int.Parse(x));
var set = new SortedSet<int>(xs);

foreach (var x in set.Reverse())
{
    var diff = 2020 - x;
    foreach (var y in set.GetViewBetween(0, diff))
    {
        var z = 2020 - x - y;
        if (set.Contains(z))
        {
            System.Console.WriteLine(x * y * z);
        }
    }
}