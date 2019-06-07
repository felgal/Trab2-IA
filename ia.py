class vertice:
    def __init__(self,nome):
        self.nome = nome
        self.arestas = []
        self.valores = []

class aresta:
    def __init__(self,nome,vert1,vert2):
        self.nome = nome
        self.vertices = []
        self.vertices.append(vert1)
        self.vertices.append(vert2)
        self.relacoes = []

def verificaSeExiste(vals,nome):
    for x in vals:
        if(x.nome==nome):
            return x
    return None

def verificaSeExisteVal(vals,nome):
    for x in vals.valores:
        if(x==nome):
            return True
    return False

def verificaSeExisteAresta(vals,dividido):
    for x in vals:
        if(x.nome==dividido[1]):
            if(verificaSeExiste(x.vertices,dividido[0])!=None and verificaSeExiste(x.vertices,dividido[2])!=None):
                return x
    return None

def verificaSeExisteArestaPorNome(vals,nome1,nome2):
    for x in vals:
        if(verificaSeExiste(x.vertices,nome1)!=None and verificaSeExiste(x.vertices,nome2)!=None):
            return x
    return None

def printaGrafo(verts):
    for x in verts:
        print("Nome vertice: "+x.nome)
        for y in x.arestas:
            print("Nome aresta: ("+y.nome+") liga "+y.vertices[0].nome+" a "+y.vertices[1].nome)
            for z in y.relacoes:
                print("Relacao da aresta: "+str(z))
        for y in x.valores:
            print("Nome valor: "+y)
        print()


vertices=[]
arestas=[]
f= open("grafoIA.txt","r+")
linhas=f.readlines()
for linha in linhas:
    dividido = linha.strip('\n').strip(" ").split("-")


    vert1 = verificaSeExiste(vertices,dividido[0])
    if(vert1==None):
        vert1=vertice(dividido[0])
        vertices.append(vert1)

    vert2 = verificaSeExiste(vertices, dividido[2])
    if (vert2 == None):
        vert2=vertice(dividido[2])
        vertices.append(vert2)

    arest = verificaSeExisteAresta(arestas,dividido)
    if(arest == None):
        arest = aresta(dividido[1],vert1,vert2)
        vert1.arestas.append(arest)
        vert2.arestas.append(arest)
        arestas.append(arest)


f= open("importIA.txt","r+")
linhas=f.readlines()
for linha in linhas:
    linha = linha.strip('\n').strip(" ").strip(".").strip(")")
    linha = linha.split("(")
    linha[1] = linha[1].strip(' ').split(",")

    if(linha[0]=="governo"):
        arest = verificaSeExisteArestaPorNome(arestas,"pais",linha[0])
        arest.relacoes.append(linha[1])
        vert1 = verificaSeExiste(vertices,"pais")
        if(not verificaSeExisteVal(vert1,linha[1][0])):
            vert1.valores.append(linha[1][0])
        vert2 = verificaSeExiste(vertices,linha[0])
        if(not verificaSeExisteVal(vert2,linha[1][1])):
            vert2.valores.append(linha[1][1])


printaGrafo(vertices)

f.close()