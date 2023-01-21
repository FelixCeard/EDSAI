import unittest

class Interface_Test(unittest.TestCase):
    def test_blank_not_terminal(self):
        state = State('X', [
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_']
        ])
        
        self.assertEqual(terminal_test(state), None)
        
    def test_one_mark_not_terminal(self):
        state = State('O', [
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', 'X'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_']
        ])
        
        self.assertEqual(terminal_test(state), None)
        
    def test_three_marks_not_terminal(self):
        state = State('O', [
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', 'X'],
            ['_', '_', '_', '_', '_', 'O'],
            ['_', '_', '_', '_', '_', 'X'],
            ['_', '_', '_', '_', '_', '_']
        ])
        
        self.assertEqual(terminal_test(state), None)
        
    def test_incomplete_max_wins_horizontal(self):
        state = State('O', [
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', 'O', 'O', 'O'],
            ['_', '_', '_', '_', '_', 'X'],
            ['_', '_', '_', '_', '_', 'X'],
            ['_', '_', '_', '_', '_', 'X'],
            ['_', '_', '_', '_', '_', 'X']
        ])
        
        self.assertEqual(terminal_test(state), 100)

    def test_incomplete_max_wins_vertical(self):
        state = State('O', [
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', 'O', 'O', 'O'],
            ['_', '_', 'X', 'X', 'X', 'X'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_']
        ])
        
        self.assertEqual(terminal_test(state), 100)

    def test_incomplete_max_wins_diagonal(self):
        state = State('O', [
            ['_', '_', '_', '_', 'X', 'X'],
            ['_', '_', '_', 'O', 'X', 'O'],
            ['_', '_', 'X', 'X', 'O', 'O'],
            ['_', '_', 'X', 'O', 'X', 'O'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_']
        ])
        
        self.assertEqual(terminal_test(state), 100)
        
    def test_incomplete_min_wins_vertical(self):
        state = State('X', [
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', 'X', 'X', 'X'],
            ['_', 'O', 'O', 'O', 'O', 'X']
        ])
        
        self.assertEqual(terminal_test(state), -100)

    def test_incomplete_min_wins_horizontal(self):
        state = State('X', [
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', 'O'],
            ['_', '_', '_', '_', '_', 'O'],
            ['_', '_', '_', '_', '_', 'O'],
            ['_', '_', '_', '_', 'X', 'O'],
            ['_', '_', '_', 'X', 'X', 'X']
        ])
        
        self.assertEqual(terminal_test(state), -100)

    def test_incomplete_min_wins_diagonal(self):
        state = State('X', [
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', 'O', '_'],
            ['_', '_', '_', 'O', 'X', '_'],
            ['_', '_', 'O', 'X', 'O', '_'],
            ['_', 'O', 'X', 'X', 'X', '_']
        ])

        state = State('X', [
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', 'O'],
            ['_', '_', '_', '_', 'O', 'X'],
            ['_', '_', '_', 'O', 'X', 'X'],
            ['_', '_', 'O', 'X', 'O', 'X'],
            ['_', '_', '_', 'O', '_', '_']
        ])
        
        self.assertEqual(terminal_test(state), -100)
        
    def test_complete_min_wins(self):
        state = State('O', [
            ['X', 'X', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'O', 'X', 'X', 'O'],
            ['O', 'X', 'O', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'O', 'O', 'X'],
            ['X', 'O', 'X', 'X', 'X', 'O'],
            ['X', 'O', 'X', 'O', 'O', 'X']
        ])
        
        self.assertEqual(terminal_test(state), -100)
        
    def test_draw(self):
        state = State('O', [
            ['O', 'X', 'O', 'X', 'O', 'O'],
            ['O', 'X', 'O', 'X', 'O', 'O'],
            ['O', 'X', 'O', 'X', 'O', 'O'],
            ['X', 'O', 'X', 'O', 'X', 'X'],
            ['X', 'O', 'X', 'O', 'X', 'X'],
            ['X', 'O', 'X', 'O', 'X', 'X']
        ])
        
        self.assertEqual(terminal_test(state), 0)

class Minimax_Test(unittest.TestCase):
    def test_minimax_obvious_min_can_win(self):
        state = State('O', [
            ['_', 'O', 'O', 'X', 'X', 'X'],
            ['O', 'X', 'X', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'X', 'X', 'X'],
            ['_', 'X', 'X', 'O', 'X', 'O'],
            ['O', 'X', 'O', 'O', 'X', 'O'],
            ['_', 'O', 'X', 'X', 'O', 'X']
        ])
        
        v, a = Min_Value_Decision(state)
        
        self.assertEqual(v, -100)
        self.assertEqual(a, 3)

    def test_minimax_obvious_max_always_loses(self):
        state = State('X', [
            ['_', 'O', 'O', 'X', 'X', 'X'],
            ['_', 'X', 'X', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'X', 'X', 'X'],
            ['O', 'X', 'O', 'O', 'O', 'X'],
            ['O', 'X', 'O', 'X', 'X', 'O'],
            ['_', 'O', 'X', 'X', 'O', 'X']
        ])
        
        v, a = Max_Value_Decision(state)
        
        self.assertEqual(v, -100)
        
    def test_minimax_draw_if_perfect_play(self):
        state = State('O', [
            ['_', '_', 'O', 'X', 'X', 'X'],
            ['_', 'X', 'X', 'O', 'O', 'O'],
            ['_', 'O', 'O', 'X', 'X', 'X'],
            ['_', '_', 'X', 'O', 'X', 'O'],
            ['_', '_', 'O', 'O', 'X', 'O'],
            ['_', 'O', 'X', 'X', 'O', 'X']
        ])
        
        v, a = Min_Value_Decision(state)
        
        self.assertEqual(v, 0)
        self.assertEqual(a, 0)

    def test_minimax_min_can_win(self):
        state = State('X', [
            ['_', 'X', 'O', 'X', 'X', 'X'],
            ['_', 'O', 'O', 'X', 'O', 'X'],
            ['_', '_', 'O', 'X', 'X', 'X'],
            ['_', '_', 'X', 'O', 'X', 'O'],
            ['_', 'O', 'O', 'O', 'X', 'X'],
            ['_', 'O', 'X', 'O', 'O', 'X']
        ])
        
        v, a = Max_Value_Decision(state)
        
        self.assertEqual(v, -100)

    def test_minimax_max_can_win(self):
        state = State('X', [
            ['_', '_', 'O', 'X', 'X', 'X'],
            ['_', 'X', 'X', 'O', 'O', 'O'],
            ['_', 'O', 'O', 'X', 'X', 'X'],
            ['_', '_', 'X', 'O', 'X', 'O'],
            ['_', '_', 'O', 'O', 'X', 'O'],
            ['_', 'O', 'X', 'X', 'O', 'X']
        ])
        
        v, a = Max_Value_Decision(state)
        
        self.assertEqual(v, 100)