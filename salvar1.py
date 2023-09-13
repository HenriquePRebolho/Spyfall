import random

player = random.randint(4, 8)
# print(player)

jogadores = {
    "Escola": ["Professor(a)", "Aluno bom", "Faxineira(o)", "Diretor(a)", "Secretário(a)", "Cordenador(a)", "Segurança",
               "Repetente"],
    "Praia": ['Salva-vidas', 'Praiador(a)', 'Surfista', 'Jogador(a) de vôlei', 'Nadador(a)', 'Pescador(a)',
              'Marinheiro(a)', 'Camelô'],
    "Teatro": ['Ator/Atriz', "Diretor(a)", "Telespectador", "Faxineiro", "Maquiador", "Avaliador", "Bilheteiro",
               "Estilista"],
    "Cassino": ["Segurança", "Jogador rico", "Caixa", "Faxineiro", "Gerente", "Barman", "Jogador pobre", "Mordomo"],
    "Circo": ["Plateia", "Palhaço", "Diretor", "Faxineira", "Malabarista", "Mágico", "Engolidor de espada",
              "Trapezista"],
    "Banco": ["Estagiário", "Gerente", "Caixa", "Pobre", "Segurança", "Faxineiro", "Atendente comercial", "Assaltante"],
    "Hotel": ["Camareiro", "Recepcionista", "Cozinheiro", "Barman", "Mordomo", "Garçom", "Gerente", "Hóspede"]}

lugar = random.choice(list(jogadores.items()))
print(lugar[0])

profissoes = []

prof1 = lugar[1]

for i in prof1:
    profissoes.append(i)

# print(profissoes)

lista = []

while len(lista) < player:
    prof = random.choice(profissoes)
    lista.append(prof)
    profissoes.remove(prof)

    if len(lista) == player:
        # por algum motivo sem o pop() a lista vem com um item a mais do que deveria
        lista.pop()
        break

s = random.randint(0, len(lista))
lista.insert(s, "Espião")

print(lista)
