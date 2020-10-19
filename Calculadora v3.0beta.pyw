# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:28:13 2020

@author: JOSE-PC
"""

import sys
import operator
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QLCDNumber
from math import sin, cos, tan, log, factorial, pi, sqrt
from PyQt5.QtGui import QIcon
import qtawesome as qta
from PyQt5 import uic

        
READY = 0
INPUT = 1



class Calculadora(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("Calculadora.ui",self)
        self.setWindowTitle("Calculadora")
        self.setWindowIcon(QIcon('calculadora.ico'))
        
        self.setFixedSize(376, 320)
        
        self.stack = None
        
        
    
        # conteo de numeros
        for n in range(0, 10):
            getattr(self, 'btn_n%s' % n).pressed.connect(lambda v=n: self.entrada_numeros(v))
        
        # llamado de funciones
        self.boton_suma.pressed.connect(lambda: self.operacion(operator.add))
        self.boton_resta.pressed.connect(lambda: self.operacion(operator.sub))
        self.boton_multiplicacion.pressed.connect(lambda: self.operacion(operator.mul))
        self.boton_division.pressed.connect(lambda: self.operacion(operator.truediv))
        
        self.boton_seno.clicked.connect(self.seno)
        self.boton_coseno.clicked.connect(self.coseno)
        self.boton_tangente.clicked.connect(self.tangente)
        self.boton_log.clicked.connect(self.logaritmo)
        self.boton_factorial.clicked.connect(self.fact)
        self.boton_porcentage.pressed.connect(self.operacion_porcentage)
        self.btn_igual.pressed.connect(self.igualdad)
        self.boton_cambiarsigno.clicked.connect(self.cambio_signo)
        self.radioButton_decimal.pressed.connect(self.number_decimal)
        self.radioButton_binario.pressed.connect(self.number_binario)
        self.radioButton_octal.pressed.connect(self.number_octal)
        self.radioButton_hexadecimal.pressed.connect(self.number_hexadecimal)
        self.boton_potencia_2.clicked.connect(self.potencia_2)
        self.boton_potencia_3.clicked.connect(self.potencia_3)
        self.boton_raiz.clicked.connect(self.Raiz)
        self.boton_back.clicked.connect(self.boton_Back)
        self.btn_clear.pressed.connect(self.clear)
        self.boton_history.pressed.connect(self.datos_almacenados)
        self.boton_rellamada.pressed.connect(self.rellamada_datos)
        self.boton_back.setIcon(qta.icon('fa5s.backspace'))
        self.boton_pi.clicked.connect(self.boton_Pi)
        
        
        
        if self.radioButton_decimal.isChecked():
            self.display_number.setMode(QLCDNumber.Dec)
        elif self.radioButton_binario.isChecked():
            self.display_number.setMode(QLCDNumber.Bin)
        elif self.radioButton_octal.isChecked():
            self.display_number.setMode(QLCDNumber.Oct)
        elif self.radioButton_hexadecimal.isChecked():
            self.display_number.setMode(QLCDNumber.Hex)

        self.memory = 0
        self.clear()
        self.menu_Bar()
        
        
    def display(self):
        self.display_number.display(round(self.stack[-1], 2))
            
            
            
    def clear(self):
        
        self.state = READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None
        self.display()
        

    def datos_almacenados(self):
        self.memory = self.display_number.value()

    def rellamada_datos(self):
        self.state = INPUT
        self.stack[-1] = self.memory
        self.display()
        
    def entrada_numeros(self, v):
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = v
            
        else:
            self.stack[-1] = self.stack[-1] * 10 + v

        self.display()
        
        
        
    def operacion(self, op):
        if self.current_op:  
            self.igualdad()

        self.stack.append(0)
        self.state = INPUT
        self.current_op = op

    def operacion_porcentage(self):
        self.state = INPUT
        self.stack[-1] *= 0.01
        self.display()
        

    def igualdad(self):
        
        if self.state == READY and self.last_operation:
            s, self.current_op = self.last_operation
            self.stack.append(s)

        if self.current_op:
            self.last_operation = self.stack[-1], self.current_op

            self.stack = [self.current_op(*self.stack)]
            self.current_op = None
            self.state = READY
            self.display()
        
            
            
    def boton_Back(self):
        self.stack[-1] = int(self.stack[-1] / 10)    
        self.display()

    
    def boton_Pi(self):
        self.stack[-1] = pi
        self.display()

   
         

         
    def potencia_2(self):
        self.stack[-1] = pow(self.stack[-1], 2)
        self.display()
        
    def potencia_3(self):
        self.stack[-1] = pow(self.stack[-1], 3)
        self.display()
        
    def Raiz(self):
        self.stack[-1] = sqrt(self.stack[-1])
        self.display()
       
    
         
    def cambio_signo(self):
        self.stack[-1] *= -1
        self.display()
        
        
    def number_decimal(self):
        
        self.display_number.setMode(QLCDNumber.Dec)
        
    def number_binario(self):
        
        self.display_number.setMode(QLCDNumber.Bin)
        
    def number_octal(self):
        self.display_number.setMode(QLCDNumber.Oct)
        
    def number_hexadecimal(self):
        
        self.display_number.setMode(QLCDNumber.Hex)
        
        

    def seno(self):
        
        
        if self.radianes.isChecked():
            
            
                self.stack[-1] = round(sin(self.stack[-1]),3)
                self.display()

                
        elif self.angulos.isChecked():
                
                self.stack[-1] = round(sin((self.stack[-1]*pi)/180),3)
                self.display()
  
            
    def coseno(self):
        
  
        if self.radianes.isChecked():
            
            
                self.stack[-1] = round(cos(self.stack[-1]),3)
                self.display()

                
        elif self.angulos.isChecked():
                
                self.stack[-1] = round(cos((self.stack[-1]*pi)/180),3)
                self.display()
                       
        

            
    def tangente(self):
        
        if self.radianes.isChecked():
            
            
                self.stack[-1] = round(tan(self.stack[-1]),3)
                self.display()

                
        elif self.angulos.isChecked():
                
                self.stack[-1] = round(tan((self.stack[-1]*pi)/180),3)
                self.display()
            

                
    def logaritmo(self):

        
        self.stack[-1] = round(log(self.stack[-1],10),3)
        self.display()

        
        
    def fact(self):
        
        self.stack[-1] = round(factorial(self.stack[-1]))
        self.display()
        
        
    # Creacion de Barra de menu
        
    def menu_Bar(self):
        
        menu = self.menuBar()
        menu.setStyleSheet('color: white ; background-color: #444444')
        
        
        # Menu Archivo
        menu_archivo = menu.addMenu("&Archivo")
        file_action = QAction(qta.icon('fa5.times-circle'), '&Exit', self)
        file_action.setShortcut('Ctrl+Q')
        file_action.setStatusTip('Salir')
        menu_archivo.addAction(file_action)
        file_action.triggered.connect(QApplication.instance().closeAllWindows)
        
        # Menu ayuda
        menu_ayuda = menu.addMenu("&Ayuda")
        
        about_action = QAction(qta.icon('fa5s.info-circle'), '&Acerca de...', self)
        about_action.setShortcut('Ctrl+I')
        about_action.setStatusTip('Informacion')
        
        about_program = QAction(qta.icon('fa5s.hammer'), '&¿Que hay de nuevo?', self)
        about_program.setShortcut('Ctrl+U')
        
        
        menu_ayuda.addAction(about_action)
        about_action.triggered.connect(self.info)
        
        menu_ayuda.addAction(about_program)
        about_program.triggered.connect(self.upgrades)
        
        
    def info(self):
        
        msg = QMessageBox()
        
        msg.setStyleSheet('background-color: rgb(35, 35, 35); color: gray ')
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Acerca de...")
        msg.setWindowIcon(QIcon('calculadora.ico'))
        msg.setText(" Creador:  Ing.Viamontes\n Organizacion:  Universidad de Oriente\n Grupo de trabajo:  Bioteam\n version:  3.0beta")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()
        
    def upgrades(self):
        upgrades = QMessageBox()
        upgrades.setWindowTitle('¿Que hay de nuevo?')
        upgrades.setWindowIcon(qta.icon('fa5s.hammer'))
        upgrades.setStyleSheet('background-color: rgb(35, 35, 35); color: gray ')
        upgrades.setText('- Mejoramiento de la Interfaz\n- Reducción y optimización de lineas de código\n- Nuevos botones con sus respectivas funcionalidades\n- Adaptación de un lcd númerico como display\n- Conversión a sistemas numericos')
        upgrades.exec_()
        
    
app = QApplication(sys.argv)
app.setStyle("Fusion")
ventana = Calculadora()
ventana.show()
app.exec_()