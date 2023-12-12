import requests


def run():
    cep = input('Digite o CEP: ')

    # Remover espaços, pontos e espaços extras
    clean_cep = cep.replace(' ', '').replace('.', '').strip()

    try:
        response = requests.get(f'https://viacep.com.br/ws/{clean_cep}/json/')
        data = response.json()

        if 'erro' not in data:
            print(data['logradouro'])
            print(f"{data['localidade']}/{data['uf']}")
        else:
            print('CEP não encontrado.')

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")


if __name__ == "__main__":
    run()
