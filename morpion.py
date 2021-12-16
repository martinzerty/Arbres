class morpio:
    def __init__(self):
        self.plato = []
        self.gen_plato()
        self.print_plato()

    def gen_plato(self):
        self.plato = [list([0,0,0]) for x in range(3)]

    def print_plato(self):
        for x in self.plato:
            for y in x:
                if y == 1:
                    print(" O ", end="")
                elif y == 2:
                    print(" X ", end="")
                else:
                    print(" - ", end="")
            print('')

    def ask_play(self):
        print("Entrez un chiffre en 1 et 9 : ")
        point = eval(input()) - 1
        pos = (point//3, point%3)
        self.plato[pos[0]][pos[1]] = 1
        self.print_plato()

    def 
P = morpio()
P.ask_play()
