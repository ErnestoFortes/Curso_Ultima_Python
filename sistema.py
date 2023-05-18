from Ex115.lib.interface import *
from Ex115.lib.arquivo import *
from time import sleep

arq = 'Cursoemvideo.txt'

if arquivoexiste(arq):
    print('Arquivo encontrado com sucesso!!')
else:
    print('Arquivo não encontrado!')
    criararquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'cadastrar nova pessoa', 'sair do sistam'])
    if resp == 1:
        #opção de listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resp == 2:
        #opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Digite o seu nome Nome: '))
        idade = leiaInt('Digite a sua Idade: ')
        nascimento = str(input('Digite a sua data de nascimento: '))
        CPF = str(input('Digite o seu CPF: '))
        cadastrar(arq, nome, idade, nascimento, CPF)
    elif resp == 3:
        #Opção de sair do sistema
        cabeçalho("saindo do sistema .... Até logo")
        break
    else:
        cabeçalho('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)





