def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
    figMaria = 0
    figJoao = 0

    figurinhas_da_maria = list(set(figurinhas_da_maria))
    figurinhas_do_joao = list(set(figurinhas_do_joao))


    for i in range(len(figurinhas_da_maria)):
        for j in range(len(figurinhas_do_joao)):
            if figurinhas_da_maria[i] == figurinhas_do_joao[j]:
                figMaria += 1  


    for k in range(len(figurinhas_do_joao)):
        for l in range(len(figurinhas_da_maria)):
            if figurinhas_do_joao[k] == figurinhas_da_maria[l]:
                figJoao += 1




    if (len(figurinhas_da_maria) - int(figMaria)) < (len(figurinhas_do_joao) - int(figJoao)):
        return print(f"Máximo de figurinhas para troca {len(figurinhas_da_maria) - int(figMaria)}")
    else:
        return print(f"Máximo de figurinhas para troca {len(figurinhas_do_joao) - int(figJoao)}")
        

if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao)


