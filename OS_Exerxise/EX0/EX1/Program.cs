﻿using System;
using System.Diagnostics;
using System.Threading;

namespace OS_Sync_Ex_01
{
    class Program
    {
        private static int sum = 0;

        static void plus()
        {
            int i;
            for(i = 1; i < 1000001; i++){
                sum += i;
            }
        }
        static void minus()
        {
            int i;
            for(i = 1; i < 1000000; i++){
                sum -= i;
            }
        }
        static void Main(string[] args)
        {
            /*using Thread it cause concurency problem*/
            Thread P = new Thread(new ThreadStart(plus));
            Thread M = new Thread(new ThreadStart(minus));

            Stopwatch sw = new Stopwatch();
            Console.WriteLine("Strat...");
            sw.Start();

            P.Start();
            M.Start();

            P.Join();
            M.Join();

            sw.Stop();
            Console.WriteLine("sum = {0}", sum);
            Console.WriteLine("Time used = {0}", sw.ElapsedMilliseconds.ToString() + "ms");

        }
    }
}