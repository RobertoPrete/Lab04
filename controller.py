import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = ""

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handle_alert(self, e):
        if e.control.value == "italian" or e.control.value == "spanish" or e.control.value == "english":
            self._view.create_alert("Messaggio di conferma", "Lingua selezionata correttamente")
        elif e.control.value == "Default" or e.control.value == "Linear" or e.control.value == "Dichotomic":
            self._view.create_alert("Messaggio di conferma", "Modalità di ricerca selezionata correttamente")
        else:
            self._view.create_alert("ERRORE!", "Opzione selezionata non esistente")

    def handle_Spell_Check(self, e):
        language = self._view.get_language()
        if language is None:
            self._view.create_alert("Errore!", "Selezionare una lingua")
        modality = self._view.get_modality_of_search()
        if modality is None:
            self._view.create_alert("Errore!", "Selezionare una modalità di ricerca")
        txtIn = self._view.get_text_to_check()
        if txtIn == "":
            self._view.create_alert("Errore!", "Inserire una frase da correggere")

        self._view.clear_input_text()

        e.control.value = self.handleSentence(txtIn, language, modality)
        print("valore evento", e.control.value, type(e.control.value))
        parole_errate = e.control.value[0].strip(" -")
        print("parole errate: ", parole_errate, type(parole_errate))

        self._view.output_correzione(txtIn, parole_errate, e.control.value[1])

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text