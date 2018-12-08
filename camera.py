import wx


import time

import os,shutil
import os.path

import cv, cv2
import time
import traceback
import conectPostgres as conn

class ShowCapture ( wx.Frame ):
	
	def __init__(self, parent,  fps=7):
		###
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,640 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		capture = cv2.VideoCapture(0)
		capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, 400)
		capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 640)

		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, (500,500), wx.TAB_TRAVERSAL )
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
			time.sleep(3)
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
		


class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.Bind( wx.EVT_ACTIVATE, self.actualizarBitmap )#evento para actualizar el bitmap luego de tomar la foto

		self.SetSizeHintsSz( wx.Size( 500,500 ), wx.Size( 600,600 ) )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Tomar Foto", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		
		
		self.btn_guardar = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btn_guardar, 0, wx.ALL, 5 )
		
		
		self.nombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.nombre, 0, wx.ALL, 5 )
		
		
		#Especificando que al momento de abrir el formulario nos busque si hay una foto de un usuario
		#en el lugar donde no tiene que ser, si la hay que la borre, para asi poner
		#un png por defecto que es la silueta de un user
		self.ruta="orig_frame.jpg"
		
		if os.path.exists(self.ruta):
			os.remove(self.ruta)
			self.ruta="user.png"
			print "Habia foto, pero se a eliminado"
			
		else:
			self.ruta="user.png"
			print "NO existia imagen de usuario en el sistema"
		img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)##copiar
		
		self.imagen2 = wx.StaticBitmap( self, wx.ID_ANY,wx.BitmapFromImage(img), wx.DefaultPosition, (200,200), 0 )
		self.ancho = 200
		self.alto = 200
		self.imagen2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		bSizer1.Add( self.imagen2, 0, wx.ALL, 5 )
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.foto )
		self.btn_guardar.Bind( wx.EVT_BUTTON, self.guardarImg )
		
		self.postgres = conn.Database()
	
	def __del__( self ):
		pass
		
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
		self.imagen2.SetBitmap(wx.BitmapFromImage(img))
		self.Refresh()
		
	def nombreImg(self):
		sql="""select max(id) from usuarios """
		data_param=''
		typesql='S'
		self.datos = self.postgres.query(sql,data_param,typesql)	
		for dato in self.datos:
				id=dato[0]+1
				id=(str(id))
		name_img = "user"+id+".jpg"
		return name_img
		
	def guardarImg(self,event):
		self.user_png = self.nombreImg()
		ruta = str(os.getcwd())+"/imagenes"
		print ruta
		if os.path.exists(ruta):
			self.moverImg()
		else:
			os.mkdir("imagenes", 0o777)
			self.moverImg()
	
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
				
	def ponerFoto(self):
		self.ruta="orig_frame.jpg"
		img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)
		#Escala la imagen preservando la relacion de aspecto, es decir no deformarla visualmente
		W = img.GetWidth()
		H = img.GetHeight()
		
		if W > H:
			NewW = self.PhotoMaxSize
			NewH = self.PhotoMaxSize * H / W
		else:
			NewH = self.PhotoMaxSize
			NewW = self.PhotoMaxSize * W / H
		img = img.Scale(NewW,NewH)
		self.imagen2.SetBitmap(wx.BitmapFromImage(img))
		self.Refresh()
		print "Puse foto"
		
	# Virtual event handlers, overide them in your derived class
	def foto( self, event ):
		
		panel = ShowCapture(self)
		panel.Show()
		
	



class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame1(None)
        self.SetTopWindow(frame)
        frame.Show()
        return 1
if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()

