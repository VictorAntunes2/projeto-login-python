import PySimpleGUI as sg

layout = [
    [sg.Text("Usuário")],
    [sg.Input(key="usuario")],
    [sg.Text("senha")],
    [sg.Input(key="senha")],
    [sg.Button("login")],
    [sg.Text("", key="mensagem")],
]

window = sg.Window("Login", layout=layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "login":
        senha_correta = "a123"
        usuario_correto = "Antunes17"
        usuario = value["usuario"]
        senha = value["senha"]
        if senha == senha_correta and usuario == usuario_correto:
            window["mensagem"].update("Login feito com sucesso.")
        else:
            window["mensagem"].update("Senha ou usuário incorreto.")
