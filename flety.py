import flet as ft
import random 

def main (pagina:ft.Page):
    pagina.title = "Super programa do Godoy com Flet" #Alterando o título da janela
    pagina.bgcolor = "#E7E7E7" # Alterando cor da janela
    pagina.window.height = 900  # Alterando altura da janela
    pagina.window.width = 1700 # Alternado a largura da janela
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Alterar posição horizontal do meu texto

    


    # Criando um componente de texto

    texto_grito = ft.Text(value="OHHH", 
                          color= "#ffffff",
                          size= 40,
                          bgcolor="#C70000",
                          
                        
                          )
    
    texto_hello = ft.Text(value="""Toca no Calleri""", 
                          color= "#fa1f1f",
                          size= 40,
                          italic=True,
                          bgcolor="#FFFFFFFF",
                        
                          )
    
    texto_bem_vindo = ft.Text(value="Que é golll", 
                          color= "#ffffff",
                          size= 40,
                          bgcolor="#C70000",
                          
                        
                          )
    
    def mostrar_imagem():
        if imagem.visible == True:
            imagem.visible = False
        else: 
            imagem.visible = True

    
        

     
    botao = ft.Button(content="Clique Aqui",
                      bgcolor = "#000000FF",
                      color= "#ffffff",
                      on_click=mostrar_imagem,
                      )
    

    

    
  
    imagem = ft.Image(
                        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRz6elj2q5Bc0Z4a3W_1UF8GhpZ8SA18l2LHwNx0jyPjQ&s=10",
                        width= 300,
                        height=300,
                       border_radius=100,
                       visible= False)
    
    
    
    pagina.add(texto_grito)
    pagina.add(texto_hello)
    pagina.add(texto_bem_vindo)
    pagina.add(imagem)
    pagina.add(botao)

    pagina.update()
    
    

ft.run(main)

