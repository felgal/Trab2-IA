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

def verificaExisteRecursivoNum(nomeVertParada,vertice,vertAnt,nome,profundidade):
    if profundidade==0:
        return ""
    #print(vertice.nome+"  "+nome)
    pib = [0,0]
    for x in vertice.arestas:
        if(x.vertices[0].nome==nomeVertParada or x.vertices[1].nome==nomeVertParada ):
            for y in x.relacoes:
                if(y[0]==nome):
                    return [1,int(y[1])]
                if(y[1]==nome):
                    return [1,int(y[0])]
        if(x.vertices[0].nome!=vertAnt and x.vertices[1].nome!=vertAnt):
            for y in x.relacoes:
                val = [0,0]
                if(y[0]==nome and x.vertices[0].nome==vertice.nome):
                    val =verificaExisteRecursivoNum(nomeVertParada,x.vertices[1],vertice.nome,y[1],profundidade-1)
                if(y[1]==nome and x.vertices[0].nome==vertice.nome):
                    val =verificaExisteRecursivoNum(nomeVertParada,x.vertices[1],vertice.nome,y[0],profundidade-1)
                if(y[0]==nome and x.vertices[1].nome==vertice.nome):
                    val =verificaExisteRecursivoNum(nomeVertParada,x.vertices[0],vertice.nome,y[1],profundidade-1)
                if(y[1]==nome and x.vertices[1].nome==vertice.nome):
                    val =verificaExisteRecursivoNum(nomeVertParada,x.vertices[0],vertice.nome,y[0],profundidade-1)
                pib[0]+=val[0]
                pib[1]+=val[1]
    return pib

def verificaExisteRecursivo(nomeVertParada,vertice,vertAnt,nome,profundidade):
    if profundidade==0:
        return ""
    #print(vertice.nome+"  "+nome)
    vals=""
    for x in vertice.arestas:
        if(x.vertices[0].nome==nomeVertParada or x.vertices[1].nome==nomeVertParada ):
            for y in x.relacoes:
                if(y[0]==nome):
                    return " "+y[1]
                if(y[1]==nome):
                    return " "+y[0]
        if(x.vertices[0].nome!=vertAnt and x.vertices[1].nome!=vertAnt):
            for y in x.relacoes:
                if(y[0]==nome and x.vertices[0].nome==vertice.nome):
                    vals +=verificaExisteRecursivo(nomeVertParada,x.vertices[1],vertice.nome,y[1],profundidade-1)
                if(y[1]==nome and x.vertices[0].nome==vertice.nome):
                    vals +=verificaExisteRecursivo(nomeVertParada,x.vertices[1],vertice.nome,y[0],profundidade-1)
                if(y[0]==nome and x.vertices[1].nome==vertice.nome):
                    vals +=verificaExisteRecursivo(nomeVertParada,x.vertices[0],vertice.nome,y[1],profundidade-1)
                if(y[1]==nome and x.vertices[1].nome==vertice.nome):
                    vals +=verificaExisteRecursivo(nomeVertParada,x.vertices[0],vertice.nome,y[0],profundidade-1)
    return vals

def verificaExisteRecursivov2(nomeVertParada,vertice,vertAnt,nome,profundidade):
    if profundidade==0:
        return ""
    #print(vertice.nome+"  "+nome)
    vals=""
    for x in vertice.arestas:
        if(x.vertices[0].nome==nomeVertParada or x.vertices[1].nome==nomeVertParada ):
            sum=""
            for y in x.relacoes:
                if(y[0]==nome):
                    sum +=" "+y[1]
                if(y[1]==nome):
                    sum += " "+y[0]
            return sum
        if(x.vertices[0].nome!=vertAnt and x.vertices[1].nome!=vertAnt):
            for y in x.relacoes:
                if(y[0]==nome and x.vertices[0].nome==vertice.nome):
                    vals +=verificaExisteRecursivo(nomeVertParada,x.vertices[1],vertice.nome,y[1],profundidade-1)
                if(y[1]==nome and x.vertices[0].nome==vertice.nome):
                    vals +=verificaExisteRecursivo(nomeVertParada,x.vertices[1],vertice.nome,y[0],profundidade-1)
                if(y[0]==nome and x.vertices[1].nome==vertice.nome):
                    vals +=verificaExisteRecursivo(nomeVertParada,x.vertices[0],vertice.nome,y[1],profundidade-1)
                if(y[1]==nome and x.vertices[1].nome==vertice.nome):
                    vals +=verificaExisteRecursivo(nomeVertParada,x.vertices[0],vertice.nome,y[0],profundidade-1)
    return vals


