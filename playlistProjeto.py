#pesquisei num site, e vi que minha logica estava certa, mas tive problemas com indentação
#https://www.online-ide.com/online_python_syntax_checker

#indent-rainbow utilizado para ajudar na indentação


playlist = []
exitConfirm = 0

nomePlaylist = input("Digite o nome para a sua Playlist: ").title()

while(exitConfirm == 0):

    playlistMenu = int(input(f"=== MINHA PLAYLIST: {nomePlaylist} ===\n1 - Adicionar música\n2 - Visualizar playlist\n3 - Pesquisar música na playlist\n4 - Remover uma música que está na playlist\n0 - Sair\nSelecionado: "))

    match playlistMenu:
        case 1:
            musicConfirm = "S"

            while (musicConfirm == "S"):
                cadastroMusicas = input("Digite o nome da música: ")

                if (cadastroMusicas not in playlist):
                    playlist.append(cadastroMusicas)
                    print(f"Música {cadastroMusicas} adicionada a {nomePlaylist} com sucesso!")
                else:
                    print(f"Música {cadastroMusicas} já existe na Playlist.")

                
                musicConfirm = input("Deseja continuar adicionando músicas? S/N: ").upper()
#talvex verificar se a pessoa colocar algo diferente de S ou N...
        case 2:
            print(f"Verificando musicas em{nomePlaylist}...")
            if( len(playlist) == 0 ):
                print(f"Nenhuma musica encontrada em Playlist {nomePlaylist}")
            else:
                (print(f"Musicas encontradas na Playlist:{nomePlaylist}:\n{playlist}: {len(playlist)}"))

        case 3:
            searchMusic = input("Digite a musica que deseja procurar:")
            if (searchMusic not in playlist):
                print(f"Musica {searchMusic} não registrada em {nomePlaylist}.")
            else:
                print(f"Musica {searchMusic} está em {nomePlaylist}.")

        case 4:
            removeToPlaylist = input(f"Digite o nome da musica que deseja remover:\n{playlist}\n :")

            if(removeToPlaylist not in playlist):
                print("Digite uma musica valida!")
            else:
                playlist.remove(removeToPlaylist)
                print(f"Musica {removeToPlaylist} removida com sucesso!")

        case 0:
            confirmQuest = input("Tem certeza que deseja finalizar o programa?S/N: ").upper()
            if(confirmQuest == "S"):
                print("Encerrando o programa...até a nossa próxima playlist!")
                exitConfirm = 1
            elif(confirmQuest == "N"):
                print("Ufa...Voltando para o menu principal...")
            else:
                print("Digite um valor valido")

        case _:
            print("Nenhuma opção das mostradas encontradas!Vontando para o menu...")
