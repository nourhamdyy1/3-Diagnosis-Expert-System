import PySimpleGUI as pg

# set the theme
pg.theme("DarkAmber")
layout = [
    [pg.Text("enter name:")],
    [pg.InputText()],
    [pg.Text("enter your age:")],
    [pg.InputText()],

    [pg.Text("How bad is the fever?", size=(15, 1)),
     pg.Radio("0", group_id=1),
     pg.Radio("1", group_id=1),
     pg.Radio("2", group_id=1),
     pg.Radio("3", group_id=1),
     ],

    [pg.Text("What frequency of spots on the skin?", size=(15, 1)),
     pg.Radio("0", "group2"),
     pg.Radio("1", "group2"),
     pg.Radio("2", "group2"),
     pg.Radio("3", "group2"),
     ],

    [pg.Text("  How often does muscle pain occur?", size=(15, 1)),
     pg.Radio("0", "group3"),
     pg.Radio("1", "group3"),
     pg.Radio("2", "group3"),
     pg.Radio("3", "group3"),
     ],

    [pg.Text("What is the intensity and frequency/intensity of joint pain?", size=(15, 1)),
     pg.Radio("0", "group4"),
     pg.Radio("1", "group4"),
     pg.Radio("2", "group4"),
     pg.Radio("3", "group4"),
     ],
    [pg.Text("  Do you have conjunctivitis?", size=(15, 1)),
     pg.Radio("True", "group5"),
     pg.Radio("False", "group5"),

     ],

    [pg.Text("What is the intensity of joint swelling?", size=(15, 1)),
     pg.Radio("0", "group6"),
     pg.Radio("1", "group6"),
     pg.Radio("2", "group6"),
     pg.Radio("3", "group6"),
     ],

    [pg.Text("What is the intensity/frequency of the headaches?", size=(15, 1)),
     pg.Radio("0", "group7"),
     pg.Radio("1", "group7"),
     pg.Radio("2", "group7"),
     pg.Radio("3", "group7"),
     ],

    [pg.Text("How intense is the skin sensitivity (itch)?", size=(15, 1)),
     pg.Radio("0", "group8"),
     pg.Radio("1", "group8"),
     pg.Radio("2", "group8"),
     pg.Radio("3", "group8"),
     ],

    [pg.Text("What is the intensity of shortness of breath?", size=(15, 1)),
     pg.Radio("0", "group9"),
     pg.Radio("1", "group9"),
     pg.Radio("2", "group9"),
     pg.Radio("3", "group9"),
     ],

    [pg.Text("How often do crack on the skin  appear?", size=(15, 1)),
     pg.Radio("0", "group10"),
     pg.Radio("1", "group10"),
     pg.Radio("2", "group10"),
     pg.Radio("3", "group10"),

     ],

    [pg.Text("Does you have  any problems neurological?", size=(15, 1)),
     pg.Radio("True", "group11"),
     pg.Radio("False", "group11")
     ],


[pg.Button("OK"), pg.Button("Cancel")]
]
window = pg.Window("Form", layout)

while True:
    event, value = window.read()
    print(event)
    print(value)
    pg.popup("the values you entered", value)
    if event == pg.WIN_CLOSED or event == "Cancel":
        break

window.close()