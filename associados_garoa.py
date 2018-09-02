Abdo = "Alexandre Abdo"
Abreu = "Abreu" #nome?
Alexandra = "Alexandra Percario"
Anchises = "Anchises"
Andre = "Andre" #nome completo? (seria esse o Hermann?)
AndreHermann = "André Hermann"
Afonso = "Afonso Coutinho"
Agaelebe = "Hugo Lima Borges"
Aylons = "Gustavo Bruno"
BrunoBorges = "Bruno Lima Borges" # (Irmão do Hugo)
BrunpLP = "Bruno Luiz de Paula"
CSM = "CSM" #nome?
Dandara = "Dandara Jatobá"
Dente = "Dente" # nome?
DQ = "Daniel Quadros"
FabioH = "FabioHirano"
Fabricio = "Fabricio" #nome?
Fellype = "Fellype Cazorino"
FMolina = "Fernando Molina"
FSouza = "Felipe Souza"
Gabrielzinho = "Gabriel Almeida"
GringoMexico = "Gringo do México" #nome real?
Guisso = "Fernando Guisso"
Gutem = "Gutemberg Nunes"
GutoMaia = "Gustavo Maia Neto"
IanF = "Ian Fernandez"
JAdriano = "João Adriano"
JamesRaznor = "James Raznor"
Juca = "Felipe Correa da Silva Sanches"
LaTeX = "LaTeX" #nome real?
LAlcantara = "Lucas Alcântara"
LuisLeao = "Luis Fernando de Oliveira Leão"
Marcel = "Marcel" #nome?
MarceloCampos = "Marcelo Campos"
MarceloRodrigues = "Marcelo Rodrigues" # Lab de Garagem
Mesel = "Vinicius Mesel"
Mike = "Mike Howard"
NelsonCanton = "Nelson Canton"
NelsonBrito = "Nelson Brito"
Oda = "Eduardo Oda"
Pampolha = "Pampolha" #nome?
Pitanga = "Rodrigo Rodrigues da Silva"
RdosGatos = "Rodrigo dos Gatos" # nome real? Rodrigo Silveira talvez?
RodrigoSilveira = "Rodrigo Silveira"
Rubens = "Rubão" #verificar nome completo
RMunhoz = "Rogério Munhoz"
Sandro = "Sandro Friedland"
Subnet = "Luís Guilherme Pires Martins de Abreu"
Tales = "Tales Cione"
Thomas = "Thomas" # Francês
Ulysses = "Ulysses Soldá Junior"
VAlves = "Vitor Alves"
Vitor = "Vitor Fernandes"
Vido = "Lucas Vido"
VJPixel = "VJ Pixel"
Vrech = "Matheus Vral Vrech"
Yumi = "Amanda Yumi Ambriola"
Wesley = "Wesley Shaimon"

# CMC de 16 de Janeiro de 2018:
CMC.data("2018-01-16")
Afonso.apresenta_padawan(JamesRaznor)
Mike.apresenta_padawan(Marcel) # faz cerveja, lava panela de feijoada e faz pizza.
Mesel.apresenta_padawan(NelsonBrito)

# CMC de 20 de Fevereiro de 2018:
CMC.data("2018-02-20")
Guisso.apresenta_padawan(AndreHermann)
CMC.readmite_associado(Ulysses)

# CMC de 20 de Março de 2018:
CMC.data("2018-03-20")
CMC.observa_desligamento(NelsonCanton) # solicitou
CMC.observa_desligamento(Aylons) # solicitou
CMC.aprova_associado(NelsonBrito, endosso=[Mesel])

# CMC de 17 de Abril de 2018:
CMC.data("2018-04-17")
CMC.observa_desligamento(BrunoLP, motivo="3 meses de atraso")
CMC.pergunta("Dúvida: Marcelo Rodrigues ainda é associado?")

# CMC de 15 de Maio de 2018:
CMC.data("2018-05-15")
# NOTA: Reunião cancelada por falta de quorum mínimo.
# Mas constam as seguintes intenções:
CMC.observa_desligamento(Guisso) # (não requer autorização do CMC)
#
# "Afonso apresenta Stefanie Melo e Aline Paffaro como padawans,
#  já estão a 3 semanas tocando a atividade
#  Clube de Estudos de Algoritmos."

# CMC de 19 de Junho de 2018:
CMC.data("2018-06-19")
Juca.apresenta_padawan(LAlcantara)
CMC.aprova_associado(IanF, endosso=[Oda, Yumi])
CMC.readmite_associado(Guisso) # mediante quitação de atraso de 6 mensalidades
CMC.observa_desligamento(BrunoBorges)

# CMC de 17 de Julho de 2018:
CMC.data("2018-07-17")
Afonso.apresenta_padawan(VRech)
CMC.aprova_associado(LAlcantara, endosso=[Juca])

# CMC de 21 de Agosto de 2018:
CMC.data("2018-08-21")
Afonso.apresenta_padawans([Alexandra,
                           Dandara,
                           FSouza,
                           Wesley,
                           VAlves])
