def usu_pimeiraletra(usuario):
    return usuario[0].isupper()

def usu_space(usuario):
    if " " in usuario:
        return False
    else:
        return True

def usuárioSpecial(usuario):
    if any(not c.isalnum() for c in usuario):
        return False
    else:
        return True


def usuáriocaractere(usuario):
    if len(usuario) > 30:
        return False
    else:
        return True