import string
import unittest

caracteres = string.ascii_letters + string.digits + string.punctuation + " "

def crypt(message, pas):
    message_crypte = ""
    for char in message:
        if char in caracteres:
            index = caracteres.index(char)
            char_crypte = caracteres[(index + pas) % len(caracteres)]
            message_crypte += char_crypte
        else:
            message_crypte += char
    return message_crypte + str(pas)

def crypter_message_utilisateur():
    message = input("Entrez le message à crypter : ")
    pas = int(input("Entrez le décalage (entier entre 1 et 9) : "))
    if 1 <= pas <= 9:
        message_crypte = crypt(message, pas)
        print("Message crypté :", message_crypte)
    else:
        print("Le décalage doit être un entier entre 1 et 9.")

class TestCrypt(unittest.TestCase):
    def test_crypt_lowercase(self):
        self.assertEqual(crypt("abc", 1), "bcd1")

    def test_crypt_uppercase(self):
        self.assertEqual(crypt("XYZ", 3), "ABC3")

    def test_crypt_mixed_case(self):
        self.assertEqual(crypt("Hello World", 5), "Mjqqt%&qtwhi5")

    def test_crypt_non_alpha_characters(self):
        self.assertEqual(crypt("123!@#", 2), "123!@#2")

if __name__ == '__main__':
    choix = input("Voulez-vous crypter un message ? (oui/non) ")
    if choix.lower() == "oui":
        crypter_message_utilisateur()
    else:
        unittest.main()
