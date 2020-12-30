// criar uma aplicação que salva o nome e nota de alunos em array e depois retorna a lista dos alunos com aas notas
// bonus: retornar a média da nota dos alunos cadastrados

using System;

namespace Projetos_Alunos
{
    class Program
    {
        static void Main(string[] args)
        {
            Aluno[] alunos = new Aluno[50];
            int indexAlunos = 0;
            string opcao = Menu.Menu_1();

            while (opcao.ToLower() != "x")
            {

                switch (opcao)
                {
                    case "1":
                        Console.WriteLine();
                        Console.WriteLine("Informe o nome do aluno:");
                        Console.Write("==> ");
                        var aluno = new Aluno();
                        aluno.Nome = Console.ReadLine().ToUpperInvariant();
                        Console.WriteLine();


                        Console.WriteLine($"Informe a nota do aluno {aluno.Nome}:");
                        Console.Write("==> ");
                        
                        if (decimal.TryParse(Console.ReadLine(), out decimal nota)) {
                            aluno.Nota = nota;
                        }else{
                            throw new ArgumentException("Nota deve ser do tipo decimal !");
                        }

                        alunos[indexAlunos] = aluno;
                        indexAlunos++;
                        Console.WriteLine($"Quantidade restante de cadastros: {50 - indexAlunos} alunos.");
                        break;

                    case "2":
                        Console.WriteLine();
                        foreach (var registro in alunos){

                            if (! string.IsNullOrEmpty(registro.Nome)){
                                Console.WriteLine($"|Aluno: {registro.Nome} -- Nota: {registro.Nota}");
                            }
                        }
                        break;

                    case "3":
                        Console.WriteLine();
                        decimal notaTotal = 0, quantAlunos = 0;

                        for (int i = 0; i < alunos.Length; i++){

                            if (! string.IsNullOrEmpty(alunos[i].Nome)){ // se atentar com o uso do sinal !
                                notaTotal = notaTotal + alunos[i].Nota;

                                quantAlunos++;
                            }
                        }

                        var media = notaTotal / quantAlunos;
                        ConceitoEnum conceitoGeral;

                        if (media < 2){
                            conceitoGeral = ConceitoEnum.E;
                        }
                        
                        else if (media < 4){
                            conceitoGeral = ConceitoEnum.D; 
                        }
                        
                        else if (media <= 6){
                            conceitoGeral = ConceitoEnum.C; 
                        }
                        
                        else if (media < 8){
                            conceitoGeral = ConceitoEnum.B; 
                        }
                        else{
                            conceitoGeral = ConceitoEnum.A;
                        }

                        Console.WriteLine($"|Média geral dos alunos registrados: {media} -- Conceito geral: {conceitoGeral}");

                        break;

                    default:
                        throw new ArgumentOutOfRangeException("Opção inválida !");
                }

                opcao = Menu.Menu_1();
            }
        }
    }
}
