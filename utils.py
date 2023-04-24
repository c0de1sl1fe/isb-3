from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives.asymmetric import padding as padding1
from cryptography.hazmat.primitives import padding
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


# 1.1


def generateSymmKey() -> str:
    # return os.urandom(16)
    return os.urandom(16)

# 1.2


def generateAssymKeys():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)

# 1.3


def saveAssymKeys(pathOfPublic: str, pathOfPrivate: str, publicKey: rsa.RSAPublicKey, privateKey: rsa.RSAPrivateKey) -> None:
    public_pem = os.path.join(pathOfPublic, 'public.pem')
    with open(public_pem, 'wb') as public_out:
        public_out.write(publicKey.public_bytes(encoding=serialization.Encoding.PEM,
                                                format=serialization.PublicFormat.SubjectPublicKeyInfo))
    public_out.close
    private_pem = os.path.join(pathOfPrivate, 'private.pem')
    with open(private_pem, 'wb') as private_out:
        private_out.write(privateKey.private_bytes(encoding=serialization.Encoding.PEM,
                                                   format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                   encryption_algorithm=serialization.NoEncryption()))
    private_out.close

# 1.4


def saveSymmKey(pathOfKey: str, publicKey: rsa.RSAPublicKey, symmKey: str):
    name = os.path.join(pathOfKey, "symm.bin")
    c_text = publicKey.encrypt(symmKey, padding1.OAEP(mgf=padding1.MGF1(
        algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    with open(name, 'wb') as symm_out:
        symm_out.write(c_text)
    symm_out.close

# 2.1 and 3.1


def loadAndDecryptSymmKey(pathOfKey: str, pathOfPrivateKey: str):
    dc_text = ''
    privateKey = 0
    with open(pathOfKey, 'rb') as symm_in, open(pathOfPrivateKey, 'rb') as private_in:
        privateKey = private_in.read()
        privateKey = load_pem_private_key(privateKey, password=None)
        dc_text = symm_in.read()
    return privateKey.decrypt(dc_text, padding1.OAEP(mgf=padding1.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

# 2.2


def encryptData(pathToSave: str, pathOfData: str, key):
    name = os.path.join(pathToSave, 'encryptedData.bin')
    with open(pathOfData, 'r', encoding='utf-8') as data_in, open(name, 'wb') as data_out:
        text = data_in.read()
        padder = padding.ANSIX923(128).padder()
        text = bytes(text, 'UTF-8')
        padded_text = padder.update(text)+padder.finalize()
        iv = os.urandom(16)
        cipher = Cipher(algorithms.SM4(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()
        print(c_text)
        data_out.write(iv)
        data_out.write(c_text)
    data_in.close
    data_out.close

# 3.2


def decryptData(pathToSave: str, pathOfData: str, key):
    name = os.path.join(pathToSave, 'decryptedData.txt')
    with open(pathOfData, 'rb') as data_in, open(name, 'w', encoding='utf-8') as data_out:
        iv = data_in.read(16)
        text = data_in.read()
        # iv = os.urandom(16)
        cipher = Cipher(algorithms.SM4(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(text) + decryptor.finalize()
        unpadder = padding.ANSIX923(128).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
        print(unpadded_dc_text.decode('UTF-8', errors='ignore'))

        data_out.write(unpadded_dc_text.decode('UTF-8', errors='ignore'))
