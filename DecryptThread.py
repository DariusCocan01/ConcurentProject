import threading

class DecryptThread(threading.Thread):
    def __init__(self, filename, output_filename):
        super().__init__()
        self.filename = filename
        self.output_filename = output_filename
        self.decrypted_content = ""

    def run(self):
        with open(self.filename, 'r') as file:
            encrypted_content = file.read()
            decrypted_content = self.caesar_decrypt(encrypted_content, 8)

        with open(self.output_filename, 'w') as file:
            file.write(decrypted_content)
    def caesar_decrypt(self, text, shift):
        decrypted = ""
        for char in text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                decrypted += chr((ord(char) - offset - shift) % 26 + offset)
            else:
                decrypted += char
        return decrypted
    