using System;

namespace C_
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Ready ?");

            for (int i = 3; i > 0; i = i - 1)
            {
                Console.WriteLine($"{i}...");
            }

            Console.Write("Bang !");
        }
    }
}