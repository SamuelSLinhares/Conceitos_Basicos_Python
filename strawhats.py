def trueorfalse(entrada):
    if (entrada in {'s', 'S', 'sim', 'Sim'}):
        return True
    else:
        return False

mais_25 = input('Seu chapéu de palha favorito possui mais que 25 anos? ')

if(trueorfalse(mais_25)):
    homem = input('Ele é homem? ')
    
    if(trueorfalse(homem) == False):
        print('Seu chapéu de palha favorito é a Nico Robin!')
    
    else:
        fruta = input('Seu personagem preferido é usuário de Akuma no Mi? ')
       
        if(trueorfalse(fruta)):
            print('Seu chapéu de palha favorito é o Brook!')
        
        else:
            humano = input('Ele é da raça humana? ')
            
            if(trueorfalse(humano)):
                print('Seu chapéu de palha favorito é o Franky!')
            
            else:
                print('Seu chapéu de palha favorito é o Jimbei!')
else:
    homem = input('Ele é um homem? ')
    
    if(trueorfalse(homem) == False):
        viaja = input('Ela viaja com o bando atualmente? (21/06/2026) ')

        if(trueorfalse(viaja)):
            print('Seu chapéu de palha favorito é a Nami!')
        
        else:
            print('Seu chapéu de palha favorito é Nefertari D. Vivi!')
    
    else:
        fruta = input('Ele é usuário de Akuma no Mi? ')

        if(trueorfalse(fruta)):
            humano = input('Ele nasceu como um ser humano? ')

            if(trueorfalse(humano)):
                print('Seu chapéu de palha favorito é Monkey D. Luffy, o homem que será o Rei dos Piratas!')
            
            else:
                print('Seu chapéu de palha favorito é Tony Tony Chopper!')
        
        else:
            armamento = input('Ele possui Haki do Armamento? ')

            if(trueorfalse(armamento) == False):
                print('Seu chapéu de palha favorito é o Usopp!')

            else:
                rei = input('Ele possui Haki do Rei? ')

                if(trueorfalse(rei)):
                    print('Seu chapéu de palha favorito é Roronoa Zoro!')

                else:
                    print('Seu chapéu de palha favorito é o Sanji!')
