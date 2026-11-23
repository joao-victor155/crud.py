import mysql.connector
from crud import AlunoCRUD

def menu():
    print("\n--- SISTEMA DE CADASTRO DE ALUNOS ---")
    print("1 - Cadastrar novo aluno (Create)")
    print("2 - Listar todos os alunos (Read)")
    print("3 - Atualizar curso preferido (Update)")
    print("4 - Excluir aluno (Delete)")
    print("0 - Sair")
    return input("Escolha uma opção: ").strip()

def main():

    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
           
            database="cadastro"
        )
    except Exception as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return

    
    crud = AlunoCRUD(conexao)

    while True:
        opcao = menu()

        if opcao == "1":
            print("\n--- NOVO ALUNO ---")
            nome = input("Nome: ").strip()
            profissao = input("Profissão: ").strip()
            nascimento = input("Data de nascimento (AAAA-MM-DD): ").strip()
            sexo = input("Sexo (M/F): ").strip().upper()
            peso = float(input("Peso (ex: 75.5): ").replace(",", "."))
            altura = float(input("Altura (ex: 1.75): ").replace(",", "."))
            nacionalidade = input("Nacionalidade [Enter para Brasil]: ").strip() or "Brasil"
            
            curso_input = input("ID do curso preferido [Enter para deixar vazio]: ").strip()
            cursopreferido = int(curso_input) if curso_input.isdigit() else None

            crud.criar_aluno(nome, profissao, nascimento, sexo, peso, altura, nacionalidade, cursopreferido)

        elif opcao == "2":
            crud.listar_alunos()

        elif opcao == "3":
            print("\n--- ATUALIZAR CURSO PREFERIDO ---")
            criterio = input("Digite o ID ou o Nome exato do aluno: ").strip()
            novo_curso = input("Digite o novo ID do curso preferido (1 a 30): ").strip()
            
            if novo_curso.isdigit():
                crud.atualizar_curso_preferido(criterio, int(novo_curso))
            else:
                print("\n[AVISO] O ID do curso precisa ser um número.")

        elif opcao == "4":
            print("\n--- EXCLUIR ALUNO ---")
            criterio = input("Digite o ID ou o Nome exato do aluno para excluir: ").strip()
            crud.deletar_aluno(criterio)

        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break

        else:
            print("\n[AVISO] Opção inválida! Tente novamente.")

    
    if conexao.is_connected():
        conexao.close()
        print("Conexão com o banco encerrada.")

if __name__ == "__main__":
    main()