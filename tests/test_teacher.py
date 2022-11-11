mport unittest
from source_code.app import user


class user_test_sheet(unittest.TestCase):
    def setUp(self):
        self.user1 = user.Teacher(user_id="001", name="Alex", email="alex@bu.com",password = 123456)


    def test01_ID(self):
        self.assertEqual(self.user1.get_ID(), "001")


    def test02_name_PT_1(self):
        self.assertEqual(self.user1.get_name().lower(), "Alex".lower())


    def test03_name_PT_2(self):
        self.assertTrue(self.user1.get_name() == "Alex")


    def test04_password(self):
        self.assertEqual(self.user1.get_passworld(),  password = 123456)



if __name__ == '__main__':
    unittest.main()