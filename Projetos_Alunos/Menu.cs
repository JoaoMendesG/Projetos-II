using System;

namespace Projetos_Alunos
{
    public class Menu
    {
        public static string Menu_1()
        {
            Console.ForegroundColor = ConsoleColor.DarkGreen;
            Console.WriteLine();
            Console.WriteLine("=====Menu=====");
            Console.WriteLine();
            Console.ForegroundColor = ConsoleColor.White;

            Console.WriteLine("Escola uma das opções abaixo:");
            Console.WriteLine("1 - Cadastrar novo aluno.");
            Console.WriteLine("2 - Conferir lista de alunos.");
            Console.WriteLine("3 - Checar média geral das nota.");
            Console.WriteLine("x - sair.");

            Console.Write("==> ");

            string opcao;
            opcao = Console.ReadLine();
            return opcao;
        }
    }
}