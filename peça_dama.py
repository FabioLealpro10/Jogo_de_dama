
def criar_tabuleiro():
    tabuleiro = [[],[],[],[],[],[],[],[]]
    for linha in range(8):
        if linha%2==0: # linha Pa
            for coluna in range(8):
                if coluna%2==0:
                    tabuleiro[linha].append('_')
                else:
                    tabuleiro[linha].append(' ')
        else: # linha Impa
            for coluna in range(8):
                if coluna%2==0:
                    tabuleiro[linha].append(' ')
                else:
                    tabuleiro[linha].append('_')
    return tabuleiro

def mostra_tabuleiro(tabuleiro):
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('  ',end='')
    for cont in range(1,9):
        print(f' {cont} ',end='')
    print('\n ','-'*24)
    for cont,linha in enumerate(tabuleiro):
        print(f'{cont+1}|',end='')
        for coluna in linha:
            print(f' {coluna} ',end='')
        print('|')
    print(' ','-'*24)

def possives_movimentos(plinha,pcoluna):
    tabu = criar_tabuleiro()
    diagonais_abaixo = plinha-pcoluna #  2 4 6
    if 0>=diagonais_abaixo:
        l_ID = plinha - pcoluna if plinha>=pcoluna else pcoluna - plinha # começo da diagonal 1
    else:
        lina_ZB = diagonais_abaixo# começo da diagonal 1
        coluna_ZB = 0
    l_ED = plinha + pcoluna # começo da diagonal 2
    l_mP = plinha+1
    c_E = pcoluna-1
    c_D = pcoluna+1
    for linha in range(8):
        for coluna in range(8):
            if linha == plinha and coluna==pcoluna:
                tabu[linha][coluna] = 'D'
            elif l_mP<=linha:
                if c_D==coluna :
                    tabu[linha][coluna] = 'X'
                elif c_E==coluna:
                    tabu[linha][coluna]='X'
            elif l_mP>linha:
                if 0>=diagonais_abaixo:
                    if l_ID==coluna:
                            tabu[linha][coluna] = 'X'
                else:
                    if linha == lina_ZB and coluna_ZB==coluna:
                        tabu[linha][coluna] = 'X'
                        lina_ZB+=1
                        coluna_ZB+=1
                if l_ED==coluna:
                    tabu[linha][coluna] = 'X'
        if l_mP<=linha:
            l_mP+=1
            c_D+=1
            c_E-=1
        else:
            if 0>=diagonais_abaixo:
                l_ID+=1
            l_ED-=1
    return tabu


from time import sleep    
while True:
    tabuleiro = criar_tabuleiro()
    mostra_tabuleiro(tabuleiro)
    while True:
        try:
            linha = int(input('Linha: '))-1
            coluna = int(input('Coluna: '))-1
            if tabuleiro[linha][coluna]=='_':
                break
            else:
                print('\33[31mLocalizações Invalidas.Digite novamente.\33[m')# erro de localização
        except:
            print('\33[31mLocalizações Invalidas.Digite novamente.\33[m')# erro de digitação
    print('Movimentos possives..')
    sleep(1)
    print()
    mostra_tabuleiro(possives_movimentos(linha,coluna))
    sleep(10)
   



