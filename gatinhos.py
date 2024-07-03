import csv #Importa o módulo csv, que fornece funções para ler e escrever arquivos CSV.
from datetime import datetime

#Função para carregar os dados do arquivo CSV
def carregar_dados(filename):
    felinos = [] #Lista para guardar os dados dos felinos
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file) #Leitor CSV que mapeia a primeira linha para um dicionário
        for row in reader:
            felinos.append(row)     #Adiciona cada linha do CSV à lista felinos
    return felinos  #Retorna a lista de felinos

#Função que exibe o menu principal do sistema
def menu_principal():
    print("Bem-vindo ao sistema de gestão da ONG TRICOLOR É O GRÊMIO!")
    print("Escolha uma opção:")
    print("1) Cadastrar felino")
    print("2) Alterar status de felino")
    print("3) Consultar informações sobre felino")
    print("4) Apresentar estatísticas gerais")
    print("5) Filtragem de dados")
    print("6) Salvar")
    print("7) Sair do programa")

#Função principal que executa o programa
def main():
    filename = 'gatinhos.csv'#Nome do arquivo CSV
    felinos = carregar_dados(filename)#Carrega os dados do arquivo
    
    while True: #Loop principal do programa
        menu_principal()    #Exibe o menu principal
        opcao = input("Digite o número da opção desejada: ")    #Lê a opção do usuário
        
        if opcao == '1':
            cadastrar_felino(felinos)   #Chama a função para cadastrar um novo felino
        elif opcao == '2':
            alterar_status_felino(felinos)  #Chama a função para alterar o status de um felino
        elif opcao == '3':
            consultar_informacoes_felino(felinos)   #Chama a função para consultar informações de um felino
        elif opcao == '4':
            apresentar_estatisticas(felinos)    #Chama a função para apresentar estatísticas gerais#Chama a função para apresentar estatísticas gerais
        elif opcao == '5':
            filtrar_dados(felinos)  #Chama a função para filtrar dados
        elif opcao == '6':
            salvar_dados(filename, felinos)     #Chama a função para salvar os dados no arquivo
        elif opcao == '7':
            salvar_dados(filename, felinos)     #Salva os dados antes de sair
            print("Saindo do programa. Até mais!")
            break   #Encerra o loop e sai do programa
        else:
            print("Opção inválida. Tente novamente.")   #Mensagem de erro para opção inválida

#Função para cadastrar um novo felino
def cadastrar_felino(felinos):
    novo_felino = {}#Dicionário para armazenar os dados do novo felino
    #Solicita os dados do felino ao usuário
    novo_felino['Nome'] = input("Nome: ")
    novo_felino['Sexo'] = input("Sexo (M/F): ")
    novo_felino['Idade'] = input("Idade (meses): ")
    novo_felino['Raça'] = input("Raça: ")
    novo_felino['Cor Predominante'] = input("Cor Predominante: ")
    novo_felino['Castrado'] = input("Castrado (Sim/Não): ")
    novo_felino['FIV+'] = input("FIV+ (Sim/Não): ")
    novo_felino['FELV+'] = input("FELV+ (Sim/Não): ")
    novo_felino['Data de Resgate'] = input("Data de Resgate (dd/mm/yyyy): ")
    novo_felino['Adotado'] = input("Adotado (Sim/Não): ")
    novo_felino['Lar Temporário'] = input("Lar Temporário (Sim/Não): ")
    novo_felino['Data de Adoção/Hospedagem'] = input("Data de Adoção/Hospedagem (dd/mm/yyyy): ")
    novo_felino['Tutor'] = input("Tutor: ")
    novo_felino['Contato'] = input("Contato: ")
    novo_felino['Data da Última Vacina'] = input("Data da Última Vacina (dd/mm/yyyy): ")
    novo_felino['Data da Última Desvermifugação'] = input("Data da Última Desvermifugação (dd/mm/yyyy): ")
    novo_felino['Data do Último Antipulgas'] = input("Data do Último Antipulgas (dd/mm/yyyy): ")
    novo_felino['Informações Extras'] = input("Informações Extras: ")

    felinos.append(novo_felino) #Adiciona o novo felino à lista
    print("Felino cadastrado com sucesso!")

#Função para alterar o status de um felino existente
def alterar_status_felino(felinos):
    listar_felinos(felinos)     #Lista os felinos cadastrados
    indice = int(input("Digite o número do felino que deseja alterar: ")) - 1   #Lê o índice do felino a ser alterado

    if 0 <= indice < len(felinos):  #Verifica se o índice é válido
        felino = felinos[indice]
        print("Escolha a informação que deseja alterar:")
        for i, chave in enumerate(felino.keys(), start=1):
            print(f"{i}) {chave}: {felino[chave]}")     #Exibe as informações do felino para escolha

        while True:
            opcao = int(input("Digite o número da informação que deseja alterar (0 para sair): "))
            if opcao == 0:
                break   #Sai do loop se a opção for 0
            elif 1 <= opcao <= len(felino):
                chave = list(felino.keys())[opcao - 1]
                novo_valor = input(f"Digite o novo valor para {chave}: ")
                felino[chave] = novo_valor  #Atualiza o valor da chave escolhida
                print(f"{chave} atualizado com sucesso!")
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Felino não encontrado.")      #Mensagem de erro se o índice for inválido

