playlist = []
exitConfirm = 0

nomePlaylist = input("Digite o nome para a sua Playlist: ").title()

while(exitConfirm == 0):

    playlistMenu = int(input(f"=== MINHA PLAYLIST: {nomePlaylist} ===\n1 - Adicionar música\n2 - Visualizar playlist\n3 - Ver quantidade de músicas\n4 - Verificar se uma música está na playlist\n5 - Remover música\n0 - Sair\nSelecionado: "))

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
            if searchMusic not in playlist:
                print(f"Musica {searchMusic} não registrada em {nomePlaylist}.")
            else:
                print(f"Musica {searchMusic} está em {nomePlaylist}.")

        case 4:
            next

        case _:
            print("Nenhuma opção das mostradas encontradas!")