def verificaExisteRecursivoDuploFiltrado(parada,vertice,vertAnt,nome,profundidade,vencedores):
    #print(vertice.nome+"  "+nome)
    if(profundidade==0):
        return vencedores
    for x in vertice.arestas:
        if(parada==[]):
            return vencedores
        if(x.vertices[0].nome==parada[0][0] or x.vertices[1].nome==parada[0][0]):
            vencedores[0]+=1
            if(vencedores[1]==[]):
                for y in x.relacoes:
                    if (y[0] == nome):
                        vencedores[1].append(y[1])
                    if (y[1] == nome):
                        vencedores[1].append(y[0])
            else:
                paises = verificaExisteRecursivov2("pais",x.vertices[1],"",parada[0][1],6).split(" ")
                for y in vencedores[1]:
                    if y in paises:
                        vencedores[0]+=1
                    else:
                        vencedores[1].remove(y)
                for y in vencedores[1]:
                    if y in paises:
                        vencedores[0]+=1
                    else:
                        vencedores[1].remove(y)

            parada.pop(0)

        if(x.vertices[0].nome!=vertAnt and x.vertices[1].nome!=vertAnt):
            for y in x.relacoes:
                valsTemp=[0,[]]
                if(y[0]==nome and x.vertices[0].nome==vertice.nome):
                    valsTemp =verificaExisteRecursivoDuploFiltrado(parada,x.vertices[1],vertice.nome,y[1],profundidade-1,vencedores)
                if(y[1]==nome and x.vertices[0].nome==vertice.nome):
                    valsTemp =verificaExisteRecursivoDuploFiltrado(parada,x.vertices[1],vertice.nome,y[0],profundidade-1,vencedores)
                if(y[0]==nome and x.vertices[1].nome==vertice.nome):
                    valsTemp =verificaExisteRecursivoDuploFiltrado(parada,x.vertices[0],vertice.nome,y[1],profundidade-1,vencedores)
                if(y[1]==nome and x.vertices[1].nome==vertice.nome):
                    valsTemp =verificaExisteRecursivoDuploFiltrado(parada,x.vertices[0],vertice.nome,y[0],profundidade-1,vencedores)
                if(valsTemp[0]>vencedores[0]):
                    vencedores=valsTemp
    return vencedores

