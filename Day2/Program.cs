using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace Day2
{

    class SplitedData
    {
        List<string> rang = new List<string>();
        List<string> target = new List<string>();
        List<string> cleanedtarget = new List<string>();
        List<string> data = new List<string>();
        List<int> miniRang = new List<int>();
        List<int> maxRang = new List<int>();
        public int PartOneoutcomeCount;
        public int PartTwooutComeCount;

        public void ReadData()
        {
            using (StreamReader sr = new StreamReader("/Users/danyang/Code/Advent of Code/Day2/input.txt"))
            {
                string line;
                string[] strArray;
                while ((line = sr.ReadLine()) != null)
                {
                    strArray = line.Split(" ");

                    rang.Add(strArray[0]);
                    target.Add(strArray[1]);
                    data.Add(strArray[2]);
                }
            }

            foreach (var item in rang)
            {
                string[] rangArray;
                rangArray = item.Split("-");
                miniRang.Add(Convert.ToInt32(rangArray[0]));
                maxRang.Add(Convert.ToInt32(rangArray[1]));
            }


            foreach (var item in target)
            {
                string[] removed;
                removed = item.Split(":");
                cleanedtarget.Add(removed[0]);
            }   
        }

        public void PartOneoutcome()
        {
            for (int i = 0; i < data.Count; i++)
            {
                char targetN = Convert.ToChar(cleanedtarget[i]);
                int count = data[i].Count(f => f == targetN);
                int miniR = miniRang[i];
                int maxR = maxRang[i];

                if(count>= miniR && count <= maxR)
                {
                    PartOneoutcomeCount++;
                }
            }

            Console.Write($"the number of valid password is: {PartOneoutcomeCount}");
        }

        public void PartTwoOutcome()
        {
            for (int i = 0; i < data.Count; i++)
            {
                char targetN = Convert.ToChar(cleanedtarget[i]);
                int miniP = miniRang[i];
                int maxP = maxRang[i];
                string targetdata = data[i];

                char miniT = Convert.ToChar(targetdata[miniP - 1]);
                char maxT = Convert.ToChar(targetdata[maxP - 1]);

                if (miniT == targetN ^ maxT == targetN)
                {
                    PartTwooutComeCount++;
                }


            }
            Console.Write($"the number of Part Two valid password is: {PartTwooutComeCount}");
        }

    }


    class Program
    {
        static void Main(string[] args)
        {
            var sd = new SplitedData();
            sd.ReadData();
            //sd.PartOneoutcome();
            sd.PartTwoOutcome();
            Console.Read();
        }
    }
}
