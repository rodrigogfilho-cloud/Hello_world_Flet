import flet as ft
import random as rd

def main (pagina:ft.Page):
    pagina.title = "FRASE DO DIA É" 
    pagina.window.height = 900  
    pagina.window.width = 1000
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
    

    lista_frases = ["Não deixe ninguém falar oq vc é, pq se vc deixar eles falarem oq vc é, nem vc vai saber oq vc é ",
                    "Acredite nos seus sonhos, pq com força de vontade vc chega onde vc quiser", 
                    "Nunca deixe alguém botar o dedo na sua cara, pq ai vc vai mostrar que é só mais um",
                    "Dondie quieres ?"]
    
    lista_imagens = ["img/img1.jpg",
                     "img/img2.jpg",
                     "img/img3.jpg",
                     "img/img4.jpg",
                     ]
    lista_cores = ["#f81e1e",
                   "#fbff00",
                   "#58fcfc",
                   "#ff00d4",
                   ]
   
    
    
    
    def alterar_itens():
        texto.value = rd.choice (lista_frases)
        imagem.src = rd.choice (lista_imagens)
        pagina.bgcolor = hex(rd.randint(0,16700000))
        

    botao = ft.Button(content="APERTE PARA A SURPRESA",
                      bgcolor= "#d1d1fc",
                      on_size_change = 40,
                      on_click=alterar_itens)
    
    texto = ft.Text (value="",
                     weight=ft.FontWeight.BOLD,
                    )

    imagem = ft.Image(src="")

    pagina.add(botao)
    pagina.add(texto)
    pagina.add(imagem)

    
ft.run(main)