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
## Class MyFrame2
###########################################################################



class Menu ( wx.Frame ):
	
	def __init__( self, parent ):
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Welcome", pos = wx.DefaultPosition, size = wx.Size( 268,220 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"MENU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 12, 74, 90, 92, False, "Sans" ) )
		fgSizer1.Add( self.m_staticText1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"r.png", wx.BITMAP_TYPE_ANY ) , wx.DefaultPosition,wx.Size( 90,90 ), wx.BU_AUTODRAW )
		fgSizer1.Add( self.m_bpButton1, 0, wx.ALL, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button2 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"busqueda.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size(90,90), wx.BU_AUTODRAW )
		fgSizer1.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.abrir_registro )
		self.m_button2.Bind( wx.EVT_BUTTON, self.abrir_busqueda )
		
		self.postgres = conn.Database()
		
	def __del__( self ):
		pass
	def abrir_busqueda( self, event):
		busqueda = Busqueda(self)
		busqueda.Show()
		
		self.m_button2.Disable()
		
	def abrir_registro( self, event):
		registre= registro(self)
		registre.Show()
		self.m_bpButton1.Disable()
		
class registro ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Registro", pos = wx.DefaultPosition, size = wx.Size( 490,450), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 490,450 ), wx.Size( 490,450) )#haciendo que siempre el formulario tenga las misms dimensiones
		self.Bind( wx.EVT_ACTIVATE, self.actualizarBitmap )#evento para actualizar el bitmap luego de tomar la foto
		
		self.postgres = conn.Database()
		
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer2.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.txt_nombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_nombre, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		#####
		
		self.ruta="orig_frame.jpg"
		
		if os.path.exists(self.ruta):
			os.remove(self.ruta)
			self.ruta="user.png"
			print "Habia foto, pero se a eliminado"
			
		else:
			self.ruta="user.png"
			print "NO existia imagen de usuario en el sistema"
		img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)
		
		self.ancho = 150
		self.alto = 200
		
		##bitmap
		
		
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition, wx.Size( 140,140 ), 0 )
		fgSizer2.Add( self.m_bitmap1, 0, wx.ALL, 5 )
		
		self.user = wx.StaticText( self, wx.ID_ANY, u"Apellido:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.user.Wrap( -1 )
		fgSizer2.Add( self.user, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_apellido = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_apellido, 0, wx.ALL, 5 )
		
		self.btn_foto = wx.Button( self, wx.ID_ANY, u"Foto", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn_foto, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Dirección", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_dir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_dir, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Teléfono:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer2.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_tel = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_tel, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"DUI:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer2.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_dui = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_dui, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"NIT:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.txt_nit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_nit, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn_guardar = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn_guardar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn_cancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn_cancelar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( fgSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
		
		# Connect Events
		self.btn_guardar.Bind( wx.EVT_BUTTON, self.guardar )
		self.btn_cancelar.Bind( wx.EVT_BUTTON, self.cancelar )
		self.btn_foto.Bind( wx.EVT_BUTTON, self.foto )
		
		self.padre = parent
		
	
	def __del__( self ):
		self.padre.m_bpButton1.Enable(True)
		
	
	def abrir_registro( self, event ):
		registro = registro(self)
		registro.Show()
		self.m_bpButton1.Enable(False)	
	
	
		
	def foto( self, event ):
		
		panel = ShowCapture(self)
		panel.Show()
	
	#funcion para actualizar el bitmap luego de tomar la foto, o cada vez que el foco cambie
	#hacia el formulario de registro, consiste en; tomar la ultima fotografia de un usuario, en este
	#caso, la foto que se acaba de tomar del usuario, para intercambiarla por la que ya estaba, que era
	#la silueta de un user png, y refrescamos el bitmap, para que haga el cambio automatico
	def actualizarBitmap(self, event):
		print "Focus"
		self.ruta="orig_frame.jpg"
		if os.path.exists(self.ruta):
			
			self.ruta="orig_frame.jpg"
			print "Habia foto"
			
		else:
			self.ruta="user.png"
			print "NO existia imagen de usuario en el sistema"
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
		self.m_bitmap1.SetBitmap(wx.BitmapFromImage(img))
		self.Refresh()
	
	
	
	# Virtual event handlers, overide them in your derived class
	def guardar( self, event ):
		self.nombre = str(self.txt_nombre.GetValue())
		self.apellido = str(self.txt_apellido.GetValue()) 
		self.direc = str(self.txt_dir.GetValue()) 
		self.telefono = str(self.txt_tel.GetValue()) 
		self.dui = str(self.txt_dui.GetValue()) 
		self.nit = str(self.txt_nit.GetValue())

		
		sql1= "INSERT INTO usuarios(nombre,apellido,direccion) VALUES ('', '','')"
		data_param=("")
		typesql='I'
		self.postgres.query(sql1,data_param,typesql)
		self.jpg = self.nombreImg()
		self.ultimo = self.ultimoId()
		sql="update  usuarios  set nombre='"+self.nombre+"', apellido='"+self.apellido+"',direccion='"+self.direc+"', telefono='"+self.telefono+"', dui='"+self.dui+"', nit='"+self.nit+"', imagen='"+self.jpg+"' where id = '"+self.ultimo+"'"
		data_param=("")
		typesql='U'
		self.dial = wx.MessageDialog(None, 'DATOS GUARDADOS CON EXITO', 'Info', wx.OK|wx.CENTRE)
		if self.postgres.query(sql,data_param,typesql):
			if self.guardarImg():
				if self.dial.ShowModal() == wx.ID_OK:
					self.Close()
			else:
				self.dial = wx.MessageDialog(None, 'IMAGEN NO GUARDADA', 'ERROR', wx.OK|wx.CENTRE)
		else:
			self.dial = wx.MessageDialog(None, 'DATOS NO GUARDADOS ERROR VERIFIQUE BIEN SUS DATOS', 'ERROR', wx.OK|wx.CENTRE)
		
	def ultimoId(self):
		sql="""select max(id) from usuarios """
		data_param=''
		typesql='S'
		self.datos = self.postgres.query(sql,data_param,typesql)	
		for dato in self.datos:
				self.id=dato[0]
				self.id=(str(self.id))
		
		return self.id
		
	def nombreImg(self):
		sql="""select max(id) from usuarios """
		data_param=''
		typesql='S'
		self.datos = self.postgres.query(sql,data_param,typesql)	
		for dato in self.datos:
				id=dato[0]
				id=(str(id))
		name_img = "user"+id+".jpg"
		return name_img
		
	def nombreImg2(self):
		sql="""select max(id) from usuarios """
		data_param=''
		typesql='S'
		self.datos = self.postgres.query(sql,data_param,typesql)	
		for dato in self.datos:
				id=dato[0]+1
				id=(str(id))
		name_img = "user"+id+".jpg"
		print name_img
		return name_img
		
	def guardarImg(self):
		self.user_png = self.nombreImg()
		ruta = str(os.getcwd())+"/imagenes"
		print ruta
		if os.path.exists(ruta):
			self.moverImg()
			return True
		else:
			os.mkdir("imagenes", 0o777)
			self.moverImg()
			return True
			
	
	def moverImg(self):
		if os.path.exists("orig_frame.jpg"):
			os.rename("orig_frame.jpg", self.user_png)
			if os.path.exists("imagenes/"+self.user_png):
				print "Habia imagen con el mismo usuario pero se a borrado"
				os.remove("imagenes/"+self.user_png)
				shutil.move(self.user_png ,"imagenes")
			else:
				shutil.move(self.user_png ,"imagenes")
			print "Movido y renombrado con exito"
		else:
			print "No existe foto de usuario para guardar"
	
	
	
	def cancelar( self, event ):
		self.Close()
		event.Skip()
		


class Busqueda ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Buscar Usuario", pos = wx.DefaultPosition, size = wx.Size( 1157,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT ) )
		
		self.Bind( wx.EVT_ACTIVATE, self.actualizarBitmap )#evento para actualizar el bitmap luego de tomar la foto
		
		
		
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
		
		
		#####
		
		self.ruta="orig_frame.jpg"
		
		if os.path.exists(self.ruta):
			os.remove(self.ruta)
			self.ruta="user.png"
			print "Habia foto, pero se a eliminado"
			
		else:
			self.ruta="user.png"
			print "NO existia imagen de usuario en el sistema"
		img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)
		
		self.ancho = 150
		self.alto = 200
		
		##
		
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
		
		self.m_textid = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
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
		
		self.m_modificar = wx.Button( self, wx.ID_ANY, u"Modificar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_modificar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_eliminar = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_eliminar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
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
		self.m_modificar.Bind( wx.EVT_BUTTON, self.modificar )
		self.m_eliminar.Bind( wx.EVT_BUTTON, self.eliminar )
		
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
	
					
	def abrir_busqueda( self, event):
		busqueda = Busqueda(self)
		busqueda.Show()
		
	def busqueda(self, event):
		 self.cargar_datos()
		 
	def foto( self, event ):
		
		panel = ShowCapture(self)
		panel.Show()
		
	def modificar(self, event):
		id = str(self.m_textid.GetValue())
		self.nombre = str(self.m_textnombre.GetValue())
		self.apellido = str(self.m_textapellido.GetValue())
		self.direccion = str(self.m_textdireccion.GetValue())
		self.telefono = str(self.m_texttelefono.GetValue())
		self.dui = str(self.m_textdui.GetValue())
		self.nit = str(self.m_textnit.GetValue())
		jpg = "user"+id+".jpg"
		sql="update usuarios set nombre='"+self.nombre+"', apellido='"+self.apellido+"',direccion='"+self.direccion+"', telefono='"+self.telefono+"', dui='"+self.dui+"', nit='"+self.nit+"' , imagen ='"+jpg+"' where id='"+id+"'"
		data_param=("")
		typesql='U'
		self.dial = wx.MessageDialog(None, 'DATOS GUARDADOS CON EXITO', 'INFO', wx.OK|wx.CENTRE)
		if self.postgres.query(sql,data_param,typesql):
			if os.path.exists("orig_frame.jpg"):
				if self.moverImg(jpg):
					self.dial.ShowModal()
					self.limpiarCajas()
					self.cargar_datos()
				else:
					self.dial = wx.MessageDialog(None, 'IMAGEN NO MOVIDA', 'INFO', wx.OK|wx.CENTRE)
					self.dial.ShowModal()
			else:
				self.dial.ShowModal()
				self.limpiarCajas()
				self.cargar_datos()
			

		else:
			self.dial = wx.MessageDialog(None, 'DATOS NO GUARDADOS ERROR VERIFIQUE BIEN SUS DATOS', 'ERROR', wx.OK|wx.CENTRE)
			print "No guardados"
			self.dial.ShowModal()
			self.cargar_datos()

			
		
	
	def moverImg(self,img):
		self.user_png = img
		if os.path.exists("orig_frame.jpg"):
			os.rename("orig_frame.jpg", self.user_png)
			if os.path.exists("imagenes/"+self.user_png):
				print "Habia imagen con el mismo usuario pero se a borrado"
				os.remove("imagenes/"+self.user_png)
				shutil.move(self.user_png ,"imagenes")
				return True
			else:
				shutil.move(self.user_png ,"imagenes")
				return True
			print "Movido y renombrado con exito"
			
		else:
			print "No existe foto de usuario para guardar"
		
	def limpiarCajas(self):
		self.m_textid.SetValue("")
		self.m_textnombre.SetValue("")
		self.m_textapellido.SetValue("")
		self.m_textdireccion.SetValue("")
		self.m_texttelefono.SetValue("")
		self.m_textdui.SetValue("")
		self.m_textnit.SetValue("")
		
	
	def eliminar(self, event):	
		id = str(self.m_textid.GetValue())
		self.dial = wx.MessageDialog(None, '¿REALMENTE DESEA ELIMINAR ESTE REGISTRO?', 'Info', wx.OK|wx.CENTRE)
		if self.dial.ShowModal() == wx.ID_OK:
			sql="delete from usuarios where id = '"+id+"'"
			data_param=("")
			typesql='D'
			if self.postgres.query(sql,data_param,typesql):
				self.dial = wx.MessageDialog(None, 'REGISTRO ELIMINADO CON EXITO', 'Info', wx.OK|wx.CENTRE)	
				if self.dial.ShowModal() == wx.ID_OK:
					self.cargar_datos()
					self.limpiarCajas()	
			
			
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
	
	
	def foto( self, event ):
		
		panel = ShowCapture(self)
		panel.Show()
	
	#funcion para actualizar el bitmap luego de tomar la foto, o cada vez que el foco cambie
	#hacia el formulario de registro, consiste en; tomar la ultima fotografia de un usuario, en este
	#caso, la foto que se acaba de tomar del usuario, para intercambiarla por la que ya estaba, que era
	#la silueta de un user png, y refrescamos el bitmap, para que haga el cambio automatico
	def actualizarBitmap(self, event):
		print "Focus"
		self.ruta="orig_frame.jpg"
		if os.path.exists(self.ruta):
			
			self.ruta="orig_frame.jpg"
			print "Habia foto"
			
		else:
			self.ruta="user.png"
			print "NO existia imagen de usuario en el sistema"
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

		
		
		
		
class ShowCapture ( wx.Frame ):
	
	def __init__(self, parent,  fps=7):
		###
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,640 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        ## INDICE DE LA CAMARA
		capture = cv2.VideoCapture(0)
		capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, 1000)
		capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 1000)

		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, (2000,2000), wx.TAB_TRAVERSAL )
		self.m_panel1.SetMinSize( wx.Size( 400,640 ) )
		self.m_panel1.SetMaxSize( wx.Size( 400,640 ) )
		self.m_panel1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button3 = wx.Button( self.m_panel1, wx.ID_ANY, u"CAPTURA",  wx.Point( -500,-1 ), wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button3, 0, wx.ALL, 5 )
		
		####
		
		self.capture = capture

		ret, frame = self.capture.read()


		height, width = frame.shape[:2]


		parent.SetSize((width, height))


		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		

		self.bmp = wx.BitmapFromBuffer(width, height, frame)

		
		self.timer = wx.Timer(self)

		self.timer.Start(1000./fps)


		self.Bind(wx.EVT_PAINT, self.OnPaint)

		self.Bind(wx.EVT_TIMER, self.NextFrame)
		
		
		
		#####
		
		
		self.m_bpButton3 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, self.bmp, wx.DefaultPosition, (400,640), wx.BU_AUTODRAW|wx.NO_BORDER )
		bSizer4.Add( self.m_bpButton3, 0, wx.ALL, 5 )
		self.m_bpButton3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		self.m_bpButton3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		
		
		self.m_panel1.SetSizer( bSizer4 )
		self.m_panel1.Layout()
		bSizer4.Fit( self.m_panel1 )
		bSizer3.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		###
		
		
		
		
		
		
		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.guardar )
		self.m_bpButton3.Bind( wx.EVT_BUTTON, self.guardar )
		
		self.postgres = conn.Database()

	
	# Virtual event handlers, overide them in your derived class
	def guardar( self, event ):
		self.timer.Stop()
		
		try:
			cv2.imwrite('orig_frame.jpg', self.imagen_guardar)
			time.sleep(1)
			print "Guardado"
			self.Close() 
		except AttributeError:
			traceback.print_exc()
		event.Skip()
		
	def OnPaint(self, evt):

		dc = wx.BufferedPaintDC(self)

		dc.DrawBitmap(self.bmp, 0, 0)
		print "Imprimiendo"



	def NextFrame(self, event):

		ret, self.imagen_guardar = self.capture.read()

		if ret:

			frame = cv2.cvtColor(self.imagen_guardar, cv2.COLOR_BGR2RGB)
			height, width = frame.shape[:2]
			print height,width
			self.bmp.CopyFromBuffer(frame)
			
			self.Refresh()
			print "refresh"



	def __del__(self):
		pass

		


	
class MyApp(wx.App):
    def OnInit(self):
        frame = Menu(None)
        self.SetTopWindow(frame)
        frame.Show()
        return 1
# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()

