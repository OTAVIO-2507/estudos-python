import os  # Importa o módulo 'os' que é utilizado para interagir com o sistema operacional, como limpar a tela com 'cls'.

# Define a lista de números e de nomes que serão usadas mais tarde
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_de_nomes = ['Otávio', 'Ysabela', 'Miguel', 'Gabriel']

# Função para exibir as instruções iniciais para o usuário
def exibir_instrucao():
    print("""𝑺𝑬𝑳𝑬𝑪𝑰𝑶𝑵𝑬 𝑼𝑴𝑨 𝑫𝑨𝑺 𝑶𝑷𝑪̧𝑶̃𝑬𝑺 👇
      """)

# Função para exibir as opções que o usuário pode escolher
def exibir_opcoes():
    print('1.Lista de número de 1 a 10')
    print('2.Lista de 4 nomes')
    print('3.Ano de nascimento, ano Atual e sua Idade')
    print('4.Todas as Listas')
    print('5.Lista de Números Decrescente')
    print('6.Tabuada')
    print('7.Soma dos números da Lista de 1 a 10')
    print('8.Média dos núemros da Lista de 1 a 10')

# Função para voltar ao menu principal após a execução de uma ação
def voltar_ao_menu_principal():
    input('\nPressione qualquer tecla para voltar ao menu principal')  # Espera o usuário pressionar qualquer tecla para voltar
    main()  # Chama a função principal novamente para reiniciar o processo

# Função para tratar a escolha do usuário quando ele escolhe uma opção inválida
def opcao_invalida():
    print('Opção Inválida!')  # Mensagem indicando que a escolha não é válida
    voltar_ao_menu_principal()  # Retorna ao menu principal

# Função para escolher uma opção
def escolher_opcao():
    escolha_uma_opcao = input('\nEscolha uma opção: ').strip()  # Recebe a entrada do usuário e remove espaços extras

    # Verifica se a entrada do usuário é um número
    if not escolha_uma_opcao.isdigit():  # Se não for número, chama a função para tratar opção inválida
        opcao_invalida()
        return  # Sai da função caso a entrada seja inválida

    escolha_uma_opcao = int(escolha_uma_opcao)  # Converte a entrada para inteiro
    os.system('cls')  # Limpa a tela (funciona no Windows)

    # Ordena a lista de números em ordem decrescente
    numero_drecrescente = sorted(lista_de_numeros, reverse=True)

    # Condicional para realizar as ações conforme a escolha do usuário
    if escolha_uma_opcao == 1:
        print(f' {lista_de_numeros}')  # Exibe a lista de números de 1 a 10
    elif escolha_uma_opcao == 2:
        print(f'{lista_de_nomes}')  # Exibe a lista de nomes
    elif escolha_uma_opcao == 3:
        ano_nascimento = input('\nDigite sua data de nascimento: ').strip()  # Solicita o ano de nascimento do usuário
        
        # Validação para garantir que o campo de nascimento não está vazio
        if not ano_nascimento:  
            print("Você deve inserir um valor para o ano de nascimento.")
            voltar_ao_menu_principal()
            return
        
        # Verifica se o valor do ano de nascimento é um número válido
        if not ano_nascimento.isdigit():  
            print("Valor inválido! O ano de nascimento deve ser um número inteiro.")
            voltar_ao_menu_principal()
            return
            
        ano_nascimento = int(ano_nascimento)  # Converte para inteiro
        ano_atual = input('\nDigite o ano atual: ').strip()  # Solicita o ano atual

        # Validação para garantir que o campo de ano atual não está vazio
        if not ano_atual:  
            print("Você deve inserir um valor para o ano atual.")
            voltar_ao_menu_principal()
            return
        
        # Verifica se o ano atual é um número válido
        if not ano_atual.isdigit():  
            print("Valor inválido! O ano atual deve ser um número inteiro.")
            voltar_ao_menu_principal()
            return
        
        ano_atual = int(ano_atual)  # Converte para inteiro
        idade_do_usuario = ano_atual - ano_nascimento  # Calcula a idade
        print(f'\nSeu ano de nascimento é {ano_nascimento} e o ano atual é {ano_atual}, então você tem {idade_do_usuario} anos.')  # Exibe a idade

    elif escolha_uma_opcao == 4:
        # Exibe todas as listas
        todas_as_listas = [lista_de_numeros, lista_de_nomes, numero_drecrescente]
        titulo_nome = ['\nLista de Número:', '\nLista de Nome:', '\nLista de Ano:', '\nLista de Números Decrescentes:']

        for i in range(len(todas_as_listas)):
            print(f'{titulo_nome[i]} {todas_as_listas[i]}')

    elif escolha_uma_opcao == 5:
        print(numero_drecrescente)  # Exibe a lista de números em ordem decrescente
    elif escolha_uma_opcao == 6:
        # Solicita um número para mostrar a tabuada
        numero_tabuada = input('Digite um número para ver sua tabuada: ').strip()

        # Verifica se o usuário digitou algo
        if not numero_tabuada:
            print('Digite um número para ver a tabuada.')
        else:
            # Se o número tiver vírgula, avisa o usuário e substitui por ponto
            if ',' in numero_tabuada:
                print("A maneira correta de digitar um número decimal é usando o ponto (.) e não a vírgula (,).")
                numero_tabuada = numero_tabuada.replace(',', '.')  # Substitui a vírgula por ponto

            try:
                numero_tabuada = float(numero_tabuada)  # Converte para float
                for i in range(1, 11):  # Gera a tabuada
                    resultado = numero_tabuada * i
                    print(f'{numero_tabuada} x {i} = {resultado}')
            
            except ValueError:
                print("Você deve digitar um número válido.")  # Caso o valor seja inválido

    elif escolha_uma_opcao == 7:
        # Soma os números da lista e exibe o resultado
        numero_soma = sum(lista_de_numeros)
        print(numero_soma)    
    elif escolha_uma_opcao == 8:
        # Calcula e exibe a média da lista de números
        valor_media = sum(lista_de_numeros) / len(lista_de_numeros)
        print(f'O valor da média da Lista é igual a {valor_media}')
    else:
        opcao_invalida()  # Caso a opção não seja válida, chama a função de opção inválida

    # Depois de terminar a execução da opção, pede para voltar ao menu principal
    voltar_ao_menu_principal()

# Função principal que inicia o programa
def main():
    os.system('cls')  # Limpa a tela
    exibir_instrucao()  # Exibe a instrução inicial
    exibir_opcoes()  # Exibe as opções disponíveis
    escolher_opcao()  # Chama a função para escolher a opção

# Chama a função principal para iniciar o programa
if __name__ == '__main__':
    main()
