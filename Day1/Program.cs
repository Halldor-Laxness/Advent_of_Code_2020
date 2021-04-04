using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Day1
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] input = File.ReadAllLines("/Users/danyang/Code/Advent of Code/Day1/input.txt");
            List<int> data = (Array.ConvertAll(input, s => Int32.Parse(s))).ToList();

            for (int i = 0; i < data.Count; i++)
            {
                var target = 2020 - data[i];

                if(data.Contains(target))
                {
                    Console.WriteLine("OutCome: {0}", target * data[i]);
                    break;
                }
            }
        }
    }
}
