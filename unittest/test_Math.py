from calculator import Math
import unittest

# class Test_StartEnd(unittest.TestCase):
#     def setUp(self):
#         print("test start")
#     def tearDown(self):
#         print("test end")
#
# class Testadd2(Test_StartEnd):
#     def test_add(self):
#         j=Math(5,10)
#         self.assertEqual(j.add(),15)
#         #self.assertEqual(j.add(),12)
#         print("test_add")
#
#
# class Testsub1(Test_StartEnd):
#     def test_sub(self):
#         j=Math(10, 10)
#         self.assertEqual(j.sub(), 0)
#         print("test_sub")

class Lm1(unittest.TestCase):

    def setUp(self):
        print("lm1 start")
    def test_a(self):
        print("test_a")
    def test_b(self):
        print("test_b")
    def tearDown(self):
        print("lm1 end")


class Lm2(unittest.TestCase):

    def setUp(self):
        print("lm2 start")

    def test_d(self):
        print("test_d")

    def test_c(self):
        print("test_c")

    def tearDown(self):
        print("lm2 end")
if __name__=='__main__':
    #unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(Lm2("test_d"))
    # suite.addTest(Lm1("test_b"))
    # suite.addTest(Lm2("test_c"))
    # suite.addTest(Lm1("test_a"))

    # suite=unittest.TestSuite()
    # suite.addTest(TestMath("test_add"))
    # suite.addTest(TestMath("test_sub"))
    #
    # runer=unittest.TextTestRunner()
    # runer.run(suite)
