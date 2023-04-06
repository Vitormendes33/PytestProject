from cryptographyFramework import *

initializeWrite()
user = "vitor"
password = "12345"
encryptedText = encryptMessage(user, password, "Minha mensagem secreta!")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Minha segunda mensagem secreta!")
saveNewLine(encryptedText)

