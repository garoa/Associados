#!/usr/bin/env python
# coding: utf-8
from garoa import Pessoa, ConselhoMandaChuva

Abdo = Pessoa("Alexandre Abdo")
Abreu = Pessoa("Abreu") #nome?
Alexandra = Pessoa("Alexandra Percario")
Aleph = Pessoa("Alberto Fabiano")
Allan = Pessoa("Allan") #nome completo? Seria esse o Allan Moreira?
AllanTrindade = Pessoa("Allan Trindade") # (de São Vicente)
Anchises = Pessoa("Anchises")
Anderson = Pessoa("Anderson Queiroz") # irmao gemeo do Tiago
Andre = Pessoa("Andre") #nome completo? (seria esse o Hermann? ou o Oliveira?)
AndreOliveira = Pessoa("Andre de Oliveira")
AndreHermann = Pessoa("André Hermann")
Afonso = Pessoa("Afonso Coutinho")
Agaelebe = Pessoa("Hugo Lima Borges")
Aylons = Pessoa("Gustavo Bruno")
Belasco = Pessoa("Pedro Belasco")
BrunoBorges = Pessoa("Bruno Lima Borges") # (Irmão do Hugo)
BrunoLP = Pessoa("Bruno Luiz de Paula")
CSM = Pessoa("CSM") #nome? Seria esse o Carlos CM?
CarlosCM = Pessoa("Carlos CM") # do time de CTF do Garoa
Carril = Pessoa("Fernando Carril")
Ceci = Pessoa("Cecilia Tanaka")
Christian = Pessoa("Christian") # nome completo?
Dandara = Pessoa("Dandara Jatobá")
DanielaIwassa = Pessoa("Daniela Iwassa")
Dente = Pessoa("Marcelo Araujo Dente")
DQ = Pessoa("Daniel Quadros")
Emerson = Pessoa("Emerson Monteiro Sobreiro") #padawan do Fabricio
ErickEmiliano = Pessoa("Erick Emiliano")
ErikDataleak = Pessoa("Erik Dataleak Ramos") #nome real?
Erin = Pessoa("Erin") #nome completo?
Eros = Pessoa("Eros") #nome completo?
FabioH = Pessoa("Fabio Hirano")
FabricioBiazzotto = Pessoa("Fabricio Biazzotto")
Fellype = Pessoa("Fellype Cazorino")
FelipeMoreira = Pessoa("Felipe Moreira")
Fernanda = Pessoa("Fernanda") # do Lab de Garagem #nome completo?
FMolina = Pessoa("Fernando Molina")
FSouza = Pessoa("Felipe Souza")
Gabi = Pessoa("Gabriela Fonseca")
Gabrielzinho = Pessoa("Gabriel Almeida")
Gabs = Pessoa("Gabriel 'Gabs'") #nome completo?
Giovanna = Pessoa("Giovanna")
GringoMexico = Pessoa("Gringo do México") #nome real?
Guisso = Pessoa("Fernando Guisso")
GustavoRibeiro = Pessoa("GustavoRibeiro")
Gutem = Pessoa("Gutemberg Nunes de Carvalho")
GutoMaia = Pessoa("Gustavo Maia Neto")
Helena = Pessoa("Helena (amiga do Afonso)")
IanF = Pessoa("Ian Fernandez")
Italo = Pessoa("Italo") #nome completo?
Ivar = Pessoa("Ivar") #nome completo?
Ismael = Pessoa("Ismael Lopes")
JAFreitas = Pessoa("João Adriano Freitas")
JamesRaznor = Pessoa("James Raznor")
JamesSouza = Pessoa("James Souza")
Jonnes = Pessoa("Jonnes") #nome completo?
Juca = Pessoa("Felipe Correa da Silva Sanches")
Kemel = Pessoa("Kemel Zaidan")
LaTeX = Pessoa("Leandro Teixeira (LaTeX)")
LAlcantara = Pessoa("Lucas Alcântara")
Lechuga = Pessoa("Lechuga") #nome completo?
LeonardoSantos = Pessoa("Leonardo Garcia Tales dos Santos")
LuisLeao = Pessoa("Luis Fernando de Oliveira Leão")
Luiz = Pessoa("Luiz") #nome completo?
Marcel = Pessoa("Marcel") #nome?
MarceloCampos = Pessoa("Marcelo Campos")
MarceloRodrigues = Pessoa("Marcelo Rodrigues") # Lab de Garagem
Mesel = Pessoa("Vinicius Mesel")
Micael = Pessoa("Micael Vitor DJ")
Mike = Pessoa("Mike Howard")
Moreno = Pessoa("Moreno Hassem")
NelsonCanton = Pessoa("Nelson Canton")
NelsonBrito = Pessoa("Nelson Brito")
Oda = Pessoa("Eduardo Oda")
Otto = Pessoa("Otto Heringer")
Pampolha = Pessoa("Pampolha") #nome?
Pitanga = Pessoa("Rodrigo Rodrigues da Silva")
Ramalho = Pessoa("Luciano Ramalho")
RafaelML = Pessoa("Rafael M Lopes")
RobertJr = Pessoa("Robert Junior") # Guisso disse: "Ele é um cabeludinho, magrinho, com cara de nerd, que vem com o pai."
RodrigoSilveira = Pessoa("Rodrigo Gomes da Silveira") # "dos gatos"
Roger = Pessoa("Roger") #nome completo?
RogerioMunhoz = Pessoa("Rogério Munhoz")
Rubens = Pessoa("Rubão") #verificar nome completo (Rubens Tadeu talvez?)
Sandro = Pessoa("Sandro Friedland")
Sebastiao = Pessoa("Sebastião") #nome completo? Seria esse o Sebastiao Barreto ?
Subnet = Pessoa("Luís Guilherme Pires Martins de Abreu")
Tales = Pessoa("Tales Cione")
Taumaturgo = Pessoa("Raphael Taumaturgo") # "o cara da cerveja"
Tiago = Pessoa("Tiago Queiroz") # irmao gemeo do Anderson
Tony = Pessoa("Tony de Marco")
Thomas = Pessoa("Thomas") # Francês
Ulysses = Pessoa("Ulysses Soldá Junior")
VAlves = Pessoa("Vitor Alves")
Vecchio = Pessoa("Vecchio") #nome completo?
Vitor = Pessoa("Vitor Fernandes")
Vido = Pessoa("Lucas Vido")
Villares = Pessoa("Alexandre Villares")
VJPixel = Pessoa("VJ Pixel")
Vrech = Pessoa("Matheus Vral Vrech") # (São Carlos)
Yumi = Pessoa("Amanda Yumi Ambriola")
Yanava = Pessoa("Yanava") # nome?
Wesley = Pessoa("Wesley Shaimon")

