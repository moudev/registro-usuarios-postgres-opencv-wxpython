# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  9 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os,shutil
import sys
import wx
import wx.xrc
import sqlite3
import wx.dataview
import time
import conectPostgres as conn
import cv, cv2

###########################################################################
## Class MyFrame3
###########################################################################

class Busqueda ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Buscar Usuario", pos = wx.DefaultPosition, size = wx.Size( 1157,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Busqueda", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_textbuscar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 319,-1 ), 0 )
		fgSizer3.Add( self.m_textbuscar, 0, wx.ALL, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.listctrl = wx.ListCtrl( self, wx.ID_ANY,  wx.Point( 10,10 ), wx.Size( 800,440 ), wx.LC_REPORT|wx.SUNKEN_BORDER )
		fgSizer3.Add( self.listctrl, 0, wx.ALL, 5 )
		
		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.ruta="user.png"
		img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)
		
		self.m_bitmap5 = wx.StaticBitmap( self, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition, wx.Size( 140,140 ), 0 )
		fgSizer5.Add( self.m_bitmap5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		self.m_cambiarfoto = wx.Button( self, wx.ID_ANY, u"Cambiar foto", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_cambiarfoto, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer5.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.m_textid = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textid, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		fgSizer5.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.m_textnombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textnombre, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Apellido", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		fgSizer5.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.m_textapellido = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textapellido, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Dirección", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		fgSizer5.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_textdireccion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textdireccion, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Telefono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer5.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_texttelefono = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_texttelefono, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"DUI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		fgSizer5.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.m_textdui = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textdui, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"NIT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer5.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.m_textnit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textnit, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Modificar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		
		
		fgSizer3.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect
		
		self.listctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.seleccionar)
		self.m_textbuscar.Bind( wx.EVT_TEXT, self.busqueda )
		self.m_cambiarfoto.Bind( wx.EVT_BUTTON, self.foto )
		
		self.padre = parent
		self.ancho = 150
		self.postgres = conn.Database()
		#Evento cargar datos de encabezado a la lista y se definen las columnas que lleva el control
		self.listctrl.InsertColumn(0, 'Id', width=50)
		self.listctrl.InsertColumn(1, 'Nombre', width=250)
		self.listctrl.InsertColumn(2, 'Apellido', width=250)
		self.listctrl.InsertColumn(3, 'Direccion', width=250)
		self.listctrl.InsertColumn(4, 'Telefono', width=100)
		self.listctrl.InsertColumn(5, 'Dui', width=50)
		self.listctrl.InsertColumn(6, 'Nit', width=50)
		self.cargar_datos()
	def __del__( self ):
		self.padre.m_button2.Enable(True)
	def actualizar_datos( self, event ):
		nombre = str(self.m_textnombre.GetValue())
		apellido = str(self.m_textapellido.GetValue())
		direccion = str(self.m_textdireccion.GetValue())
		telefono = str(self.m_texttelefono.GetValue())
		dui = str(self.m_textdui.GetValue())
		nit = str(self.m_textnit.GetValue())
	
					
	def abrir_busqueda( self, event):
		busqueda = Busqueda(self)
		busqueda.Show()
		
	def busqueda(self, event):
		 self.cargar_datos()
		 
	def foto( self, event ):
		
		panel = ShowCapture(self)
		panel.Show()
		 
	def seleccionar(self, event):
		self.item ='' 
		self.item2 ='' 
		self.item = self.listctrl.GetFocusedItem() #traer la posicion del indice
		self.item2 = self.listctrl.GetItemText(self.item)#traer el texto del primera columna segun la posicion del indice
		data_param = ""
		if self.item2!="":
			numreg=0
			typesql='S'
			identificador=str(self.item2)
			sql="SELECT count(*) FROM usuarios  where id='"+identificador+"'"
			self.filas=self.postgres.query(sql,data_param,typesql)	
			for fila in self.filas:
				registros=fila[0]
			if registros>0:       
				sql="select * from usuarios where id='"+identificador+"'"
				self.rows=self.postgres.query(sql,data_param,typesql)	
		
				for row in self.rows:					           
					self.m_textid.SetValue(str(row[0]))
					self.m_textnombre.SetValue(str(row[1]))
					self.m_textapellido.SetValue(str(row[2]))
					self.m_textdireccion.SetValue(str(row[3]))
					self.m_texttelefono.SetValue(str(row[4]))
					self.m_textdui.SetValue(str(row[5]))
					self.m_textnit.SetValue(str(row[6]))	
					self.imagen = str(row[7])
					
				self.ruta = "imagenes/"+self.imagen
				if os.path.exists(self.ruta):
					self.ruta=self.ruta
					
				else:
					self.ruta="user.png"
					self.dial = wx.MessageDialog(None, 'NO EXISTE  LA IMAGEN DE ESTE USUARIO', 'ERROR', wx.OK|wx.CENTRE)
					self.dial.Show()
				img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)
				W = img.GetWidth()
				H = img.GetHeight()
					
				if W > H:
					NewW = self.ancho
					NewH = self.ancho * H / W
				else:
					NewH = self.ancho
					NewW = self.ancho * W / H
				img = img.Scale(NewW,NewH)
				self.m_bitmap5.SetBitmap(wx.BitmapFromImage(img))
				self.Refresh()
										
			else:
				print "no hay registros"
		
		
	def busqueda_fila(self, id):
		cadena_buscar=self.txt_Id.GetValue()	
		if cadena_buscar!="":
			numreg=0
			typesql='S'
			data1=str(cadena_buscar)
			data_param= {'id1':data1} 
			sql="""SELECT count(*) FROM empleado  where id=:id1"""
			self.filas=self.db.query(sql,data_param,typesql)	
			for fila in self.filas:
				numreg=fila[0]
			if numreg>0:       
				sql="""select * from empleado where id=:id1"""
				self.rows=self.db.query(sql,data_param,typesql)	
		
				for row in self.rows:					           
					self.txt_Dui.SetValue(str(row[1]))
					self.txt_Nombre.SetValue(str(row[2]))
					self.txt_Edad.SetValue(str(row[3]))
					self.txt_Direccion.SetValue(str(row[4]))
					self.txt_Nit.SetValue(str(row[5]))
					self.txt_Salario.SetValue(str(row[6]))

					if row[8] is None: #row[8] es la posicion del cursor del campo imagen
						self.ruta='imgs/blank_img.png'
					else:			
						fout = open('newimg.jpg','wb') # Crear archivo para escribir imagen
						fout.write(str(row[8]))  #Escribir imagen desde Bd a otro Archivo en disco
						fout.close()
						self.ruta='newimg.jpg' 	
			else:
				self.txt_Dui.SetValue("")
				self.txt_Nombre.SetValue("")
				self.txt_Edad.SetValue("")
				self.txt_Direccion.SetValue("")
				self.txt_Nit.SetValue("")
				self.txt_Salario.SetValue("")
				
				self.ruta='imgs/blank_img.png'		
			self.VerImagen(self.ruta) #Llamar al metodo para ver la imagen

		 
	def cargar_datos(self):
		#evento para cargar datos de la bd a la lista de 2 maneras todos si el ctrl texto esta vacio 
		#o dependiendo de la busqueda con like asi muestra los resultados
		self.listctrl.DeleteAllItems() # quita los renglones de la lista
		self.buscar = str(self.m_textbuscar.GetValue())	
		if self.buscar!="":
			self.cadena_busqueda="%"+str(self.buscar)+"%"
			sql="select * from usuarios where nombre like '"+ self.cadena_busqueda+"'  or apellido like '"+ self.cadena_busqueda+"'   order by id"
			data_param=''
			typesql='SL'
			print sql
			self.rows=self.postgres.query(sql,data_param,typesql)
		else:	
			sql="""select * from usuarios order by id"""
			data_param=''
			typesql='S'
			self.rows=self.postgres.query(sql,data_param,typesql)	
		self.row_count = 0
		#al tener el cursor se van insertando las columnas
		for row in self.rows:
			self.listctrl.InsertStringItem(self.row_count, str(row[0])) #Para insertar el indice de la fila pero del control va en la posicion columna 0
			self.listctrl.SetStringItem(self.row_count,1, str(row[1])) #en la fila insertada columna 1, se inserta el valor que queremos
			self.listctrl.SetStringItem(self.row_count,2, str(row[2])) #en la fila insertada columna 2, se inserta el valor siguiente 
			self.listctrl.SetStringItem(self.row_count,3, str(row[3]))
			self.listctrl.SetStringItem(self.row_count,4, str(row[4]))
			self.listctrl.SetStringItem(self.row_count,5, str(row[5]))
			self.listctrl.SetStringItem(self.row_count,6, str(row[6]))
						
			if self.row_count % 2:
				self.listctrl.SetItemBackgroundColour(self.row_count, "cyan")
			else:
				self.listctrl.SetItemBackgroundColour(self.row_count, "yellow")
			self.row_count += 1	   


class MyApp(wx.App):
    def OnInit(self):
        frame = Busqueda(None)
        self.SetTopWindow(frame)
        frame.Show()
        
        return 1
# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
    
