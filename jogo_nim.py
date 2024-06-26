import random

def imprimir_pilhas(pilhas):
	for i, pilha in enumerate(pilhas):
		print(f"pilha {i}: {'*' * pilha} objetos")
		

def obter_movimento_jogador(pilhas):
	while True:
		try:
			indice_pilha = int(input("Escolha o indice da pilha: "))
			if indice_pilha < 0 or indice_pilha >= len(pilhas) or pilhas[indice_pilha] == 0:
				print("Escolha inválida, tente novamente!")
				continue
			objetos_para_remover = int(input("Escolha o numero de objetos a remover: "))
			if objetos_para_remover <= 0 or objetos_para_remover > pilhas[indice_pilha]:
				print("Escolha de objetos incorreta, tente novamente! ")
				continue
			return indice_pilha, objetos_para_remover
		except ValueError:
				print("Entrada invalida, tente novamente! ")
			
			
def obter_movimento_computador(pilhas):
	pilhas_nao_vazias = [i for i in range(len(pilhas)) if pilhas[i] > 0]
	indice_pilha = random.choice(pilhas_nao_vazias)
	objetos_para_remover = random.randint(1, pilhas[indice_pilha])
	print(f"Compurador escolher remover {objetos_para_remover} objetos da pilha {indice_pilha}")
	return indice_pilha, objetos_para_remover
	

def jogar_nim():
	pilhas = [3, 4, 5]
	turno_jogador = True
	
	while any(pilhas):
		print("\nPilhas:")
		imprimir_pilhas(pilhas)
	
		if turno_jogador:
			print("Sua vez:")
			indice_pilha, objetos_para_remover = obter_movimento_jogador(pilhas)
		else:
			print("Vez do computador:")
			indice_pilha, objetos_para_remover = obter_movimento_computador(pilhas)
	
		pilhas[indice_pilha] -= objetos_para_remover
		turno_jogador = not turno_jogador
		
	if turno_jogador:
		print("O computador ganhou!")
	else:
		print("Você ganhou!")
		
jogar_nim()
			
		
		