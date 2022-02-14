# Kirjoita postinumerot-moduulin testit tähän tiedostoon

# postitoimipaikan nimellä löytyy vain yksi postinumero
# postitoimipaikan nimellä löytyy useita postinumeroita
# postitoimipaikan nimellä ei löydy lainkaan postinumeroita.

from postinumerot import postinumerot_func

def test_one_multiple(): 

   nrot2 = postinumerot_func("LOHJA")

   assert len(nrot2) > 1

#?????????????

def test_two_one(): 

   nrot2 = postinumerot_func("Korvatunturi")

   assert len(nrot2) == 1

def test_three_none(): 

   nrot2 = postinumerot_func("Atlantis")

   assert len(nrot2) < 1