# Os 'jedis' por enquanto são as raízes do grafo incompleto de associados.
# Mas depois que toda a história estiver transcrita aqui,
# esse será a lista dos associados co-fundadores:
jedis = [
  Anchises,
  Agaelebe,
  FabioH,
  Juca,
  Mike,
  Ramalho,
  Tiago,
  Vido,
  Yumi,
]

CMC = ConselhoMandaChuva(jedis)

# CMC de 19 de Janeiro de 2016:
CMC.data("2016-01-19")
Mike.apresenta_padawans([DanielaIwassa,
                         Carril])
CMC.aprova_associado(DanielaIwassa, endosso=[Mike])
CMC.aprova_associado(Carril, endosso=[Mike])

# CMC de 16 de Fevereiro de 2016:
CMC.data("2016-02-16")
Ramalho.apresenta_padawan(Villares)
Mike.apresenta_padawan(MarceloCampos)
CMC.aprova_associado(Villares, endosso=[Ramalho])
CMC.aprova_associado(MarceloCampos, endosso=[Mike])
# Pitanga apresentou uma proposta de "endorsements" que foi acatada ao Regimento Interno, mas nunca vi ser implementada de fato.

# CMC de 15 de Março de 2016:
CMC.data("2016-03-15")
Mike.apresenta_padawans([Gutem,
                         JAFreitas])
Agaelebe.apresenta_padawan(BrunoBorges)
CMC.aprova_associado(Gutem, endosso=[Mike])
CMC.aprova_associado(JAFreitas, endosso=[Mike])
CMC.aprova_associado(BrunoBorges, endosso=[Agaelebe])

# CMC de 19 de Abril de 2016:
CMC.data("2016-04-19")
CMC.readmite_associado(Ceci) # "Se possível, Ceci solicita retomar a associação junto ao Garoa Hacker Clube, bem como retornar a ser membro do CMC e retomar a moderação das listas do Garoa, bem como de suas redes sociais. Saudadinhas, hehe...  ;)"

# CMC de 17 de Maio de 2016:
CMC.data("2016-05-17")
# Não houve movimentação no quadro de associados/padawans

