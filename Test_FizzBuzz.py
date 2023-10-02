import unittest

def crypt(message):
    message_list = list(message)

    for i in range(len(message_list)):
        char = message_list[i]
        if char.isalpha():
            new_char = chr(ord(char) + 1)
            message_list[i] = new_char

    encrypted_message = ''.join(message_list)
    return encrypted_message

class TestCrypt(unittest.TestCase):
    def test_crypt_lowercase(self):
        self.assertEqual(crypt("abc"), "bcd")

    def test_crypt_uppercase(self):
        self.assertEqual(crypt("XYZ"), "YZA")

    def test_crypt_mixed_case(self):
        self.assertEqual(crypt("Hello World"), "Ifmmp Xpsme")

    def test_crypt_non_alpha_characters(self):
        self.assertEqual(crypt("123!@#"), "123!@#")

if __name__ == '__main__':
    unittest.main()