import unittest as u

max_integer = __import__("6-max_integer").max_integer
class Test_max_integer(u.TestCase):
    

    def test_None(self):
        # When passing an empty list
        self.assertIs(max_integer([]), None)

    def test_str(self):
        # When passing strings only in the list
        self.assertEqual(max_integer(["Yehia", "Medhat", "Yusuf"]), "Yusuf")
        self.assertEqual(max_integer(["", "Medhat", "Yusuf"]), "Yusuf")
        self.assertEqual(max_integer(["Nehia", "Medhat", "Yusuf"]), "Yusuf")
        self.assertEqual(max_integer(["Yehia", "Zedhat", "Yusuf"]), "Zedhat")
        self.assertEqual(max_integer(["Yehia", "Qedhat", "Zusuf"]), "Zusuf")

    def test_str_int(self):
        # When passing both strings and integers
        self.assertRaises(TypeError, max_integer, [5, "Medhat", "Yusuf"])
        self.assertRaises(TypeError, max_integer, [5, 6, "Yusuf"])
        self.assertRaises(TypeError, max_integer, [10, "Medhat", 55])

    def test_int(self):
        # When passing only integers
        self.assertEqual(max_integer([5, 300, 5000]), 5000)
        self.assertEqual(max_integer([5000, 5, 300]), 5000)
        self.assertEqual(max_integer([5, 5000, 300]), 5000)

    def test_float(self):
        # When passing floats
        self.assertEqual(max_integer([300.0, 300.232, 300.5]), 300.5)
        self.assertEqual(max_integer([300.232, 300.5, 300.0]), 300.5)
        self.assertEqual(max_integer([5.0, 5000, 300.0]), 5000)

    def test_lists(self):
        # When passing lists inside lists containing only numbers
        self.assertEqual(max_integer([[1, 2 ,3], [10, 20, 30], [20, 40, 60]]), [20, 40, 60])
        self.assertEqual(max_integer([[1, 2 ,3], [100, 20, 30], [20, 40, 60]]), [100, 20, 30])
        self.assertEqual(max_integer([[120, 2 ,3], [100, 20, 30], [20, 40, 60]]), [120, 2 ,3])
        self.assertEqual(max_integer([[120, 2 ,3], [100.5, 20, 30], [20, 40, 60.75]]), [120, 2 ,3])
        self.assertEqual(max_integer([[120, 2 ,3], [1000.0, 20, 30], [20, 40, 60]]), [1000.0, 20, 30])
