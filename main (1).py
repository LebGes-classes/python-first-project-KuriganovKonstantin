from maze import (
    Maze,
)
from game import(
    Game,
)

def main():
    '''Запуск программы.'''
    is_running = True
    
    while is_running:
        levels = {'0': 0, '1': 7, '2': 9, '3': 11, '4': 15}
        
        difficult = input(
                        '\nВыберите уровень сложности\n'
                        '1) Easy\n'
                        '2) Normal\n'
                        '3) Hard\n'
                        '4) Impossible\n'
                        '\nЕсли хотите выйти, введите 0\n'
                        )
        
        if difficult == '0':
            print('Пока, удачи!')
            break
        
        elif difficult in levels:
            level = levels[difficult]
        else:
            continue
        # Создание лабиринта
        maze = Maze(level)
        maze.maze_start()
        maze.dfs(*maze.get_start())
        maze.generate_exit()
        
        # Запуск игры
        game = Game()
        game.walk(maze)
        
if __name__ == '__main__':
    main()