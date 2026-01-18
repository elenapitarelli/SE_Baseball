from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self._id_map = {}
        self._salary_dict = {}
        self.G = nx.Graph() # non orientato, senza di
    def get_years(self):
        return DAO.get_years_from_1980()
    def get_teams(self, year):
        return DAO.get_team(year)

    def costruisci_grafo(self,year):
        self.G.clear()
        self._id_map = {}
        self._nodes = DAO.get_team(year)
        self._edges = DAO.get_all_coppie(year)
        self.salari_dict = DAO.calcola_salario_per_anno(year)

        # nodi
        for team in self._nodes:
            self._id_map[team.id]= team



        # aggiungo nodi
        self.G.add_nodes_from(self._id_map.keys())
        #archi
        for id1, id2 in self._edges:
            if id1 in self._id_map and id2 in self._id_map: #se id 1 e id sono nella mappa dei nodi
                t1 = self._id_map[id1] #ogg t1 corrispondente
                t2 = self._id_map[id2] #ogg t2 corrispondente
                peso = self.salari_dict.get(t1.id,0) + self.salari_dict.get(t2.id,0) #prendo salario tema1 dal dizionario , se nonesiste rest 0; lo spmmpo al salario di t2.
                self.G.add_edge(t1.id, t2.id, weight=peso) # aggiungo arco pesato(peso è somma salari)

    def get_vicini(self,team): #team qui è l'id del nodo del grafo
        vicini =[] # creo lista vuota --> conterrà (nodo_vicino, peso) per tutti i vicini del nodo team
        for n in self.G.neighbors(team): # ciclo su tutti nodi vicini al nodo team
            peso = self.G[team][n]['weight'] #dizionario degli attributi dell’arco che collega team a n.
            # ["weight] prende valore della chiave weight (ovvero peso dell'arco)
            #peso contiene la somma dei salari dei due team
            vicini.append((n,peso)) #aggiunge alla lista "vicini" la tupla(nodovicino, peso)
        return sorted (vicini, key=lambda x: x[1], reverse=True) # restituisce ordinala la lista vicini;
        # key=lambda x: x[1] → significa che l’ordinamento avviene in base al secondo elemento della tupla, cioè peso
        # reverse=True --> dal peso piu grande al piu piccolo. --> restituisce lista ordinata in ordine decrescente di peso






