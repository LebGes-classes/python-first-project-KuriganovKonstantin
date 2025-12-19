from maze import(
    Maze,
)
from view import(
    View,
)
from os import(
    system,
)
class Game:
    """Класс, осуществляющий геймплей"""
    
    def print_maze(self, maze: Maze, simbols: dict) -> None:
        """Метод для вывода красивого лабиринта.
        
        Args:
            maze (Maze): Объект лабиринта.
            simbols (dict): Словарь для преобразования значений в символы.
        """
        
        for line in View(maze).display(simbols):
            print(*line)

    def walk(self, maze: Maze):
        """Метод, который осуществляет передвижение.
        
        Args:
            maze (Maze): Объект лабиринта.
        """
        
        i, j = maze.get_maze_true_start()
        maze_structure = maze.structure

        is_running = True

        while is_running:
            system('clear')
            
            print(
                '\nВыберите действие:\n'
              'W - Наверх\n'
              'S - Вниз\n'
              'D - Вправо\n'
              'A - Налево\n'
              'EXIT - Завершить игру!\n'
              )
            
            self.print_maze(maze, {0: '⬜', 1: '⬛', 2: '😡', 3: '⬛', 4: '⬛'}) # Закрашивание белым цветом клеток, по которым можно пройти

            move = input().lower()

            if move == 'w' and i > 0 and maze_structure[i-1][j] != 1:
                maze_structure[i][j] = 0
                i -= 1
            elif move == 's' and i < maze.get_size()-1 and maze_structure[i+1][j] != 1:
                maze_structure[i][j] = 0
                i += 1
            elif move == 'd' and j < maze.get_size()-1 and maze_structure[i][j+1] != 1:
                maze_structure[i][j] = 0
                j += 1
            elif move == 'a' and j > 0 and maze_structure[i][j-1] != 1:
                maze_structure[i][j] = 0
                j -= 1
            elif move == 'exit':
                system('clear')
                
                print(
                    'Вы проиграли!\n'
                      'Структура лабиринта:'
                      )
                
                self.print_maze(maze, {0: '⬜️', 1: '⬛', 2: '☠️', 3: '🚩', 4: '⬜️'})# Вывод струкуры лабиринта
                
                is_running = False
            
            maze.structure[i][j] = 2
            
            if (i, j) == maze.get_maze_exit():
                system('clear')
                
                print('ПОБЕДА!!!')
                
                self.print_maze(maze, {0: '⬜️', 1: '⬛', 2: '😎', 3: '⬛', 4: '⬛'}) # Последний вывод лабиринта, в случае победы
                
                is_running = False