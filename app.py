from cryptographyFramework import *
from validsenha import *
from validusuarios import *



user = usuario = input("Digite seu usuário: ")
usu_pimeiraletra(usuario)
usu_space(usuario)
usuárioSpecial(usuario)
usuáriocaractere(usuario)
user = senha = input("Digite sua senha: ")
sen_maiuscula(senha)
sen_minuscula(senha)
sen_numero(senha)
sen_min(senha)
caractere_especial(senha)
user = usuario
password = senha
menssage = input("Escreva a mensagem que deseja criptografar: \n")
if len (menssage) > 70:
    print("Sua mensagem tem mais de 70 caracteres, Tente novamente.")
else:
    print("Mensagem encriptada com sucesso")
mencript = encryptMessage(user, password, menssage)
saveNewLine(mencript)

