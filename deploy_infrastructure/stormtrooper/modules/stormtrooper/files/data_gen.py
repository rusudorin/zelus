# generate random data
import random
import string


def generate_str(nb):
    generated_str = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
                            for _ in range(nb))
    return generated_str