def verificaExisteRecursivoDuplo(nomeVertParada,nomeVertParada2,vertice,vertAnt,nome,profundidade):
    if profundidade==0:
        return ""
    #print(vertice.nome+"  "+nome)
    vals=[]
    valsTemp = []
    for x in vertice.arestas:
        if(x.vertices[0].nome==nomeVertParada ):
            segundaVerificaTemp = []
            segundaVerificaMaior = []
            for y in x.vertices[0].valores:
                segunda = verificaExisteRecursivo(nomeVertParada2,x.vertices[0],"",y,6)
                segundaVerificaTemp = []
                for z in x.vertices[0].valores:
                    segundaVerifica = verificaExisteRecursivo(nomeVertParada2,x.vertices[0],"",z,6)
                    if(segunda==segundaVerifica):
                        segundaVerificaTemp.append(z)
                if(len(segundaVerificaTemp) >len(segundaVerificaMaior)):
                    segundaVerificaMaior=segundaVerificaTemp
            return segundaVerificaMaior
        if(x.vertices[1].nome==nomeVertParada ):
            segundaVerificaMaior = []
            for y in x.vertices[1].valores:
                segunda = verificaExisteRecursivo(nomeVertParada2,x.vertices[1],"",y,6)
                segundaVerificaTemp = []
                for z in x.vertices[1].valores:
                    segundaVerifica = verificaExisteRecursivo(nomeVertParada2,x.vertices[1],"",z,6)
                    if(segunda==segundaVerifica):
                        segundaVerificaTemp.append(z)
                if(len(segundaVerificaTemp) >len(segundaVerificaMaior)):
                    segundaVerificaMaior=segundaVerificaTemp
            return segundaVerificaMaior
        if(x.vertices[0].nome!=vertAnt and x.vertices[1].nome!=vertAnt):
            for y in x.relacoes:
                if(y[0]==nome and x.vertices[0].nome==vertice.nome):
                    valsTemp =verificaExisteRecursivoDuplo(nomeVertParada,nomeVertParada2,x.vertices[1],vertice.nome,y[1],profundidade-1)
                if(y[1]==nome and x.vertices[0].nome==vertice.nome):
                    valsTemp =verificaExisteRecursivoDuplo(nomeVertParada,nomeVertParada2,x.vertices[1],vertice.nome,y[0],profundidade-1)
                if(y[0]==nome and x.vertices[1].nome==vertice.nome):
                    valsTemp =verificaExisteRecursivoDuplo(nomeVertParada,nomeVertParada2,x.vertices[0],vertice.nome,y[1],profundidade-1)
                if(y[1]==nome and x.vertices[1].nome==vertice.nome):
                    valsTemp =verificaExisteRecursivoDuplo(nomeVertParada,nomeVertParada2,x.vertices[0],vertice.nome,y[0],profundidade-1)
    if len(valsTemp)>len(vals):
        return valsTemp
    return vals


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
        linha[1] = [linha[1][0],linha[1][0]]
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
        if(not verificaSeExisteVal(vert1,linha[1][0][0])):
            vert1.valores.append(linha[1][0][0])
        vert2 = verificaSeExiste(vertices,linha[0])
        if(not verificaSeExisteVal(vert2,linha[1][1][1])):
            vert2.valores.append(linha[1][1][1])

printaGrafo(vertices)

#exemplo de pergunta para testar: quais oceanos encostam na america?
#quero achar continente-banhado-oceano

vertice = verificaSeExiste(vertices,"continente")
mylist = verificaExisteRecursivo("oceano",vertice,"","america",6).split(" ")
mylist = list(dict.fromkeys(mylist))
mylist.pop(0)
print("Pergunta 1:")
print("America é banhado por:")
for val in mylist:
    print(val)
print()

#exemplo de pergunta para testar: Qual subcontinente possui a maior media de pib?
#quero achar subcontinente-possui-pib
maior = [0,""]
vertice2 = verificaSeExiste(vertices,"subcontinente")
for val in vertice2.valores:
    pibAtual = verificaExisteRecursivoNum("pib",vertice2,"",val,6)
    if(pibAtual[1]/pibAtual[0]>maior[0]):
        maior[0]=pibAtual[1]/pibAtual[0]
        maior[1]=val
print("Pergunta 2:")
print("O maior pib eh de "+str(maior[1])+" com: "+str(maior[0]))

#exemplo de pergunta para testar: Qual ilhas possuem a mesma moeda na america central?
#quero primeiro subcontinente-possui-ilha
vertice = verificaSeExiste(vertices,"subcontinente")
mylist = verificaExisteRecursivoDuplo("ilha","moeda",vertice,"","america_central",6)
print()

print("Pergunta 3:")
print("As ilhas que possuem a mesma moeda na america central:")
for val in mylist:
    print(val)
print()

#exemplo de pergunta para testar: Os países da América do Sul, que foram colônia da Espanha e hoje são república presidencialista
vertice = verificaSeExiste(vertices,"subcontinente")
verificacoes=[["pais",""],["colonia","espanha"],["governo","republica_presidencialista"]]
mylist = verificaExisteRecursivoDuploFiltrado(verificacoes,vertice,"","america_do_sul",6,[0,[]])

print("Pergunta 4:")
print("Os países da América do Sul, que foram colônia da Espanha e hoje são república presidencialista são:")
for val in mylist[1]:
    print(val)
print()

f.close()