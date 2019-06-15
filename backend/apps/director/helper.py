import string

class CustomHasher:
    """
    Custom Base62 Hasher, takes string to hash as input and return
    """
    def __init__(self, hash_or_key):
        self.hash_or_key = hash_or_key
        self.base_list = string.digits + string.ascii_letters


    def encode(self):
        if self.hash_or_key == 0:
            return self.base_list[0]
        encoded_letters = []
        base_length = len(self.base_list)
        hash_iter = self.hash_or_key
        while hash_iter:
            hash_iter, remainder = divmod(hash_iter, base_length)
            encoded_letters.append(self.base_list[remainder])
        encoded_letters.reverse()
        return ''.join(encoded_letters)


    def decode(self):
        base_length = len(self.base_list)
        hash_or_key_length = len(self.hash_or_key)
        decoded_number = 0

        idx = 0
        for char in self.hash_or_key:
            power = (hash_or_key_length - (idx + 1))
            decoded_number += alphabet.index(char) * (base_length ** power)
            idx += 1

        return decoded_number

