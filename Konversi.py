# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 421,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		fgSizer3 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticTextSuhu = wx.StaticText( self, wx.ID_ANY, u"Suhu        :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSuhu.Wrap( -1 )

		fgSizer3.Add( self.m_staticTextSuhu, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_textCtrlInputan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_textCtrlInputan, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_choice2Choices = [ u"C", u"R", u"F", u"K" ]
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		fgSizer3.Add( self.m_choice2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_buttonConvert = wx.Button( self, wx.ID_ANY, u"Convert", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_buttonConvert, 0, wx.ALIGN_LEFT|wx.ALL, 5 )


		bSizer2.Add( fgSizer3, 0, wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticTextC = wx.StaticText( self, wx.ID_ANY, u"Celcius", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextC.Wrap( -1 )

		fgSizer4.Add( self.m_staticTextC, 0, wx.ALL, 5 )

		self.m_textCtrlC = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrlC, 0, wx.ALL, 5 )

		self.m_staticTextR = wx.StaticText( self, wx.ID_ANY, u"Reamur", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextR.Wrap( -1 )

		fgSizer4.Add( self.m_staticTextR, 0, wx.ALL, 5 )

		self.m_textCtrlR = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrlR, 0, wx.ALL, 5 )

		self.m_staticTextF = wx.StaticText( self, wx.ID_ANY, u"Fahrenheit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextF.Wrap( -1 )

		fgSizer4.Add( self.m_staticTextF, 0, wx.ALL, 5 )

		self.m_textCtrlF = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrlF, 0, wx.ALL, 5 )

		self.m_staticTextK = wx.StaticText( self, wx.ID_ANY, u"Kelvin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextK.Wrap( -1 )

		fgSizer4.Add( self.m_staticTextK, 0, wx.ALL, 5 )

		self.m_textCtrlK = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrlK, 0, wx.ALL, 5 )


		bSizer2.Add( fgSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_choice2.Bind( wx.EVT_CHOICE, self.m_choice2OnChoice )
		self.m_buttonConvert.Bind( wx.EVT_BUTTON, self.m_buttonConvertOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_choice2OnChoice( self, event ):
		event.Skip()

	def m_buttonConvertOnButtonClick( self, event ):
		event.Skip()


