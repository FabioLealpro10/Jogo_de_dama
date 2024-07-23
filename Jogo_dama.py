
class Damas():
    def tela(self,dados):
        print('','='*49)
        print(f' |{"-"*47}|')
        for x,linha in enumerate(dados):
            print(x+1,end='|')
            for coluna in linha:
                print(f'{coluna: ^5}',end='|')
            print()
            print(f' |{"-"*47}|')
        
        print('','='*49)
        print(' ',end=' ')
        for x in range(1,9):
            print(f'{x: ^5}',end=' ')
        print()
            

    def inicializar(self):
        tabu = []
        a = 0
        for linha in range(3):
            pecas = []
            for x in range(8):
                if x%2==a:
                    pecas.append('X')
                else:
                    pecas.append(' ')
            tabu.append(pecas[:])
            if a==0:
                a=1
            else:
                a=0


        for linha in range(2):
            pecas = []
            for x in range(8):
                if x%2==a:
                    pecas.append('O')
                else:
                    pecas.append(' ')
            tabu.append(pecas[:])
            if a==0:
                a=1
            else:
                a=0


        for linha in range(3):
            pecas = []
            for x in range(8):
                if x%2==a:
                    pecas.append('Y')
                else:
                    pecas.append(' ')
            tabu.append(pecas[:])
            if a==0:
                a=1
            else:
                a=0
        return tabu
    

    def casa_valida(self):
        global tabuleiro, jogador
        andamento.tela(tabuleiro)
        print(f'\nJOGADOR {jogador}')
        print('QUAL PEÇA QUER MOVER?\nDigite linha == 99 se deseja Desistir do jogo'.upper())
        linha = int(input('Linha: >> '))-1
        if linha == 98:
            print('Jogo finalizado por desistêcia'.upper())
            return True
        else:
            coluna = int(input('Coluna: >> '))-1
            if 0<=linha<8 and 0<=coluna<8:
                if tabuleiro[linha][coluna]==' ' or tabuleiro[linha][coluna]=='O' or jogador==1 and tabuleiro[linha][coluna]=='Y' or jogador==2 and tabuleiro[linha][coluna]=='X':
                    print('peça invalida. Digite novamente'.upper())
                    andamento.casa_valida()
            else:
                print('Casa invalida. Digite novamente')
                andamento.casa_valida()
            iL= linha
            iC = coluna
            tabuleiro[iL][iC] = 'O'
            while True:
                print('PARA ONDE QUER MOVER ESSA PEÇA ?\nDigite linha = 99 se a peça estiver bloqueada'.upper())
                linha = int(input('Linha: >> '))-1
                if linha ==  98:
                    print('PEÇA BLOQUEADA! REFAÇA A JOGADA')
                    andamento.casa_valida()
                coluna = int(input('Coluna: >> '))-1
                if 0<=linha<8 and 0<=coluna<8:
                    if tabuleiro[linha][coluna]=='O':
                        fL = linha
                        fC = coluna
                        if fL-iL ==2 or iL-fL==2:
                            if iC-fC == 2 or fC-iC==2:
                                if andamento.capiturar_peças(iL,iC,fL,fC):
                                    break
                        if fL-iL ==1 or iL-fL==1:
                            if iC-fC == 1 or fC-iC==1:
                                if jogador == 1 and iL<fL or jogador == 2 and iL>fL:
                                    break

                print('Casa invalida'.upper())
            if jogador==1:
                tabuleiro[linha][coluna] = 'X'
                jogador = 2
            else:
                tabuleiro[linha][coluna] = 'Y'
                jogador = 1
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPeça movida com Suçesso..')
            return False
                


    def capiturar_peças(self,inL,inC,finL,finC):
        if inL< finL:
            if inC<finC:
                if tabuleiro[inL+1][inC+1] != tabuleiro[inL][inC] and tabuleiro[inL+1][inC+1]!='O':
                    tabuleiro[inL+1][inC+1] = 'O'
                    return True
                else:
                    return False
            else:
                if tabuleiro[inL+1][inC-1] != tabuleiro[inL][inC] and tabuleiro[inL+1][inC-1]!='O':
                    tabuleiro[inL+1][inC-1] = 'O'
                    return True
                else:
                    return False
        else:
            if inC<finC:
                if tabuleiro[finL+1][inC+1] != tabuleiro[inL][inC] and tabuleiro[finL+1][inC+1]!='O':
                    tabuleiro[finL+1][inC+1] = 'O'
                    return True
                else:
                    return False
            else:
                if tabuleiro[finL+1][inC-1] != tabuleiro[inL][inC] and tabuleiro[finL+1][inC-1]!='O':
                    tabuleiro[finL+1][inC-1] = 'O'
                    return True
                else:
                    return False


    def fim_de_jogo(self):
            x = 0
            for peça in tabuleiro:
                if 'X' in peça:
                    x+=1
            if x==0:
                print('JOGOADOR 2 VENCEU')
                return True
            
            x = 0
            for peça in tabuleiro:
                if 'Y' in peça:
                    x+=1
            if x==0:
                print('JOGOADOR 1 VENCEU')
                return True
            return False
            
    

    def peca_dama(self):
        pass


jogador = 1
andamento = Damas()
tabuleiro = andamento.inicializar() 
def main():

    andamento = Damas()
    tabuleiro = andamento.inicializar()
    
    while True:
        if andamento.fim_de_jogo() or andamento.casa_valida():
            break
    print('OBRIGADO POR JOGAR')

if'__name___'=='__name___':
    main()
