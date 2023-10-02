import string
import unittest

caracteres = string.ascii_letters + string.digits + string.punctuation + " "

def crypt(message):
    message_crypte = ""
    for char in message:
        if char in caracteres:
            index = caracteres.index(char)
            char_crypte = caracteres[(index + 1) % len(caracteres)]
            message_crypte += char_crypte
        else:
            message_crypte += char
    return message_crypte

def crypter_message_utilisateur():
    message = input("Entrez le message à crypter : ")
    message_crypte = crypt(message)
    print("Message crypté :", message_crypte)

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
    choix = input("Voulez-vous crypter un message ? (oui/non) ")
    if choix.lower() == "oui":
        crypter_message_utilisateur()
    else:
        unittest.main()