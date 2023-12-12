import requests


def buscar_cep_por_endereco():
    rua = input('Digite o nome da rua: ')
    cidade = input('Digite o nome da cidade: ')
    estado = input('Digite a sigla do estado: ')

    try:
        # Substituído espaços por '+'
        rua_formatada = '+'.join(rua.split())

        # Consulta com estado, cidade e rua formatados
        response = requests.get(f'https://viacep.com.br/ws/{estado}/{cidade}/{rua_formatada}/json/')
        data = response.json()

        if data:
            if 'erro' not in data:
                if len(data) == 1:
                    print_resultado(data[0])
                else:
                    print('Foram encontradas várias opções para a rua fornecida:')
                    for i, endereco in enumerate(data, start=1):
                        print(f"{i}. {endereco['logradouro']} - {endereco['localidade']}/{endereco['uf']}")

                    opcao = int(input('Escolha o número correspondente à opção desejada: '))
                    if 1 <= opcao <= len(data):
                        print_resultado(data[opcao - 1])
                    else:
                        print('Opção inválida. Tente novamente.')
            else:
                print('Nenhum endereço encontrado para a rua fornecida.')
        else:
            print('Nenhum endereço encontrado para a rua fornecida.')

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")


def print_resultado(endereco):
    print(f"\nCEP: {endereco['cep']}")
    print(f"Rua: {endereco['logradouro']}")
    print(f"Bairro: {endereco['bairro']}")
    print(f"Cidade/UF: {endereco['localidade']}/{endereco['uf']}\n")


if __name__ == "__main__":
    buscar_cep_por_endereco()