#Função para consultar as informações de um felino específico
def consultar_informacoes_felino(felinos):
    listar_felinos(felinos)     #Lista os felinos cadastrados
    indice = int(input("Digite o número do felino que deseja consultar: ")) - 1   #Lê o índice do felino a ser consultado

    if 0 <= indice < len(felinos):      #Verifica se o índice é válido
        felino = felinos[indice]
        for chave, valor in felino.items():
            print(f"{chave}: {valor}")      #Exibe todas as informações do felino
    else:
        print("Felino não encontrado.")     #Mensagem de erro se o índice for inválido

#Função para apresentar estatísticas gerais sobre os felinos
def apresentar_estatisticas(felinos):
    total = len(felinos)    #Total de felinos cadastrados
    machos = sum(1 for f in felinos if f['Sexo'].lower() == 'm')    #Conta o número de machos
    femeas = total - machos     #Calcula o número de fêmeas
    adotados = sum(1 for f in felinos if f['Adotado'].lower() == 'sim')     #Conta o número de felinos adotados
    nao_adotados = total - adotados #Calcula o número de felinos não adotados
    negativos = sum(1 for f in felinos if f['FIV+'].lower() == 'não' and f['FELV+'].lower() == 'não')   #Conta o número de felinos negativos para FIV e FELV
    fiv = sum(1 for f in felinos if f['FIV+'].lower() == 'sim' and f['FELV+'].lower() == 'não')     #Conta o número de felinos positivos para FIV
    felv = sum(1 for f in felinos if f['FIV+'].lower() == 'não' and f['FELV+'].lower() == 'sim')       #Conta o número de felinos positivos para FELV
    ambos = sum(1 for f in felinos if f['FIV+'].lower() == 'sim' and f['FELV+'].lower() == 'sim')       #Conta o número de felinos positivos para FIV e FELV

  #Exibe as estatísticas calculadas
    print(f"Porcentagem de machos: {machos / total * 100:.2f}%")
    print(f"Porcentagem de fêmeas: {femeas / total * 100:.2f}%")
    print(f"Porcentagem de adotados: {adotados / total * 100:.2f}%")
    print(f"Porcentagem de não adotados: {nao_adotados / total * 100:.2f}%")
    print(f"Porcentagem de negativos para FIV+ e FELV+: {negativos / total * 100:.2f}%")
    print(f"Porcentagem de FIV+: {fiv / total * 100:.2f}%")
    print(f"Porcentagem de FELV+: {felv / total * 100:.2f}%")
    print(f"Porcentagem de FIV+ e FELV+: {ambos / total * 100:.2f}%")

#Função para filtrar dados dos felinos
def filtrar_dados(felinos):
    print("1) Consultar gatos resgatados por período")
    print("2) Consultar gatos adotados por período")
    opcao = input("Digite a opção desejada: ")  #Lê a opção do usuário

    if opcao == '1':
        inicio = int(input("Ano de início: "))
        fim = int(input("Ano de fim: "))
        #Filtra os felinos resgatados no período especificado
        resgatados = [f for f in felinos if inicio <= int(f['Data de Resgate'].split('/')[-1]) <= fim]
        listar_felinos(resgatados)  #Lista os felinos resgatados
    elif opcao == '2':
        inicio = int(input("Ano de início: "))
        fim = int(input("Ano de fim: "))
        #Filtra os felinos adotados no período especificado
        adotados = [f for f in felinos if f['Adotado'].lower() == 'sim' and inicio <= int(f['Data de Adoção/Hospedagem'].split('/')[-1]) <= fim]
        listar_felinos(adotados)    #Lista os felinos adotados
    else:
        print("Opção inválida.")     #Mensagem de erro para opção inválida

#Função para salvar os dados no arquivo CSV
def salvar_dados(filename, felinos):
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        fieldnames = felinos[0].keys()   #Obtém os nomes dos campos (colunas)
        writer = csv.DictWriter(file, fieldnames=fieldnames)    #Cria um escritor CSV com os nomes dos campos
        writer.writeheader()     #Escreve a linha de cabeçalho
        for felino in felinos:
            writer.writerow(felino)      #Escreve cada felino no arquivo
    print("Dados salvos com sucesso!")

#Função para listar os felinos cadastrados
def listar_felinos(felinos):
    for i, felino in enumerate(felinos, start=1):
        print(f"{i}) {felino['Nome']}")  #Exibe o nome de cada felino com seu índice

#Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    main()  #Chama a função principal para iniciar o programa
