endereco = "Rua Pedro Viriato Parigot de Souza, Apartamento 20, 3305, Ecoville, Curitiba, PR, 81200-452"

import re #Regular Expression == RegEx
padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')

busca = padrao.search(endereco)

if busca:
    cep = busca.group()

    print(cep)
