#rozbudowany moduł obsługi Aplikacju
import GUI_DESIGNER
import Lista_portow

from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets

import serial
import time


class Dodane_funkcje(GUI_DESIGNER.Ui_MainWindow):
	
	def setupUi(self,master):
		super(Dodane_funkcje,self).setupUi(master)
		
		#Metoda utworzenia zdarzeń dla SerialPortów
		i=0
		for item in self.akcja:
			item.triggered.connect(partial(self.serial, i))
			i+=1
		
		self.ustawienia_poczatkowe()
		# Ustawienie wszyskich przyciskow
	def ustawienia_poczatkowe(self):
		self.stan_checkButton = 1
		self.stan_pomiar = 0
		self.Kontrola_diod_check.clicked.connect(self.ustawienie_check)
		#self.pushButton.clicked.connect(self.pomiar)
		#self.timer = QtCore.QTimer()
		#self.timer.timeout.connect(self.funkcja_timer)
	# Metoda tworząca port
	def serial(self,wartosc):		
		print("NOWE POLACZENIE Z PORTEM : "+self.porty[wartosc]+". ")
		self.port = self.porty[wartosc]
		SERIAL = serial.Serial(self.port)
		try:
			self.reset_funkcji()
		except: """"""
		SERIAL.write(b'#01*00+')
		if self.stan_checkButton == 0:
			self.stan_checkButton = 1
			self.ustawienie_check()

	def ustawienie_funkcji(self):
		#sprawdza czy jest połaczony Port 
		try:	SERIAL = serial.Serial(self.port)
		except: 
			print("sprawdz czy wybrany odpowiedni port")
			return 0
			
		self.Button_ON_Dioda1.clicked.connect(self.d1_pressed_on)
		self.Button_ON_Dioda2.clicked.connect(self.d2_pressed_on)
		self.Button_ON_Dioda3.clicked.connect(self.d3_pressed_on)
        
		self.Button_OFF_Dioda1.clicked.connect(self.d1_pressed_off)
		self.Button_OFF_Dioda2.clicked.connect(self.d2_pressed_off)
		self.Button_OFF_Dioda3.clicked.connect(self.d3_pressed_off)
		
    #reset funkcji gdy checkbutton nie jest wciśnięty
	def reset_funkcji(self):
		try:	SERIAL = serial.Serial(self.port)
		except: 
			print("sprawdz czy wybrany odpowiedni port")
			return 0
			
		SERIAL.write(b'#01*00+')
		SERIAL.close()
		self.Button_ON_Dioda1.clicked.disconnect()
		self.Button_ON_Dioda2.clicked.disconnect()
		self.Button_ON_Dioda3.clicked.disconnect()
		self.Button_OFF_Dioda1.clicked.disconnect()
		self.Button_OFF_Dioda2.clicked.disconnect()
		self.Button_OFF_Dioda3.clicked.disconnect()
	#ustawienie funkcji gdy checkbutton nie jest wciśnięty
	def ustawienie_check(self):
		if(self.stan_checkButton):
			self.checked_on()
			self.stan_checkButton = 0
			self.ustawienie_funkcji()
		else:
			self.checked_off()
			self.stan_checkButton=1
			self.reset_funkcji()
			MainWindow.update()
			
	# METODY OBSLUGUJĄCE KLAWISZE		
	def d1_pressed_on(self):
		#otwarcie portu i wyslanie danych
		SERIAL = serial.Serial(self.port)
		SERIAL.write(b'#01*11+')
		SERIAL.close()
		print("DIODA 1 ZAPALONA")
	def d2_pressed_on(self):
		self.SERIAL = serial.Serial(self.port)
		self.SERIAL.write(b'#01*21+')
		self.SERIAL.close()
		print("DIODA 2 ZAPALONA")
	def d3_pressed_on(self):
		self.SERIAL = serial.Serial(self.port)
		self.SERIAL.write(b'#01*31+')
		self.SERIAL.close()
		print("DIODA 3 ZAPALONA")
	def d1_pressed_off(self):
		SERIAL = serial.Serial(self.port)
		SERIAL.write(b'#01*10+')
		SERIAL.close()
		print("DIODA 1 ZGASZONA")
	def d2_pressed_off(self):
		SERIAL = serial.Serial(self.port)
		SERIAL.write(b'#01*20+')
		SERIAL.close()
		print("DIODA 2 ZGASZONA")
	def d3_pressed_off(self):
		SERIAL = serial.Serial(self.port)
		SERIAL.write(b'#01*30+')
		SERIAL.close()
		print("DIODA 3 ZGASZONA")
		
    # GDY CHECKBUTTON WCISNIETY MOZNA DOKONAC WYBORU
	def checked_on(self):
		print("pressed")
		self.Button_OFF_Dioda1.setCheckable(True)
		self.Button_OFF_Dioda2.setCheckable(True)
		self.Button_OFF_Dioda3.setCheckable(True)
        
		self.Button_ON_Dioda1.setCheckable(True)
		self.Button_ON_Dioda2.setCheckable(True)
		self.Button_ON_Dioda3.setCheckable(True)
		
		self.Button_OFF_Dioda1.setChecked(True)
		self.Button_OFF_Dioda2.setChecked(True)
		self.Button_OFF_Dioda3.setChecked(True)
		        
    # GDY CHECKBUTTON NIE WCISNIETY NIE MOZNA DOKONAC WYBORU
	def checked_off(self):
		
		self.Button_OFF_Dioda1.setCheckable(False)
		self.Button_OFF_Dioda2.setCheckable(False)
		self.Button_OFF_Dioda3.setCheckable(False)
        
		self.Button_ON_Dioda1.setCheckable(False)
		self.Button_ON_Dioda2.setCheckable(False) 
		self.Button_ON_Dioda3.setCheckable(False)
<<<<<<< HEAD
	
	#metoda pomiaru
=======
			
>>>>>>> 8a36c82cf1726592be779c0998b5e71fb455a216
	def pomiar(self):
		if self.stan_pomiar == 0:
			self.timer.start(1000)
			self.stan_pomiar = 1
		elif self.stan_pomiar == 1:
			self.timer.stop()
			self.stan_pomiar=0
			
	#metoda pomiaru cyklicznego
	def funkcja_timer(self):
		SERIAL = serial.Serial(self.port)
		SERIAL.write(b'#02*11+')
		zdanie = SERIAL.readline().decode('utf-8')
		if zdanie == '\n':
			zdanie = SERIAL.readline().decode('utf-8')
		##zdanie += ch
		
		print(zdanie)
		SERIAL.close()
		self.lcdNumber.display(zdanie)

import sys
porty = Lista_portow.funkcja_zwrotu_portow()
print(porty)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Dodane_funkcje()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

