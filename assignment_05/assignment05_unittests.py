import unittest
import numpy as np

class AddNodeTest(unittest.TestCase):
    
    def test_forward(self):
        test_add = AddNode()
        x, y = np.random.randint(10, 20, 2)
        print("Testing equality of test_add.forward({0}, {1}) and {0}+{1}...".format(x, y))
        self.assertEqual(test_add.forward(x, y), x + y)
        print("Equality holds.")
    
    def test_backward(self):
        x, y = np.random.randint(10, 20, 2)
        test_add = AddNode()
        print("Testing backward pass of test_add...".format(x, y))
        test_add.forward(x, y)
        self.assertEqual(test_add.backward(1), (1, 1))
        print("Equality holds.")

class MulNodeTest(unittest.TestCase):
    
    def test_forward(self):
        test_mul = MulNode()
        x, y = np.random.randint(10, 20, 2)
        print("Testing equality of test_mul.forward({0}, {1}) and {0}*{1}...".format(x, y))
        self.assertEqual(test_mul.forward(x, y), x * y)
        print("Equality holds.")
    
    def test_backward(self):
        test_mul = MulNode()
        x, y = np.random.randint(10, 20, 2)
        print("Testing backward pass of test_mul...".format(x, y))
        test_mul.forward(x, y)
        self.assertEqual(test_mul.backward(1), (y, x))
        print("Equality holds.")

class SquareNodeTest(unittest.TestCase):
    
    def test_forward(self):
        test_square = SquareNode()
        x = np.random.randint(10, 20)
        print("Testing equality of test_square.forward({0}) and {0}^2...".format(x))
        self.assertEqual(test_square.forward(x), x**2)
        print("Equality holds.")
    
    def test_backward(self):
        test_square = SquareNode()
        x = np.random.randint(10, 20, 1)
        print("Testing backward pass of test_square...".format(x))
        test_square.forward(x)
        self.assertEqual(test_square.backward(1), (2*x))
        print("Equality holds.")
    

class SquareRootNodeTest(unittest.TestCase):
    
    def test_forward(self):
        test_squareroot = SquareRootNode()
        x = np.random.randint(10, 20, 1)
        print("Testing equality of test_squareroot.forward({0}) and {0}^0.5 ...".format(x))
        self.assertEqual(test_squareroot.forward(x), np.sqrt(x))
        print("Equality holds.")
    
    def test_backward(self):
        test_squareroot = SquareRootNode()
        x = np.random.randint(10, 20, 1)
        print("Testing backward pass of test_squareroot...".format(x))
        test_squareroot.forward(x)
        self.assertEqual(test_squareroot.backward(1), (0.5 / np.sqrt(x)))
        print("Equality holds.")
    

class SinusNodeTest(unittest.TestCase):
    
    def test_forward(self):
        test_sinus = SinusNode()
        x = np.random.randint(10, 20, 1)
        print("Testing equality of test_sinus.forward({0}) and sinus({0})...".format(x))
        self.assertEqual(test_sinus.forward(x), np.sin(x))
        print("Equality holds.")
    
    def test_backward(self):
        test_sinus = SinusNode()
        x = np.random.randint(10, 20, 1)
        print("Testing backward pass of test_sinus...".format(x))
        test_sinus.forward(x)
        self.assertEqual(test_sinus.backward(1), np.cos(x))
        print("Equality holds.")

        
class GraphTest(unittest.TestCase):
    
    def test_forward(self):
        print("Testing equality of graph_forward and analytical solution...".format(x))
        self.assertTrue(np.allclose(graph_forward(x, y, w1, w2), f(x, y, w1, w2)))
        print("Equality holds.")
    
    def test_backward(self):
        print("Testing equality of graph_backward and analytical solution...".format(x))
        grad_wrt_w1, grad_wrt_w2 = graph_backward()
        self.assertTrue(np.allclose(grad_wrt_w1, analytical_grad_wrt_w1(x, y, w1, w2)))
        self.assertTrue(np.allclose(grad_wrt_w2, analytical_grad_wrt_w2(x, y, w1, w2)))
        print("Equality holds.")
