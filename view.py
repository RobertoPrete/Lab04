import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self.__select_language = None  # menu a tendina --> Dropdown (Row1)
        self.__alert = None
        self.__type_of_search = None  # menu a tendina --> Dropdown (Row2 - parte sinistra)
        self.__text_to_check = None  # spazio dove inserire testo di ingresso --> TextField (Row2 - parte centrale)
        self.__start_correction = None  # bottone per avviare la correzione --> Elevated Button (Row2- parte destra)
        self.__out_correction = None  # area di testo di uscita della correzione --> ListView (Row3)

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title,],
                   alignment=ft.MainAxisAlignment.CENTER)
        )

        # Add your stuff here

        self.__select_language = ft.Dropdown(label="Select language", width=200, options=[ft.DropdownOption("italian"), ft.DropdownOption("english"), ft.DropdownOption("spanish")], on_change=self.__controller.handle_select_language)
        row1 = ft.Row(controls=[self.__select_language])

        self.__type_of_search = ft.Dropdown(label="Search Modality", width=300, options=[ft.DropdownOption("Default"), ft.DropdownOption("Linear"), ft.DropdownOption("Dichotomic")])
        self.__text_to_check = ft.TextField(label="Add your sentence here", expand=True,)
        self.__start_correction = ft.ElevatedButton(text="Spell Check")
        row2 = ft.Row(controls=[self.__type_of_search, self.__text_to_check, self.__start_correction])

        self.__out_correction = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        row3 = ft.Row(controls=[self.__out_correction])

        self.page.add(row1, row2, row3)

        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()

    def create_alert(self, titolo, contenuto):
        self.__alert = None
        self.__alert = ft.AlertDialog(title=titolo,
                                      content=ft.Text(value=contenuto))
        self.page.add(self.__alert)
