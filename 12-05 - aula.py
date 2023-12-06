from pyamaze import maze, agent, textLabel

labirinto = maze()

labirinto.CreateMaze(loadMaze="maze--2023-11-30--13-28-44.csv")
# labirinto.CreateMaze()
# celulas = labirinto.grid
# print(celulas)

# mapa = labirinto.maze_map
# print(mapa)

# caminho = labirinto.path
# print(caminho)

agente = agent(labirinto, footprints=True, filled=True)
# caminho = {(10, 10): (10, 9), (10, 9): (10, 8), (10, 8): (9, 8)}
caminho = "NWNWNWN"
labirinto.tracePath({agente: caminho}, delay=600)
# posicao = agente.position
# print(posicao)

texto = textLabel(labirinto, title="Nº passos", value=len(caminho))
labirinto.run()