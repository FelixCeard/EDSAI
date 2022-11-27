import unittest

        
class MRUBufferTest(unittest.TestCase):
    def test_load(self):
        buf = MRUBuffer(3)
        buf.load(2)
        buf.load(5)
        self.assertListEqual(buf.buffer, [2, 5])
   
    def test_load_evict(self):
        buf = MRUBuffer(3)
        buf.load(2)
        buf.load(5)
        buf.load(3)
        buf.load(4)
        self.assertListEqual(buf.buffer, [2,5,4])
    
    def test_get(self):
        buf = MRUBuffer(3)
        buf.load(7)
        elem = buf.get(0)
        self.assertEqual(elem, 7)
        buf.load(3)
        buf.load(2)
        elem = buf.get(1)
        self.assertEqual(elem, 3)
        self.assertListEqual(buf.buffer, [7,2,3])

    def test_evict(self):
        buf = MRUBuffer(3)
        buf.load(7)
        first_element = buf.get(0)
        self.assertEqual(first_element, 7)
        buf.load(3)
        buf.load(2)
        second_element = buf.get(1)
        self.assertEqual(second_element, 3)
        buf.evict()
        self.assertListEqual(buf.buffer, [7,2])
        third_element = buf.get(1)
        self.assertEqual(third_element, 2) 
        self.assertListEqual(buf.buffer, [7,2])
        buf.evict()
        self.assertListEqual(buf.buffer, [7])