import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        for nome in self._model.get_biblioteche():
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(nome))
        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for genere in self._model.get_generi():
            self._view.dd_genere.options.append(ft.dropdown.Option(genere))
    # CALLBACKS DROPDOWN
    def handler_biblioteca(self,e):
        scelta =e.control.value
        if scelta =="Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = scelta
    def handler_genere(self, e):
        scelta = e.control.value
        if scelta == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = scelta

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self,e):
        self._view.lv_libri.controls.clear()
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        if len(libri) == 0:
            self._view.show_alert("Nessun libro trovato con questi filtri")
        else:
            for l in libri:
                testo = f"{l['titolo']} - {l['autore']} ({l['genere']}, {l['anno_pubblicazione']}) - {l['biblioteca']} "
                self._view.lv_libri.controls.append(ft.Text(testo))
        self._view.update()
