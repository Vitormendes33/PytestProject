def sen_maiuscula(senha):
    for char in senha:
        if char.isupper():
            return True
        else:
            return False

def sen_minuscula(senha):
    for char in senha:
        if char.islower():
            return True
        else:    
            return False

def sen_numero(senha):
    for char in senha:
        if char.isdigit():
            return True
        else:    
            return ("Está faltando um número")

def sen_min(senha):
    return len(senha) >= 10

def caractere_especial(senha):
    caractere_especial = "!@#$%¨&*()_+-=}{|[]\\:\";'<>?,./"
    for char in senha:
        if char in caractere_especial:
            return True
        else:    
            return ("Está faltando o caractere especial")

