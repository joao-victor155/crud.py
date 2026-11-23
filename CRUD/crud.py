class AlunoCRUD:
    def __init__(self, conexao):
        self.conexao = conexao

    # --- CREATE ---
    def criar_aluno(self, nome, profissao, nascimento, sexo, peso, altura, nacionalidade="Brasil", cursopreferido=None):
        cursor = self.conexao.cursor()
        sql = """
            INSERT INTO alunos (nome, profissao, nascimento, sexo, peso, altura, nacionalidade, cursopreferido)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (nome, profissao, nascimento, sexo, peso, altura, nacionalidade, cursopreferido)
        try:
            cursor.execute(sql, valores)
            self.conexao.commit()
            print(f"\n[OK] Aluno '{nome}' cadastrado com sucesso! (ID: {cursor.lastrowid})")
        except Exception as erro:
            print(f"\n[ERRO] Não foi possível cadastrar o aluno: {erro}")
        finally:
            cursor.close()

    # --- READ ---
    def listar_alunos(self):
        cursor = self.conexao.cursor()
        sql = "SELECT id, nome, profissao, nascimento, sexo, peso, altura, nacionalidade, cursopreferido FROM alunos"
        cursor.execute(sql)
        registros = cursor.fetchall()

        print("\n" + "=" * 95)
        print(f"{'ID':<4} | {'NOME':<26} | {'PROFISSÃO':<20} | {'NASC.':<10} | {'CURSO PREF.':<11}")
        print("=" * 95)
        for aluno in registros:
            curso = aluno[8] if aluno[8] is not None else "Nenhum"
            print(f"{aluno[0]:<4} | {aluno[1]:<26} | {str(aluno[2]):<20} | {str(aluno[3]):<10} | {str(curso):<11}")
        print("=" * 95 + "\n")
        cursor.close()

    # --- UPDATE (Atualiza curso_preferido por ID ou Nome) ---
    def atualizar_curso_preferido(self, criterio, novo_id_curso):
        cursor = self.conexao.cursor()
        try:
            if criterio.isdigit():
                sql = "UPDATE alunos SET cursopreferido = %s WHERE id = %s"
                valores = (novo_id_curso, int(criterio))
            else:
                sql = "UPDATE alunos SET cursopreferido = %s WHERE nome = %s"
                valores = (novo_id_curso, criterio)

            cursor.execute(sql, valores)
            self.conexao.commit()

            if cursor.rowcount > 0:
                print(f"\n[OK] Curso preferido atualizado para o ID {novo_id_curso} ({cursor.rowcount} registro afetado).")
            else:
                print("\n[AVISO] Nenhum aluno encontrado com esse ID ou Nome.")
        except Exception as erro:
            # Captura erro de chave estrangeira caso o idcurso informado não exista na tabela cursos
            print(f"\n[ERRO] Falha ao atualizar (verifique se o ID do curso existe): {erro}")
        finally:
            cursor.close()

    # --- DELETE (Exclui por ID ou Nome) ---
    def deletar_aluno(self, criterio):
        cursor = self.conexao.cursor()
        try:
            if criterio.isdigit():
                sql = "DELETE FROM alunos WHERE id = %s"
                valores = (int(criterio),)
            else:
                sql = "DELETE FROM alunos WHERE nome = %s"
                valores = (criterio,)

            cursor.execute(sql, valores)
            self.conexao.commit()

            if cursor.rowcount > 0:
                print(f"\n[OK] Aluno removido com sucesso ({cursor.rowcount} registro excluído).")
            else:
                print("\n[AVISO] Nenhum aluno encontrado com esse ID ou Nome.")
        except Exception as erro:
            print(f"\n[ERRO] Não foi possível excluir o aluno: {erro}")
        finally:
            cursor.close()