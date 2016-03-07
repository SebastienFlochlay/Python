
import pathlib

from tkinter import Tk, Frame, Text, filedialog, messagebox, END

class Application(Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        # création de la fenêtre et de son champ texte
        self.fenetre = Frame(self)
        self.zone_de_texte = Text(self.fenetre, height=20, width=40)
        self.zone_de_texte.pack()
        self.fenetre.pack()

    def obtenir_fichier_profile(self):
        # ouverture d'une invite à choisir un dossier
        dossier_de_profile = filedialog.askdirectory()
        if not dossier_de_profile:
            sys.exit(0)
        

        historique = pathlib.Path(dossier_de_profile) / "places.sqlite"

        # Vérifier que le fichier d'historique existe
        if not historique.is_file():
            messagebox.showwarning(
                "Erreur", 
                "Impossible de trouver le fichier de l'historique"
            ) 
            sys.exit(0)

        return historique

    def append_text(self, string):
        self.zone_de_texte.insert(END, string)