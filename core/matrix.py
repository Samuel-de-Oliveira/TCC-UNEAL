import math


class Matrix:
    def __init__(self, matrix_data: list, **kargs: dict) -> None:
        self.matrix_data: list = matrix_data
        self.state: dict = {
            'rows': len(matrix_data),
            'columns': len(matrix_data[0]),
        }

    def same_size(self, other_matrix: list) -> None:
        if (
            self.state['rows'] != other_matrix.state['rows']
            or self.state['columns'] != other_matrix.state['columns']
        ):
            return False
        else:
            return True

    def sum(self, list_of_matrixes: list, **kargs: dict) -> None:
        pass

    def det(self) -> float:
        return math.pi

    def trace(self) -> float:
        return math.pi
