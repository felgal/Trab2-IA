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
            print("Nome valor: "+str(y))
        print()

def verificaExisteRecursivo(vertice,vertAnt,nome,profundidade):
    if profundidade==0:
        return ""
    #print(vertice.nome+"  "+nome)
    oceanos=""
    for x in vertice.arestas:
        if(x.vertices[0].nome=="oceano" or x.vertices[1].nome=="oceano" ):
            for y in x.relacoes:
                if(y[0]==nome):
                    return " "+y[1]
                if(y[1]==nome):
                    return " "+y[0]
        if(x.vertices[0].nome!=vertAnt and x.vertices[1].nome!=vertAnt):
            for y in x.relacoes:
                if(y[0]==nome and x.vertices[0].nome==vertice.nome):
                    oceanos +=verificaExisteRecursivo(x.vertices[1],vertice.nome,y[1],profundidade-1)
                if(y[1]==nome and x.vertices[0].nome==vertice.nome):
                    oceanos +=verificaExisteRecursivo(x.vertices[1],vertice.nome,y[0],profundidade-1)
                if(y[0]==nome and x.vertices[1].nome==vertice.nome):
                    oceanos +=verificaExisteRecursivo(x.vertices[0],vertice.nome,y[1],profundidade-1)
                if(y[1]==nome and x.vertices[1].nome==vertice.nome):
                    oceanos +=verificaExisteRecursivo(x.vertices[0],vertice.nome,y[0],profundidade-1)
    return oceanos

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

    if(linha[0]=="governo" or linha[0]=="moeda" or linha[0]=="continente" or linha[0]=="area" or linha[0]=="populacao" or linha[0]=="capital" or linha[0]=="idioma" or linha[0]=="colonia" or linha[0]=="pib" or linha[0]=="oceano" or linha[0]=="clima" or linha[0]=="subcontinente" or linha[0]=="regiao_continental"):
        arest = verificaSeExisteArestaPorNome(arestas,"pais",linha[0])
        arest.relacoes.append(linha[1])
        vert1 = verificaSeExiste(vertices,"pais")
        if(not verificaSeExisteVal(vert1,linha[1][0])):
            vert1.valores.append(linha[1][0])
        vert2 = verificaSeExiste(vertices,linha[0])
        if(not verificaSeExisteVal(vert2,linha[1][1])):
            vert2.valores.append(linha[1][1])

    if(linha[0]=="ilha"):
        linha[1] = [linha[1],linha[1]]
        arest = verificaSeExisteArestaPorNome(arestas,"pais",linha[0])
        arest.relacoes.append(linha[1])
        vert1 = verificaSeExiste(vertices,"pais")
        if(not verificaSeExisteVal(vert1,linha[1][0])):
            vert1.valores.append(linha[1][0])
        vert2 = verificaSeExiste(vertices,linha[0])
        if(not verificaSeExisteVal(vert2,linha[1][1])):
            vert2.valores.append(linha[1][1])


    if(linha[0]=="continentes"):
        linha[0]="continente"
        linha[1] = [linha[1],linha[1]]
        arest = verificaSeExisteArestaPorNome(arestas,"subcontinente",linha[0])
        arest.relacoes.append(linha[1])
        vert1 = verificaSeExiste(vertices,"subcontinente")
        if(not verificaSeExisteVal(vert1,linha[1][0])):
            vert1.valores.append(linha[1][0])
        vert2 = verificaSeExiste(vertices,linha[0])
        if(not verificaSeExisteVal(vert2,linha[1][1])):
            vert2.valores.append(linha[1][1])

printaGrafo(vertices)

#exemplo de pergunta para testar: quais oceanos encostam na america?
#quero achar continente-banhado-oceano

vertice = verificaSeExiste(vertices,"continente")
mylist = verificaExisteRecursivo(vertice,"","america",6).split(" ")
mylist = list(dict.fromkeys(mylist))
mylist.pop(0)
print(mylist)
f.close()