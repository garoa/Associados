#!/usr/bin/env python
# coding: utf-8
from garoa import Pessoa, ConselhoMandaChuva

Abdo = Pessoa("Alexandre Abdo")
Abreu = Pessoa("Abreu") #nome?
Alexandra = Pessoa("Alexandra Percario")
AllanTrindade = Pessoa("Allan Trindade") # (de São Vicente)
Anchises = Pessoa("Anchises")
Anderson = Pessoa("Anderson") # seria o irmao gemeo do Thiago?
Andre = Pessoa("Andre") #nome completo? (seria esse o Hermann?)
AndreHermann = Pessoa("André Hermann")
Afonso = Pessoa("Afonso Coutinho")
Agaelebe = Pessoa("Hugo Lima Borges")
Aylons = Pessoa("Gustavo Bruno")
BrunoBorges = Pessoa("Bruno Lima Borges") # (Irmão do Hugo)
BrunoLP = Pessoa("Bruno Luiz de Paula")
CSM = Pessoa("CSM") #nome? Seria esse o Carlos CM?
CarlosCM = Pessoa("Carlos CM") # do time de CTF do Garoa
Christian = Pessoa("Christian") # nome completo?
Dandara = Pessoa("Dandara Jatobá")
Dente = Pessoa("Dente") # nome?
DQ = Pessoa("Daniel Quadros")
Emerson = Pessoa("Emerson Monteiro Sobreiro") #padawan do Fabricio
Erik = Pessoa("Erik Dataleak Ramos") #nome real?
Erin = Pessoa("Erin") #nome completo?
FabioH = Pessoa("Fabio Hirano")
FabricioBiazzoto = Pessoa("Fabricio Biazzotto")
Fellype = Pessoa("Fellype Cazorino")
FMolina = Pessoa("Fernando Molina")
FSouza = Pessoa("Felipe Souza")
Gabi = Pessoa("Gabriela Fonseca")
Gabrielzinho = Pessoa("Gabriel Almeida")
GringoMexico = Pessoa("Gringo do México") #nome real?
Guisso = Pessoa("Fernando Guisso")
GustavoRibeiro = Pessoa("GustavoRibeiro")
Gutem = Pessoa("Gutemberg Nunes")
GutoMaia = Pessoa("Gustavo Maia Neto")
Helena = Pessoa("Helena (amiga do Afonso)")
IanF = Pessoa("Ian Fernandez")
Italo = Pessoa("Italo") #nome completo?
JAdriano = Pessoa("João Adriano")
JamesRaznor = Pessoa("James Raznor")
JamesSouza = Pessoa("James Souza")
Juca = Pessoa("Felipe Correa da Silva Sanches")
LaTeX = Pessoa("Leandro Teixeira (LaTeX)")
LAlcantara = Pessoa("Lucas Alcântara")
LuisLeao = Pessoa("Luis Fernando de Oliveira Leão")
Marcel = Pessoa("Marcel") #nome?
MarceloCampos = Pessoa("Marcelo Campos")
MarceloRodrigues = Pessoa("Marcelo Rodrigues") # Lab de Garagem
Mesel = Pessoa("Vinicius Mesel")
Mike = Pessoa("Mike Howard")
NelsonCanton = Pessoa("Nelson Canton")
NelsonBrito = Pessoa("Nelson Brito")
Oda = Pessoa("Eduardo Oda")
Pampolha = Pessoa("Pampolha") #nome?
Pitanga = Pessoa("Rodrigo Rodrigues da Silva")
RobertJr = Pessoa("Robert Junior") # Guisso disse: "Ele é um cabeludinho, magrinho, com cara de nerd, que vem com o pai."
RdosGatos = Pessoa("Rodrigo dos Gatos") # nome real? Rodrigo Silveira talvez?
RodrigoSilveira = Pessoa("Rodrigo Silveira")
Rubens = Pessoa("Rubão") #verificar nome completo (Rubens Tadeu talvez?)
RogerioMunhoz = Pessoa("Rogério Munhoz")
Sandro = Pessoa("Sandro Friedland")
Sebastiao = Pessoa("Sebastião") #nome completo? Seria esse o Sebastiao Barreto ?
Subnet = Pessoa("Luís Guilherme Pires Martins de Abreu")
Tales = Pessoa("Tales Cione")
Taumaturgo = Pessoa("Raphael Taumaturgo") # "o cara da cerveja"
Thiago = Pessoa("Thiago") # seria o irmao gemeo do Anderson?
Thomas = Pessoa("Thomas") # Francês
Ulysses = Pessoa("Ulysses Soldá Junior")
VAlves = Pessoa("Vitor Alves")
Vitor = Pessoa("Vitor Fernandes")
Vido = Pessoa("Lucas Vido")
VJPixel = Pessoa("VJ Pixel")
Vrech = Pessoa("Matheus Vral Vrech") # (São Carlos)
Yumi = Pessoa("Amanda Yumi Ambriola")
Wesley = Pessoa("Wesley Shaimon")

# Os 'jedis' por enquanto são as raízes do grafo incompleto de associados.
# Mas depois que toda a história estiver transcrita aqui,
# esse será a lista dos associados co-fundadores:
jedis = [
  Afonso,
  Juca,
  Dente,
  Vido,
  Guisso,
  Mike
]

CMC = ConselhoMandaChuva(jedis)

# CMC de 18 de Julho de 2017:
CMC.data("2017-07-18")
CMC.readmite_associado(DQ)
CMC.aprova_associado(Emerson, endosso=[Vido])

# CMC de 15 de Agosto de 2017:
CMC.data("2017-08-15")
Dente.apresenta_padawan(Taumaturgo) # "o cara da cerveja"
Juca.apresenta_padawan(GustavoRibeiro)
CMC.aprova_associado(GustavoRibeiro, endosso=[Juca])
CMC.observa_desligamento(GutoMaia, motivo="3 meses de atraso na mensalidade")

# CMC de 19 de Setembro de 2017:
CMC.data("2017-09-19")
Vido.apresenta_padawan(Sebastiao)
CMC.aprova_associado(Sebastiao, endosso=[Vido])
CMC.aprova_associado(Rubens, endosso=[Oda])
CMC.observa_desligamento(Christian, motivo="3 meses de atraso na mensalidade")

# CMC de 17 de Outubro de 2017:
CMC.data("2017-10-17")
# Nota: "Padawan do Dente (Taumaturgo) fugiu para a Espanha"
# Não houve movimentações no quadro de associados / padawans

# CMC de 21 de Novembro de 2017:
CMC.data("2017-11-21")
Guisso.apresenta_padawans([Gabi,
                           RobertJr])
Afonso.apresenta_padawans([AllanTrindade,
                           JamesSouza,
                           Vrech,
                           CarlosCM])

# CMC de 19 de Dezembro de 2017:
CMC.data("2017-12-19")
Guisso.apresenta_padawans([RogerioMunhoz,
                           IanF])
CMC.aprova_associado(Mesel, endosso=[Vido, Yumi])
CMC.aprova_associado(AllanTrindade, endosso=[Vido, Afonso])
CMC.aprova_associado(JamesSouza, endosso=[Afonso])

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
Afonso.apresenta_padawan(Vrech)
CMC.aprova_associado(LAlcantara, endosso=[Juca])

# CMC de 21 de Agosto de 2018:
CMC.data("2018-08-21")
Afonso.apresenta_padawans([Alexandra,
                           Dandara,
                           FSouza,
                           Wesley,
                           VAlves])

CMC.print_padawans()
#CMC.print_associados()
