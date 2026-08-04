import flet as ft
import random as rd

def main (pagina:ft.Page):
    pagina.title = "Frase" 
    pagina.bgcolor = "#E7E7E7"
    pagina.window.height = 900  
    pagina.window.width = 1000
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER 

    lista_frases = ["Neymar Lindo",
                    "Neymar é o melhor", 
                    "Respeita o Neymar",
                    "Dê oi para o Neymar"]
    
    lista_imagens = ["ney1.jpg",
                     "ney2.jpg",
                     "ney3.jpg",
                     "ney4.jpg"]
    
    
    
    
    def mostrar_frase():
        texto.value = rd.choice (lista_frases)

        imagem.src = rd.choice (lista_imagens)


        
    botao = ft.Button(content="APERTE PARA A SURPRESA",
                      on_size_change = 40,
                      on_click=mostrar_frase)
    
    texto = ft.Text (value="")

    imagem = ft.Image(src="")
    
    

    pagina.add(botao)
    pagina.add(texto)
    pagina.add(imagem)

    
ft.run(main)