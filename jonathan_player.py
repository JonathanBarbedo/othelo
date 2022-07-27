class Jonathan:
    import random

    def __init__(self, color):
        self.color = color

    def play(self, board):

        validos = board.valid_moves(self.color)
        validos_sub = [] #lista que armazena subconjuntos de jogadas válidas
        movimento_final = validos[0]
        mov_temp = [0,[0,0]] #[0]determina se movimento será alterado, [1] dermina movimento

        pontos_pro = self.contagem(board)
        pontos_cont = self.contagem_op(board)

        mov_temp = self.canto(validos)
        if(mov_temp[0]==1):
            movimento_final = mov_temp[1]
            mov_temp = self.bordas_boas(validos)
        elif(mov_temp[0]==1):
            movimento_final = mov_temp[1]
        else:
            validos_sub = self.linhas_perigosas(validos) #tira as jogadas nas linhas perigosas
            if pontos_cont/pontos_pro>=2 or pontos_pro+pontos_cont>=32:
                movimento_final = self.mais_pec(board, validos_sub)[1]
            else:
                movimento_final = self.menos_pec(board, validos_sub)[1]
        return movimento_final

    def canto(self, moves):
        movimento = [0,[0,0]]
        validos_sub = []
        for move in moves:
            if ((move.x==1 or move.x==8) and (move.y==1 or move.y==8)):
                movimento[0] = 1
                validos_sub.append(move)
        if movimento[0]==1:
            movimento[1] = self.random.choice(validos_sub)
        return movimento

    def bordas_boas(self, moves):
        movimento = [0,[0,0]]
        validos_sub = []
        for move in moves:
            if ((move.x==1 and move.y==3) or (move.x==1 and move.y==6) or
                (move.x==8 and move.y==3) or (move.x==8 and move.y==6) or
                (move.x==3 and move.y==1) or (move.x==6 and move.y==1) or
                (move.x==3 and move.y==8) or (move.x==6 and move.y==8)):
                movimento[0] = 1
                validos_sub.append(move)
        if movimento[0]==1:
            movimento[1] = self.random.choice(validos_sub)
        return movimento

    #define jogadas pelo menor numero de pecas capturadas
    def menos_pec(self, board, moves):
        movimento = [0,[0,0]]
        contador = 64 #numero de pecas apos a jogada
        for move in moves:
            clone = board.get_clone()
            movimento[1] = move
            clone.play(move, self.color)
            cont_temp = self.contagem(clone)
            if cont_temp < contador:
                contador = cont_temp
        return movimento

    def mais_pec(self, board, moves):
        movimento = [0,[0,0]]
        contador = 64 #numero de pecas apos a jogada
        for move in moves:
            clone = board.get_clone()
            movimento[1] = move
            clone.play(move, self.color)
            cont_temp = self.contagem(clone)
            if cont_temp > contador:
                contador = cont_temp
        return movimento

    def contagem(self, board):
        contador = 0
        if self.color=='white':
            contador = board.score()[0]
        else:
            contador = board.score()[1]
        return contador

    #conta peças do oponente
    def contagem_op(self, board):
        contador = 0
        if self.color=='white':
            contador = board.score()[1]
        else:
            contador = board.score()[0]
        return contador

    def linhas_perigosas(self, moves):
        validos_sub = []
        for move in moves:
            if move.x != 2 and move.x != 7 and move.y != 2 and move.y != 7:
                validos_sub.append(move)
        if len(validos_sub)==0:
            validos_sub=moves
        return validos_sub
