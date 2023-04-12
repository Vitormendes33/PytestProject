from validsenha import *
from validusuarios import *

def test_geral():
    

    assert True == usu_pimeiraletra ("Vitormendes") 
    assert False == usu_pimeiraletra ("vitormendes") 
    assert True == usu_space ("Vitormendes")
    assert False == usu_space ("Vitor mendes") 
    assert True == usuárioSpecial ("Vitormendes")
    assert False == usuárioSpecial ("V!tormendes")
    assert True == usuáriocaractere ("Vitormendes")
    assert False == usuáriocaractere ("VitormendesVitormendesVitormendesVitormendesVitormendesVitormendesVitormendesVitormendesVitormendes")

    assert True == sen_maiuscula ("Vitormendes@1") 
    assert False == sen_maiuscula ("vitormendes@1")
    assert True == sen_minuscula ("Vitormendes@1") 
    assert False == sen_minuscula ("VITORMENDES@1")
    assert True == sen_numero ("Vitormendes@1") 
    assert False == sen_numero ("Vitormendes@")
    assert True == sen_min ("Vitormendes@1") 
    assert False == sen_min ("v1t@r")
    assert True == caractere_especial ("Vitormendes@1") 
    assert False == caractere_especial ("vitormendes1")