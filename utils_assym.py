import logging
import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding as padding1
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key


def generate_assym_keys():
    """generate assym keys"""
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def save_symm_key(pathOfKey: str, publicKey: rsa.RSAPublicKey, symmKey: str) -> None:
    """encrypt and save symm key"""
    name = os.path.join(pathOfKey, "symm.bin")
    c_text = publicKey.encrypt(symmKey, padding1.OAEP(mgf=padding1.MGF1(
        algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    try:
        with open(name, 'wb') as symm_out:
            symm_out.write(c_text)
    except Exception as e:
        logging.error(f"something went wrong with {name} and {str(e)}")
        raise Exception("saving file error")


def save_assym_keys(pathOfPublic: str, pathOfPrivate: str, publicKey: rsa.RSAPublicKey, privateKey: rsa.RSAPrivateKey) -> None:
    """save assym keys to .pem file"""
    public_pem = os.path.join(pathOfPublic, 'public.pem')
    try:
        with open(public_pem, 'wb') as public_out:
            public_out.write(publicKey.public_bytes(encoding=serialization.Encoding.PEM,
                                                    format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except Exception as e:
        logging.error(f"something went wrong with {public_pem} and {str(e)}")
        raise Exception("saving file error")
    try:
        private_pem = os.path.join(pathOfPrivate, 'private.pem')
        with open(private_pem, 'wb') as private_out:
            private_out.write(privateKey.private_bytes(encoding=serialization.Encoding.PEM,
                                                       format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                       encryption_algorithm=serialization.NoEncryption()))
    except:
        logging.error(f"something went wrong with {public_pem} and {str(e)}")
        raise Exception("saving file error")


def load_and_decrypt_symm_key(pathOfKey: str, pathOfPrivateKey: str) -> bytes:
    """load and then decrypt symm key from file"""
    dc_text = ''
    privateKey = 0
    try:
        with open(pathOfKey, 'rb') as symm_in, open(pathOfPrivateKey, 'rb') as private_in:
            privateKey = private_in.read()
            privateKey = load_pem_private_key(privateKey, password=None)
            dc_text = symm_in.read()
        return privateKey.decrypt(dc_text, padding1.OAEP(mgf=padding1.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    except Exception as e:
        logging.error(f"something went wrong with {pathOfKey} and {str(e)}")
        raise Exception("loading file error")
