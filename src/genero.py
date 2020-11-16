import wikipedia

# bandas = ["Unlucky Morpheus", "Angra", "Turisas", "Wind Rose", "Dark Moor"]

def getGenero(descricao: [str]) -> str :
    for i, v in enumerate(descricao):
        if v.lower() == "metal" :
            return descricao[i - 1].capitalize() + " " + v.capitalize()
    return "Metal"

def procura(banda: str) -> [str] :
    try :
        return wikipedia.summary(banda + " (band)").split(" ")
    except :
        try :
            return wikipedia.summary(banda).split(" ")
        except :
            return [" ", "Metal"]

def main(banda: str) :
    return getGenero(procura(banda))
