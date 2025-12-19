import random


class Maze:
    """Класс для генерации структуры лабиринта"""
    
    def __init__(self, size: int) -> None:
        """Инициализация объекта лабиринта.
        
        Args:
            size (int): Размер лабиринта.
        """
        self.structure = [[1] * size for _ in range(size)]
        self.__size = size
        self.generate_random_start() # Старт вне границ для корректной работы генерации лабиринта
        self.border()
        self.__true_start = None # Вход на границе для корректного отображения
        self.__exit = None

    def border(self) -> None:
        """Генерация границ лабиринта"""
        
        for i in range(self.__size):
            self.structure[0][i] = 1
            self.structure[self.__size-1][0] = 1
            self.structure[i][0] = 1
            self.structure[self.__size-1][i] = 1

    def generate_random_start(self) -> tuple:
        """Выбор случайного старта."""
        
        side = random.choice(['top', 'bottom', 'left', 'right'])
        self.start_side = side
        lst_pos = list(range(1, self.__size-1, 2))

        if side == 'top':
            self.__start = (1, random.choice(lst_pos))
        elif side == 'bottom':
            self.__start = (self.__size-2, random.choice(lst_pos))
        elif side == 'left':
            self.__start = (random.choice(lst_pos), 1)
        else:
            self.__start = (random.choice(lst_pos), self.__size-2)

    def dfs(self, coord_i: int, coord_j: int) -> None:
        """Генерация лабиринта алгоритмом поиска в глубину.
        
        Args:
            coord_i (int): Начальная координата строки.
            coord_j (int): Начальная координата столбца.
        """
        self.structure[coord_i][coord_j] = 4

        moves = [(2, 0), (0, 2), (-2, 0), (0, -2)]
        random.shuffle(moves)  # Перемешивание элементов случайным образом

        for i, j in moves:
            new_i, new_j = coord_i + i, coord_j + j

            if (0 <= new_i < self.__size) and (0 <= new_j < self.__size) and (self.structure[new_i][new_j] == 1):
                self.structure[coord_i + i//2][coord_j + j//2] = 4

                self.dfs(new_i, new_j)

    def maze_start(self) -> None:
        """Определение точки появления игрока на границе"""
        i, j = self.__start
        if self.start_side == 'top':
            i -= 1
            self.structure[i][j] = 2
        elif self.start_side == 'bottom':
            i += 1
            self.structure[i][j] = 2
        elif self.start_side == 'right':
            j += 1
            self.structure[i][j] = 2
        else:
            j -= 1
            self.structure[i][j] = 2

        self.__true_start = i, j

    def generate_exit(self) -> None:
        """Генерация корректного выхода."""
        sides = ['top', 'bottom', 'left', 'right']
        side = random.choice([x for x in sides if x != self.start_side])

        if side == 'top':
            i, j = 0, random.randrange(1, self.__size - 1, 2)
            inner = (1, j)
        elif side == 'bottom':
            i, j = self.__size-1, random.randrange(1, self.__size - 1, 2)
            inner = (self.__size-2, j)
        elif side == 'left':
            i, j = random.randrange(1, self.__size-1, 2), 0
            inner = (i, 1)
        elif side == 'right':
            i, j = random.randrange(1, self.__size-1, 2), self.__size-1
            inner = (i, self.__size-2)

        self.structure[inner[0]][inner[1]] = 4
        self.structure[i][j] = 3
        self.__exit = (i, j)

    def get_maze_exit(self) -> tuple:
        """Геттер.
        
        Returns:
            exit: Координаты выхода.
        """
        return self.__exit

    def get_start(self) -> tuple:
        """Геттер.
        
        Returns:
            start: Координаты старта.
        """
        return self.__start

    def get_size(self) -> int:
        """Геттер.
        
        Returns:
            size: Размер лабиринта.
        """
        return self.__size

    def get_maze_true_start(self) -> tuple:
        """Геттер.
        
        Returns:
            true_start: Координаты входа.
        """
        return self.__true_start