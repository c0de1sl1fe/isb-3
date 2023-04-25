import logging
import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def generate_symm_key() -> str:
    """generate 128 bit key"""
    return os.urandom(16)


def encrypt_data(pathToSave: str, pathOfData: str, key) -> None:
    """encrypt and save data"""
    name = os.path.join(pathToSave, 'encryptedData.bin')
    try:
        with open(pathOfData, 'r', encoding='utf-8') as data_in, open(name, 'wb') as data_out:
            text = data_in.read()
            padder = padding.ANSIX923(128).padder()
            text = bytes(text, 'UTF-8')
            padded_text = padder.update(text)+padder.finalize()
            iv = os.urandom(16)
            cipher = Cipher(algorithms.SM4(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            c_text = encryptor.update(padded_text) + encryptor.finalize()
            data_out.write(iv)
            data_out.write(c_text)
        data_in.close
        data_out.close
    except Exception as e:
        logging.error(str(e))
        raise Exception("error")


def decrypt_data(pathToSave: str, pathOfData: str, key) -> None:
    """decrypt and save data"""
    name = os.path.join(pathToSave, 'decryptedData.txt')
    try:
        with open(pathOfData, 'rb') as data_in, open(name, 'w', encoding='utf-8') as data_out:
            iv = data_in.read(16)
            text = data_in.read()
            # iv = os.urandom(16)
            cipher = Cipher(algorithms.SM4(key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            dc_text = decryptor.update(text) + decryptor.finalize()
            unpadder = padding.ANSIX923(128).unpadder()
            unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
            data_out.write(unpadded_dc_text.decode('UTF-8', errors='ignore'))
    except Exception as e:
        logging.error(str(e))
        raise Exception("error")
