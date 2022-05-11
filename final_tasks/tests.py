import unittest
from io import StringIO  # для тестирования вывода
from typing import List, Tuple, Callable
from unittest.mock import patch  # для тестирования вывода

from a_nearest_zero import main as main_task_a  # чтобы не было конфликтов


class Sprint12TestCase(unittest.TestCase):
    def _assert_correct_output(
            self,
            subtest_name: str,
            module: str,
            side_effect: List[str],
            test_func: Callable,
            expected_result: str
    ) -> None:
        """Вспомогательный метод для тестирования ввода и вывода.
        Тут мы «мокаем» (Mock):
        - функцию ввода input()
        - вывод stdout.
        """
        with self.subTest(
                name=subtest_name
        ), patch(  # это Mock для функции ввода, мы «подменяем» функцию input
            f'{module}.input', side_effect=side_effect  # здесь передаются входные данные в input()
        ), patch(  # это Mock для вывода stdout, мы «подменяем» вывод
            'sys.stdout', new=StringIO()
        ) as fake_out:
            test_func()  # вызываем тестируемую функцию
            self.assertEqual(
                fake_out.getvalue(),  # тестируем наш «подмененный» вывод
                expected_result
            )

    def test_task_a(self):
        tests: Tuple[Tuple[str, str]] = (
            ('-8 -5 -2 7', '-183'),
            ('8 2 9 -10', '40')
        )

        for inp, res in tests:
            self._assert_correct_output(
                inp, 'task_a', [inp], main_task_a, res
            )


if __name__ == '__main__':
    unittest.main()

"""
python tests.py -k task_a  # так будут запущены 
только тесты, в названии которых есть task_a
"""