# CMC de 21 de Junho de 2016:
CMC.data("2016-06-21")
Tiago.apresenta_padawan(FabricioBiazzotto)
# A ata tem uma piada que pode gerar confusão: "Quem é Tiago Queiroz? O Fabrício apresenta o Tiago como associado do Garoa"
CMC.observa_desligamento(LuisLeao,      motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(RafaelML,      motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(Kemel,         motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(Otto,          motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(Eros,          motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(FelipeMoreira, motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(AndreOliveira, motivo="3 (ou mais) meses de atraso na mensalidade")


# CMC de 19 de Julho de 2016:
CMC.data("2016-07-19")
CMC.aprova_associado(FabricioBiazzotto, endosso=[Tiago])

# CMC de 16 de Agosto de 2016:
CMC.data("2016-08-16")
FabioH.apresenta_padawan(Luiz) # ata diz apenas "Fabio"
Vido.apresenta_padawan(Ismael)
CMC.readmite_associado(Jonnes) # DQ sugeriu. "Ele se afastou por algum tempo mas quer retornar."
CMC.readmite_associado(Afonso) # "Afonso pede para reativar associação e entrar no Starving Hacker"
CMC.observa_desligamento(Tales) # "Anchises informa que Tales Cione solicitou o seu desligamento"

# CMC de 20 de Setembro de 2016:
CMC.data("2016-09-20")
Agaelebe.apresenta_padawan(Ivar)
CMC.observa_desligamento(Tony, motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(LaTeX, motivo="3 (ou mais) meses de atraso na mensalidade") #dúvida: ata diz "Leandro"
CMC.observa_desligamento(Gabs, motivo="3 (ou mais) meses de atraso na mensalidade")

# CMC de 18 de Outubro de 2016:
CMC.data("2016-10-18")
CMC.aprova_associado(Sandro, endosso=[Mike])
CMC.observa_desligamento(AndreOliveira, motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(LeonardoSantos, motivo="3 (ou mais) meses de atraso na mensalidade")

# CMC de 15 de Novembro de 2016:
CMC.data("2016-11-15")
FabricioBiazzotto.apresenta_padawan(RodrigoSilveira)

# CMC de 20 de Dezembro de 2016:
CMC.data("2016-12-20")
Anchises.apresenta_padawan(ErickEmiliano)
CMC.aprova_associado(Guisso, endosso=[Yumi])
CMC.aprova_associado(RodrigoSilveira, endosso=[FabricioBiazzotto])

# CMC de 17 de Janeiro de 2017:
CMC.data("2017-01-17")
Ramalho.apresenta_padawan(Belasco)
# Ata confusa. Esse dois foram desligados? Acho que não:
#        Pitanga
#        Allan
CMC.observa_desligamento(LuisLeao,  motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(Tony,  motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(Tales, motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(Kemel, motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(Eros,          motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(FelipeMoreira, motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(Roger,         motivo="3 (ou mais) meses de atraso na mensalidade")
CMC.observa_desligamento(AndreOliveira, motivo="3 (ou mais) meses de atraso na mensalidade")

# CMC de 21 de Fevereiro de 2017:
CMC.data("2017-02-21")
# Nenhuma alteração no quadro de associados/padawans

# CMC de 21 de Março de 2017:
CMC.data("2017-03-21")
Yumi.apresenta_padawan(Mesel)
FabricioBiazzotto.apresenta_padawan(Emerson)
CMC.aprova_associado(Emerson, endosso=[FabricioBiazzotto])
CMC.aprova_associado(ErikDataleak, endosso=[Anchises])
# Ficou confuso na ata! aparentemente tem também um "Erick", suponho que seja o Emiliano:
# "Anchises apresenta Erick como associado - quarentena"
CMC.observa_desligamento(Allan, motivo="6 meses de atraso na mensalidade")
CMC.observa_desligamento(Gabs, motivo="6 meses de atraso na mensalidade")

# CMC de 18 de Abril de 2017:
CMC.data("2017-04-18")
CMC.observa_desligamento(Yanava, motivo="3 meses de atraso na mensalidade")
CMC.observa_desligamento(LaTeX, motivo="3 meses de atraso na mensalidade") # ata diz "Leandro" (é o LaTeX mesmo?)
CMC.observa_desligamento(DQ, motivo="requisitado")
# NOTA: CMC aprova DQ como associado honorário.

# CMC de 16 de Maio de 2017:
CMC.data("2017-05-16")
CMC.readmite_associado(Afonso)
Afonso.apresenta_padawan(Micael)
Tiago.apresenta_padawan(Anderson) # "como seu padawan recursivo"
Mike.apresenta_padawans([Dente,
                         Thomas])
CMC.aprova_associado(Christian, endosso=[Oda])

# CMC de 20 de Junho de 2017:
CMC.data("2017-06-20")
CMC.aprova_associado(Dente)
CMC.aprova_associado(Anderson)
CMC.aprova_associado(Thomas)
# a ata diz: "Total de associados do Garoa no final de Abril: 40 (?)"

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
