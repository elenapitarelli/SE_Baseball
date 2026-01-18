import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e): #attiva il grafo
        """ Handler per gestire creazione del grafo """""
        year = int(self._view._dd_anno.value)

        try:
            year = int(year)
        except Exception:
            self._view.show_alert("inserisci un anno valido")
            return

        self._model.costruisci_grafo(year)




    def handle_dettagli(self, e): #attiva il pulsante dettagli
        """ Handler per gestire i dettagli """""
        team_id = int(self._view.dd_squadra.value) # valore ID da dd e lo traforma in intero

        team = self._model._id_map.get(team_id) # cerco oggetto team corrispondente all id nella mappa
        if team_id not in self._model._id_map:
            print("Team non presente nel grafo:", team_id)
            self._view.update()
            return
        self._view.txt_risultato.controls.clear()
        for n, peso in self._model.get_vicini(team_id): # richiamo funzionenel model che restituisce lista vicini ordinata per peso
            team_vicino = self._model._id_map[n]
            self._view.txt_risultato.controls.append(
                ft.Text(f"{team_vicino.name} ({team_vicino.team_code}) - peso {peso}")
            ) # per pgni vicino n e suo peso, crea controllo di testo, aggiungendolo alla listview nella view
        self._view.txt_risultato.update()


    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO

    """ Altri possibili metodi per gestire di dd_anno """""
    def get_years(self):
        return self._model.get_years()


    def handle_change(self, e):
        self._view.dd_squadra.options.clear()
        year = int(self._view._dd_anno.value)
        teams = self._model.get_teams(year) # chiedo le squadre di quell'anno

        self._view.txt_out_squadre.controls.clear()
        self._view.txt_out_squadre.controls.append(ft.Text(f"Numero squadre : {len(teams)}"))

        for t in teams:
            self._view.txt_out_squadre.controls.append(ft.Text(f"{t}"))


        self._view.dd_squadra.options = [ft.dropdown.Option(key=t.id, text= t.name) for t in teams]


        self._view.update()

