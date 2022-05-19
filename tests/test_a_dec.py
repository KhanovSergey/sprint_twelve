import unittest

from final_tasks.a_dec import Dek


class StackTester(unittest.TestCase):

    # def test_dack_init(self):
    #     d = Dek(max_size=4)
    #     print(d)
    #     #self.max_size = 0
    #     print(self.size())
    #     self.assertEqual(4, self.size())

    def test_isEmpty_init(self):
        d = Dek(max_size=4)
        self.assertEqual(True, d.is_empty())

    def test_push_back(self):
        value = 4
        d = Dek(value)
        d.push_back(value)
        self.assertEqual(1, d._size)

    def test_push_pop(self):
        d = Dek(max_size=4)
        d.push_front(861)
        d.push_front(-819)
        d.pop_back()
        self.assertEqual(1, d._size)
        self.assertEqual(-819, d.pop_back())

    def test_push_pop_exp(self):
        d = Dek(max_size=4)
        d.push_front(861)
        d.push_front(-819)
        self.assertEqual(861, d.pop_back())
        self.assertEqual(-819, d.pop_back())
        self.assertEqual(0, d._size)

    def test_push_back(self):
        d = Dek(max_size=0)
        d.push_front(861)
        #d.push_front(-819)
        self.assertEqual(861, d.pop_back())
        self.assertEqual(-819, d.pop_back())
        self.assertEqual(0, d._size)

    def test_push_front(self):
        d = Dek(max_size=1)
        d.push_front(861)
        d.push_front(-819)
        self.assertEqual(861, d.pop_back())
        self.assertEqual(-819, d.pop_back())
        #self.assertEqual(0, d._size)

    def test_pop_back(self):
        d = Dek(max_size=1)
        d.push_front(861)
        # d.push_front(-819)
        self.assertEqual(861, d.pop_back())
        d.pop_back()
        #self.assertEqual(-819, d.pop_back())
        #self.assertEqual(0, d._size)

    # def test_push1_items(self):
    #     s = Dek()
    #     s.push(5)
    #     self.assertEqual([5], s.items)
    #
    # def test_push2_size(self):
    #     s = Dek()
    #     s.push(5)
    #     s.push(6)
    #     self.assertEqual(2, s.size())
    #
    # def test_push2_items(self):
    #     s = Dek()
    #     s.push(5)
    #     s.push(6)
    #     self.assertEqual([5, 6], s.items)
    #
    # def test_push2_pop1_size(self):
    #     s = Dek()
    #     s.push(5)
    #     s.push(6)
    #     s.pop()
    #     self.assertEqual(1, s.size())
    #
    # def test_push2_pop1_value(self):
    #     s = Dek()
    #     s.push(8)
    #     s.push(9)
    #     self.assertEqual(9, s.pop())
    #
    # def test_push2_pop2_size(self):
    #     s = Dek()
    #     s.push("Glob")
    #     s.push("Blob")
    #     s.pop()
    #     s.pop()
    #     self.assertEqual(0, s.size())
    #
    # def test_push2_pop2_value(self):
    #     s = Dek()
    #     s.push("Glob")
    #     s.push("Blob")
    #     s.pop()
    #     self.assertEqual("Glob", s.pop())
    #

    #
    # def test_isEmpty_push1(self):
    #     s = Dek()
    #     s.push(5)
    #     self.assertEqual(False, s.isEmpty())
    #
    # def test_isEmpty_push1_pop1(self):
    #     s = Dek()
    #     s.push(1)
    #     s.pop()
    #     self.assertEqual(True, s.isEmpty())
    #
    # def test_peek_push1(self):
    #     s = Dek()
    #     s.push(88)
    #     self.assertEqual(88, s.peek())
    #
    # def test_peek_push3_pop1(self):
    #     s = Dek()
    #     s.push(7)
    #     s.push(889)
    #     s.push(3)
    #     s.pop()
    #     self.assertEqual(889, s.peek())
    #
    # def test_pop_empty(self):
    #     s = Dek()
    #     self.assertRaises(IndexError, s.pop)
    #
    # def test_peek_empty(self):
    #     s = Dek()
    #     self.assertRaises(IndexError, s.peek)


if __name__ == '__main__':
    unittest.main()
