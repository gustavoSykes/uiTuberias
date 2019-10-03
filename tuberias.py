import pygame
import serial
from ajustes import *

class UI:
    def __init__(self):
        #inicializa la ventana
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption(titulo)
        self.clock = pygame.time.Clock()
        self.corriendo = True
        self.fondo = pygame.image.load("imagenes/tubos.jpg")
        self.arduino = serial.Serial(puerto, velocidad)
        self.estadoBomba = False
        self.estadoev1 = False
        self.estadoev2 = False
        self.estadoev3 = False
        self.estadoev4 = False
        self.estadoev5 = False
        self.estadoev6 = False
        self.pasoBomba = False
        self.paso1 = True
        self.paso2 = True
        self.paso3 = True
        self.paso4 = True
        self.paso5 = True
        self.paso6 = True
        bomba = pygame.image.load("imagenes/bomba.png").convert_alpha()
        self.bomba = pygame.transform.scale(bomba, (61, 59))
        electrovalvula = pygame.image.load("imagenes/electrovalvula.png").convert_alpha()
        electrovalvula = pygame.transform.scale(electrovalvula, (35, 63))
        flujometro = pygame.image.load("imagenes/flujometro.png").convert_alpha()
        self.flujo1 = pygame.transform.scale(flujometro, (40, 40))
        self.flujo2 = pygame.transform.scale(flujometro, (40, 40))
        self.flujo3 = pygame.transform.scale(flujometro, (40, 40))
        self.flujo4 = pygame.transform.scale(flujometro, (40, 40))
        self.ev1 = electrovalvula
        self.ev2 = electrovalvula
        self.ev3 = electrovalvula
        self.ev4 = electrovalvula
        self.ev5 = electrovalvula
        self.ev6 = electrovalvula
        self.estadoVerde = pygame.image.load("imagenes/estadoVerde.png").convert_alpha()
        self.estadoRojo = pygame.image.load("imagenes/estadoRojo.png").convert_alpha()
        self.fuente = pygame.font.Font('freesansbold.ttf', 18)
        self.datoFlujo1 = "0 L/min"
        self.datoFlujo2 = "0 L/min"
        self.datoFlujo3 = "0 L/min"
        self.datoFlujo4 = "0 L/min"
        self.textoFlujo1 = self.fuente.render(self.datoFlujo1, True, negro, blanco)
        self.textoFlujo2 = self.fuente.render(self.datoFlujo2, True, negro, blanco)
        self.textoFlujo3 = self.fuente.render(self.datoFlujo3, True, negro, blanco)
        self.textoFlujo4 = self.fuente.render(self.datoFlujo4, True, negro, blanco)
        self.textoe1 = self.fuente.render("E1", True, negro, blanco)
        self.textoe2 = self.fuente.render("E2", True, negro, blanco)
        self.textoe3 = self.fuente.render("E3", True, negro, blanco)
        self.textoe4 = self.fuente.render("E4", True, negro, blanco)
        self.textoe5 = self.fuente.render("E5", True, negro, blanco)
        self.textoe6 = self.fuente.render("E6", True, negro, blanco)

    def new(self):
        #inicia un nuevo proceso
        self.run()

    def run(self):
        #Loop
        self.funcionando = True
        while self.funcionando:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()

    def update(self):
        datos = self.arduino.readline(self.arduino.inWaiting()).strip().decode("utf-8")
        #print(datos)
        if datos == "Bomba ENCENDIDA":
            self.estadoBomba = True
        elif datos == "Bomba APAGADA":
            self.estadoBomba = False
        if datos.split(" ")[0] == "Valvula":
            if datos.split(" ")[1] == "1":
                if datos.split(" ")[2] == "ENCENDIDA":
                    self.estadoev1 = True
                else:
                    self.estadoev1 = False
            elif datos.split(" ")[1] == "2":
                if datos.split(" ")[2] == "ENCENDIDA":
                    self.estadoev2 = True
                else:
                    self.estadoev2 = False
            elif datos.split(" ")[1] == "3":
                if datos.split(" ")[2] == "ENCENDIDA":
                    self.estadoev3 = True
                else:
                    self.estadoev3 = False
            elif datos.split(" ")[1] == "4":
                if datos.split(" ")[2] == "ENCENDIDA":
                    self.estadoev4 = True
                else:
                    self.estadoev4 = False
            elif datos.split(" ")[1] == "5":
                if datos.split(" ")[2] == "ENCENDIDA":
                    self.estadoev5 = True
                else:
                    self.estadoev5 = False
            elif datos.split(" ")[1] == "6":
                if datos.split(" ")[2] == "ENCENDIDA":
                    self.estadoev6 = True
                else:
                    self.estadoev6 = False
        if datos.split(" ")[0] == "flujometro":
            if datos.split(" ")[1] == "1":
                #print(datos.split(" ")[2])
                self.datoFlujo1 = datos.split(" ")[2] + " L/min"
            elif datos.split(" ")[1] == "2":
                self.datoFlujo2 = datos.split(" ")[2] + " L/min"
            elif datos.split(" ")[1] == "3":
                self.datoFlujo3 = datos.split(" ")[2] + " L/min"
            elif datos.split(" ")[1] == "4":
                self.datoFlujo4 = datos.split(" ")[2] + " L/min"
            if self.estadoev1:
                self.textoFlujo1 = self.fuente.render(self.datoFlujo1, True, negro, blanco)
            if self.estadoev2:
                self.textoFlujo2 = self.fuente.render(self.datoFlujo2, True, negro, blanco)
            if self.estadoev3:
                self.textoFlujo3 = self.fuente.render(self.datoFlujo3, True, negro, blanco)
            if self.estadoev4:
                self.textoFlujo4 = self.fuente.render(self.datoFlujo4, True, negro, blanco)
            #TODO: agregar lectura de flujometros...

    def events(self):
        #eventos de la ventana
        for event in pygame.event.get():
            #print(pygame.key.get_pressed())
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouseX, mouseY = pygame.mouse.get_pos()
                print("mouse pos (" + str(mouseX) + "," + str(mouseY) + ")")
                #print(mousePos[0])
                if (mouseX >= 111 and mouseX <= 149) and (mouseY >= 363 and mouseY <= 392):
                    if self.estadoBomba:
                        self.arduino.write('z'.encode())
                    else:
                        self.arduino.write('x'.encode())
                elif (mouseX >= 275 and mouseX <= 312) and (mouseY >= 177 and mouseY <= 211):
                    if self.estadoev1:
                        self.arduino.write('q'.encode())
                    else:
                        self.arduino.write('w'.encode())
                elif (mouseX >= 275 and mouseX <= 312) and (mouseY >= 521 and mouseY <= 555):
                    if self.estadoev2:
                        self.arduino.write('a'.encode())
                    else:
                        self.arduino.write('s'.encode())
                elif (mouseX >= 798 and mouseX <= 836) and (mouseY >= 177 and mouseY <= 211):
                    if self.estadoev3:
                        self.arduino.write('e'.encode())
                    else:
                        self.arduino.write('r'.encode())
                elif (mouseX >= 698 and mouseX <= 737) and (mouseY >= 519 and mouseY <= 557):
                    if self.estadoev4:
                        self.arduino.write('d'.encode())
                    else:
                        self.arduino.write('f'.encode())
                elif (mouseX >= 600 and mouseX <= 636) and (mouseY >= 367 and mouseY <= 402):
                    if self.estadoev5:
                        self.arduino.write('t'.encode())
                    else:
                        self.arduino.write('y'.encode())
                elif (mouseX >= 500 and mouseX <= 538) and (mouseY >= 522 and mouseY <= 555):
                    if self.estadoev6:
                        self.arduino.write('g'.encode())
                    else:
                        self.arduino.write('h'.encode())

            if event.type == pygame.QUIT:
                if self.funcionando:
                    self.funcionando = False
                self.corriendo = False

    def mostrarPantalla(self):
        pass

    def dibujarElementos(self):
        self.screen.blit(self.bomba, [100, 290])
        self.screen.blit(self.ev1, [275, 105])
        self.screen.blit(self.ev2, [275, 450])
        self.screen.blit(self.ev3, [800, 105])
        self.screen.blit(self.ev4, [700, 450])
        self.screen.blit(self.ev5, [600, 297])
        self.screen.blit(self.ev6, [500, 450])
        self.screen.blit(self.flujo1, [430, 132])
        self.screen.blit(self.flujo2, [350, 475])
        self.screen.blit(self.flujo3, [700, 132])
        self.screen.blit(self.flujo3, [600, 475])
        self.screen.blit(self.textoFlujo1, [435, 180])
        self.screen.blit(self.textoFlujo2, [355, 523])
        self.screen.blit(self.textoFlujo3, [705, 180])
        self.screen.blit(self.textoFlujo4, [605, 523])
                                        #+10,-25
        self.screen.blit(self.textoe1, [285, 80])
        self.screen.blit(self.textoe2, [285, 425])
        self.screen.blit(self.textoe3, [810, 80])
        self.screen.blit(self.textoe4, [710, 425])
        self.screen.blit(self.textoe5, [610, 272])
        self.screen.blit(self.textoe6, [510, 425])

        #estados
        if self.estadoBomba:
            self.screen.blit(self.estadoVerde, [112, 360])
        else:
            self.screen.blit(self.estadoRojo, [112, 360])
        if self.estadoev1:
            self.screen.blit(self.estadoVerde, [275, 175])
            self.paso1 = False
        else:
            self.screen.blit(self.estadoRojo, [275, 175])
            self.paso1 = True
        if self.estadoev2:
            self.screen.blit(self.estadoVerde, [275, 520])
            self.paso2 = False
        else:
            self.screen.blit(self.estadoRojo, [275, 520])
            self.paso2 = True
        if self.estadoev3:
            self.screen.blit(self.estadoVerde, [800, 175])
            self.paso3 = False
        else:
            self.screen.blit(self.estadoRojo, [800, 175])
            self.paso3 = True
        if self.estadoev4:
            self.screen.blit(self.estadoVerde, [700, 520])
            self.paso4 = False
        else:
            self.screen.blit(self.estadoRojo, [700, 520])
            self.paso4 = True
        if self.estadoev5:
            self.screen.blit(self.estadoVerde, [600, 365])
            self.paso5 = False
        else:
            self.screen.blit(self.estadoRojo, [600, 365])
            self.paso5 = True
        if self.estadoev6:
            self.screen.blit(self.estadoVerde, [500, 520])
            self.paso6 = False
        else:
            self.screen.blit(self.estadoRojo, [500, 520])
            self.paso6 = True

    def drawPaso1(self):
        pygame.draw.rect(self.screen, azul, (240, 148, 595, 9))
        pygame.draw.rect(self.screen, azul, (388, 148, 9, 202))
        pygame.draw.rect(self.screen, azul, (388, 341, 215, 9))

    def drawPaso2(self):
        pygame.draw.rect(self.screen, azul, (180, 493, 355, 9))

    def drawPaso3(self):
        pygame.draw.rect(self.screen, azul, (835, 148, 31, 9))
        pygame.draw.rect(self.screen, azul, (857, 148, 9, 30))

    def drawPaso4(self):
        pygame.draw.rect(self.screen, azul, (735, 493, 122, 9))
        pygame.draw.rect(self.screen, azul, (857, 493, 9, 41))

    def drawPaso5(self):
        pygame.draw.rect(self.screen, azul, (603, 341, 177, 9))
        pygame.draw.rect(self.screen, azul, (771, 341, 9, 152))
        pygame.draw.rect(self.screen, azul, (735, 493, 122, 9))

        pygame.draw.rect(self.screen, azul, (857, 493, 9, 41))

    def drawPaso6(self):
        pygame.draw.rect(self.screen, azul, (535, 493, 200, 9))

    def drawPasoBomba(self):
        pygame.draw.rect(self.screen, azul, (180, 148, 9, 354))
        pygame.draw.rect(self.screen, azul, (150, 317, 39, 9))
        pygame.draw.rect(self.screen, azul, (180, 148, 100, 9))
        pygame.draw.rect(self.screen, azul, (180, 493, 100, 9))

    def draw(self):
        self.screen.blit(self.fondo, [0, 0])
        if self.estadoBomba:
            self.drawPasoBomba()
            if not self.paso1:
                self.drawPaso1()
                if not self.paso3:
                    self.drawPaso3()
                if not self.paso5:
                    self.drawPaso5()
            if not self.paso2:
                self.drawPaso2()
                if not self.paso6:
                    self.drawPaso6()
                    if not self.paso4:
                        self.drawPaso4()
        self.dibujarElementos()
        pygame.display.flip()

ui = UI()
ui.mostrarPantalla()
while ui.corriendo:
    ui.new()
    ui.mostrarPantalla()

pygame.quit()
