import wx
import Konversi

class subClass(Konversi.MyFrame2):
    def __init__(self, parent):
        Konversi.MyFrame2.__init__(self, parent)

    def m_choice2OnChoice(self, event):
        return self.m_choice2.GetSelection()

    def m_buttonConvertOnButtonClick(self, event):
        try :
            satuan = self.m_choice2OnChoice(event)
            suhu = int(self.m_textCtrlInputan.GetValue())
            if satuan == 0:
                c = suhu
                r = 4 / 5 * c
                f = 9 / 5 * c + 32
                k = c + 273
            elif satuan == 1:
                r = suhu
                c = 5 / 4 * r
                f = 9 / 4 * r + 32
                k = 5 / 4 * r + 273
            elif satuan == 2:
                f = suhu
                r = 4 / 9 * (f - 32)
                c = 5 / 9 * (f - 32)
                k = 5 / 9 * (f - 32) + 273
            elif satuan == 3:
                k = int(suhu)
                r = 4 / 5 * (k - 273)
                c = k - 273
                f = 9 / 5 * (k - 273) + 32

            self.m_textCtrlC.SetValue(str(c))
            self.m_textCtrlR.SetValue(str(r))
            self.m_textCtrlF.SetValue(str(f))
            self.m_textCtrlK.SetValue(str(k))
        except ValueError:
            wx.MessageBox("Inputan tidak sesuai", "Peringatan", wx.OK | wx.ICON_ERROR)
            if wx.OK:
                self.m_textCtrlInputan.SetValue("")



app = wx.App()
frame = subClass(parent=None)
frame.Show()
app.MainLoop()