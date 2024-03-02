import flet
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
)

class CalculatorIMC(UserControl):
    def nivelPeso(self):
        self.reset()
        self.result = Text(value="0",color=colors.WHITE, size=20)
        
        return Container(
            width=300,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[self.result], alignment="end"),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="AC",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="AC",
                            ),
                            ElevatedButton(
                                text="+/-",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="+/-",
                            ),
                            ElevatedButton(
                                text="%",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data="%",
                            ),
                            ElevatedButton(
                                text="/",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="/",
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="7",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="7",
                            ),
                            ElevatedButton(
                                text="8",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="8",
                            ),
                            ElevatedButton(
                                text="9",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="9",
                            ),
                            ElevatedButton(
                                text="*",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="*",
                            ),
                        ]
                    ),
                    
                    Row(
                        controls=[
                            ElevatedButton(
                                text="4",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="4",
                            ),
                            ElevatedButton(
                                text="5",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="5",
                            ),
                            ElevatedButton(
                                text="6",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="6",
                            ),
                            ElevatedButton(
                                text="-",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="-",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="1",
                            ),
                            ElevatedButton(
                                text="2",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="2",
                            ),
                            ElevatedButton(
                                text="3",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="3",
                            ),
                            ElevatedButton(
                                text="+",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="+",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="0",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=2,
                                on_click=self.button_clicked,
                                data="0",
                            ),
                            ElevatedButton(
                                text=".",
                                bgcolor=colors.WHITE24,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data=".",
                            ),
                            ElevatedButton(
                                text="=",
                                bgcolor=colors.ORANGE,
                                color=colors.WHITE,
                                expand=1,
                                on_click=self.button_clicked,
                                data="=",
                            ),
                        ]
                    ),
                ],
            ),
        )

import tkinter as tk

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
    
        imc = peso / (altura ** 2)
        resultado.set(f"Su IMC es: {imc:.2f}")
    except ValueError:
        resultado.set("Ingrese valores válidos")

    if imc.value < 18.5:
       txRango= "Bajo de peso, debe comer mas"
       Page.update()
       return
    elif imc.value >=  18.5 and  imc.value <= 25.9:
        txRango ="Normal"
        Page.update()
        return
    elif imc.value  >= 25 and imc.value <= 29.9:
        txRango ="Sobrepeso, debe comer balanciado"
        Page.update()
        return
    elif imc.value  >= 30 and imc.value <= 34.9:
        txRango ="Obesidad, debe hacer ejercio"
        Page.update()
        return
    elif imc.value  >= 35:
        txRango ="Obesidad extrema, debe ir al medico"
        Page.update()
        return


# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora de IMC")

# Variables para almacenar los datos del usuario y el resultado
entry_peso = tk.Entry(ventana)
entry_altura = tk.Entry(ventana)

resultado = tk.StringVar()

# Etiquetas y entradas para peso y altura
label_peso = tk.Label(ventana, text="Peso (kg):")
label_altura = tk.Label(ventana, text="Altura (m):")


label_peso.grid(row=0, column=0)
label_altura.grid(row=1, column=0)
entry_peso.grid(row=0, column=1)
entry_altura.grid(row=1, column=1)


# Botón para calcular el IMC
calcular_button = tk.Button(ventana, text="Calcular IMC", command=calcular_imc)
calcular_button.grid(row=2, columnspan=2)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, textvariable=resultado)
resultado_label.grid(row=3, columnspan=2)


flet.imc(target= "main")

          
      