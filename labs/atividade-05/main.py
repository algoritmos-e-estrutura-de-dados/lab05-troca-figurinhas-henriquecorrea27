def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao, A, B):
    figMaria = 0
    figJoao = 0
    i = 0
    j = 0
    k = 0
    l = 0


    for i in range(int(A)):
        for j in range(int(B)):
            if figurinhas_da_maria[i] == figurinhas_do_joao[j]:
                figMaria += 1           
    

    for k in range(int(B)):
        for l in range(int(A)):
            if figurinhas_do_joao[k] == figurinhas_da_maria[l]:
                figJoao += 1


    if (int(A) - int(figMaria)) < (int(B) - int(figJoao)):
        return print(f"Máximo de figurinhas para troca {int(A) - int(figMaria)}")
    else:
        return print(f"Máximo de figurinhas para troca {int(B) - int(figJoao)}")
        

if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao, A, B)


