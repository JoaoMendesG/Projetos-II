using System;
using EstruturaPilha.Empilha;

namespace EstruturaPilha
{
    class Program
    {
        static void Main()
        {
            var s = new Pilha();
            s.Empilha(1);
            Console.WriteLine(s.Desempilha());
        }
    }
}
