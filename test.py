from utils import generateAssymKeys, generateSymmKey, saveSymmKey, loadAndDecryptSymmKey, encryptData, decryptData
import os
test = generateSymmKey()
test1 = generateAssymKeys()
pub = test1.public_key()
pr = test1

print("======================")

encryptData('D:\git\isb-3\data', 'D:\git\isb-3\data\data.txt', test)


print('-----------------------------------')


decryptData('D:\git\isb-3\data', 'D:\git\isb-3\data\encryptedData.txt', test)

# генерация ключа симметричного алгоритма шифрования
# import os #можно обойтись стандартным модулем

# key = os.urandom(16) # это байты

# print(type(key))
# print(key)
# from cryptography.hazmat.primitives import padding

# padder = padding.ANSIX923(32).padder()
# text = bytes('кто прочитал тот здохнет', 'UTF-8')
# padded_text = padder.update(text)+padder.finalize()

# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# iv = os.urandom(16) #случайное значение для инициализации блочного режима, должно быть размером с блок и каждый раз новым
# cipher = Cipher(algorithms.SM4(key), modes.CBC(iv))
# encryptor = cipher.encryptor()
# c_text = encryptor.update(padded_text) + encryptor.finalize()
# print(c_text)



# decryptor = cipher.decryptor()
# dc_text = decryptor.update(c_text) + decryptor.finalize()

# unpadder = padding.ANSIX923(32).unpadder()
# unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()

# print(dc_text.decode('UTF-8'))
# print(unpadded_dc_text.decode('UTF-8'))