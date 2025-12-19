from maze import (
    Maze,
)


class View:
    """Класс для красивого отображения лабиринта."""
    def __init__(self, maze: Maze) -> None:
        """Инициализация объекта View.
        
        Args:
            maze (Maze): Объект лабиринта.
        """
        self.maze = maze.structure

    def display(self, simbols: dict):
        '''
        Метод для преобразования чисел из лабиринта в понятные для пользователя символы.
        
        Args:
            simbols (dict): Словарь для преобразования чисел в символы.
        
        Returns:
            list: Двумерный список символов.
        '''
        maze_map = []
        
        for i in range(len(self.maze)):
            line = []
            
            for j in range(len(self.maze)):
                value = self.maze[i][j]
                line.append(simbols[value])
                
            maze_map.append(line)

        return maze_map