import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parâmetros da simulação
L = 50  # Tamanho da grade (LxL)
p_infect = 0.3  # Probabilidade de infecção
p_recover = 0.1  # Probabilidade de recuperação
n_iterations = 100  # Número de iterações

# Estados
SAUDAVEL = 0
INFECTADO = 1
RECUPERADO = 2

# Inicialização da grade
grid = np.zeros((L, L), dtype=int)
grid[L//2, L//2] = INFECTADO  # Inicia com um indivíduo infectado no centro

# Função para atualizar a grade
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(L):
        for j in range(L):
            if grid[i, j] == SAUDAVEL:
                # Verifica vizinhos infectados
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < L and 0 <= nj < L:
                            if grid[ni, nj] == INFECTADO and np.random.rand() < p_infect:
                                new_grid[i, j] = INFECTADO
                                break
            elif grid[i, j] == INFECTADO:
                if np.random.rand() < p_recover:
                    new_grid[i, j] = RECUPERADO
    return new_grid

# Função para animação
def animate(frame):
    global grid
    grid = update_grid(grid)
    im.set_array(grid)
    return im,

# Configuração da animação
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='viridis', vmin=0, vmax=2)
plt.colorbar(im, ticks=[0, 1, 2], label='Estado')
plt.title('Simulação Epidemiológica')

# Cria a animação
ani = animation.FuncAnimation(fig, animate, frames=n_iterations, interval=200, blit=True)

plt.show()