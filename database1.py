import mysql.connector

class DataBase1():
    def __init__(self, banco = "adocao") -> None:
        self.banco = banco

    def connect(self):
        #self.conn = mysql.connector.connect(host='localhost',database='abrec2',user='root',password='3545')
        self.conn = mysql.connector.connect(host='192.168.22.9',database='adocao',user='root',password='fabrica@2022')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado ao Servidor de Banco de Dados: ", db_info)
        else:
            print("Erro")  



    def cadastrar_animal(self,animal ):
        self.connect()
        try: 
            self.cursor.execute("""
                    INSERT INTO adocao (especie,nome,raca,cor,idade,peso,porte,sexo,situacao) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,(animal[0],animal[1],animal[2],animal[3],animal[4],animal[5],animal[6],animal[7],animal[8]))
            self.conn.commit()

            '''campos_tabela = ('especie','raca','cor','idade','peso','porte','situacao')
        
            qntd = ("?,?,?,?,?,?,?")
            try:
                self.cursor.execute(f""" INSERT INTO adocao {campos_tabela}
                VALUES({qntd}),""")'''

            return "OK"

        except Exception as err:
            #print(err)
            return "ERRO",str(err)

        finally:
            self.close_connection()

    def buscar_todos(self):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT * FROM adocao ORDER BY id_animal;
            """)
            result = self.cursor.fetchall()
            return result
            
            #verifica os dados do select
            # for linha in result:
            #    print(linha)
            
            # return result
            #retorna a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def deletar_animal(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM adocao WHERE id_animal = '{id}'")
            self.conn.commit()
            return 'OK'



        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def alterar_animal(self, tupla_de_dados):
        #print(tupla_de_dados)
        self.connect()
        try:
            self.cursor.execute(f"""UPDATE adocao SET 
            especie = '{tupla_de_dados[1]}',
            nome = '{tupla_de_dados[2]}',
            raca = '{tupla_de_dados[3]}',
            cor = '{tupla_de_dados[4]}',
            idade = '{tupla_de_dados[5]}',
            peso = '{tupla_de_dados[6]}'
            porte = '{tupla_de_dados[7]}'
            sexo = '{tupla_de_dados[8]}'
            situacao = '{tupla_de_dados[9]}'
            WHERE id_animal = {tupla_de_dados[0]}
            """)
            self.conn.commit()
            #quando o dado for string deve ter '{var}' se for inteiro somente {id}
            return 'OK','Dados atualizados com sucesso!!!'

        except AttributeError as err:
            print(err)
        
        finally:
            self.close_connection()
    
    def filter(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT * FROM adocao WHERE nome LIKE '%{texto}%';
            """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            for linha in result:
                print(linha)
            
            return result
            #retorna a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada com sucesso!!")




    
if __name__ == "__main__":
    db = DataBase1()
    db.connect()
    db.close_connection()

