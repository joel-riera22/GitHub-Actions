from solucio_05 import *
import pytest

biblioteca = [
    {
        "llibre": "El Quixot",
        "autor": "Cervantes",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Joan", "dies": 15, "retornat": True},
            {"usuari": "Maria", "dies": 20, "retornat": False},
            {"usuari": "Pere", "dies": 12, "retornat": True}
        ]
    },
    {
        "llibre": "1984",
        "autor": "Orwell",
        "categoria": "ciència-ficció",
        "prestecs": [
            {"usuari": "Pere", "dies": 10, "retornat": True},
            {"usuari": "Anna", "dies": 25, "retornat": True},
            {"usuari": "Marta", "dies": 18, "retornat": False}
        ]
    },
    {
        "llibre": "El Senyor dels Anells",
        "autor": "Tolkien",
        "categoria": "fantasia",
        "prestecs": [
            {"usuari": "Maria", "dies": 30, "retornat": True},
            {"usuari": "Joan", "dies": 22, "retornat": True},
            {"usuari": "Pere", "dies": 15, "retornat": False}
        ]
    },
    {
        "llibre": "Crim i Càstig",
        "autor": "Dostoievski",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Anna", "dies": 28, "retornat": True},
            {"usuari": "Marta", "dies": 14, "retornat": True},
            {"usuari": "Joan", "dies": 21, "retornat": True}
        ]
    }
]

# Exercici 1
@pytest.mark.parametrize("biblioteca, categoria, res_esperat",
    [(biblioteca, "novel·la", ["El Quixot", "Crim i Càstig"]),
     (biblioteca, "ciència-ficció", ["1984"]),
     (biblioteca, "fantasia", ["El Senyor dels Anells"])])

def test_llibres_per_categoria(biblioteca, categoria, res_esperat):
    """
    Prova la funció llibres_per_categoria amb diferents casos utilitzant pytest.mark.parametrize.
    
    Args:
        biblioteca (llista): Una llista de diccionaris que conté informació sobre els llibres.
        categoria (str): La categoria dels llibres a buscar.
        res_esperat (llista): La llista esperada de llibres retornats per la funció.

    Tests inclouen:
        - Categories amb múltiples llibres ("novel·la").
        - Categories amb un sol llibre ("ciència-ficció", "fantasia").
    """
    resultat = llibres_per_categoria(biblioteca, categoria)
    assert resultat == res_esperat

# Exercici 2
@pytest.mark.parametrize("biblioteca, llibre, res_esperat",
    [(biblioteca, "El Senyor dels Anells", False),
     (biblioteca, "1984", False),
     (biblioteca, "Crim i Càstig", True)])

def test_esta_disponible(biblioteca, llibre, res_esperat):
    """
    Prova la funció esta_disponible amb diferents casos utilitzant pytest.mark.parametrize.
    
    Args:
        biblioteca (llista): Una llista de diccionaris que conté informació sobre els llibres.
        llibre (str): El títol del llibre a buscar.
        res_esperat (llista): Retorna True o False.

    Tests inclouen:
        - Titols que no apareixen ("El Senyor dels Anells", "1984").
        - Títols que apareixen ("Crim i Càstig").
    """
    resultat = esta_disponible(biblioteca, llibre)
    assert resultat == res_esperat
            
# Exercici 3
@pytest.mark.parametrize("biblioteca, usuari, res_esperat",
    [(biblioteca, "Anna", False),
     (biblioteca, "Pere", True),
     (biblioteca, "Joan", False)])

def test_usuari_te_prestecs(biblioteca, usuari, res_esperat):
    """
    Prova la funció usuari_te_prestecs amb diferents casos utilitzant pytest.mark.parametrize.
    
    Args:
        biblioteca (llista): Una llista de diccionaris que conté informació sobre els llibres.
        usuari (str): El nom de l'usuari a comprovar.
        res_esperat (llista): Retorna True o False.

    Tests inclouen:
        - Titols pendents per retornar ("True", "False").
    """
    resultat = usuari_te_prestecs(biblioteca, usuari)
    assert resultat == res_esperat
    
# Exercici 4
@pytest.mark.parametrize("biblioteca, llibre, res_esperat",
    [(biblioteca, "El Senyor dels Anells", 67),
     (biblioteca, "Crim i Càstig", 63),
     (biblioteca, "El Quixot", 47)])

def test_dies_prestec_total(biblioteca, llibre, res_esperat):
    """
    Prova la funció dies_prestec_total amb diferents casos utilitzant pytest.mark.parametrize.
    
    Args:
        biblioteca (llista): Una llista de diccionaris que conté informació sobre els llibres.
        llibre (str): El títol del llibre a calcular.
        res_esperat (llista): Calcula la suma total de dies que un llibre determinat ha estat prestat.

    Tests inclouen:
        - Tres llibres diferents.
    """
    resultat = dies_prestec_total(biblioteca, llibre)
    assert resultat == res_esperat
