import wx

class About(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, frame, id=-1, title='', pos=(-1, -1),size=(-1, -1))
        panel = wx.Panel(self)
        title = wx.StaticText(panel, label='关于\n编写者:@启培\n警告，请勿用于精密计算！\n感谢使用！')

def aboutshow(event):
    aboutframe = About()
    aboutframe.Show()

class JiaFa(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, frame, id=-1, title='加法', pos=(-1, -1), size=(500, 200))
        panel = wx.Panel(self)
        self.yin1 = wx.TextCtrl(panel, pos=(0, 50))
        self.yin2 = wx.TextCtrl(panel, pos=(150, 50))
        self.de = wx.TextCtrl(panel, pos=(300, 50), size=(150, 25), style=wx.TE_READONLY)
        fufont = wx.Font(15, wx.DEFAULT, wx.DEFAULT, wx.DEFAULT)
        fu = wx.StaticText(panel, label='+', pos=(125, 52))
        fu.SetFont(fufont)
        dengfu = wx.StaticText(panel, label='=', pos=(276, 52))
        dengfu.SetFont(fufont)
        jisuanb = wx.Button(panel, label='计算', pos=(200,100))
        jisuanb.Bind(wx.EVT_BUTTON, self.jisuan)

    def jisuan(self, event):
        try:
            yin1 = float(self.yin1.GetValue())
            yin2 = float(self.yin2.GetValue())
        except ValueError:
            wx.MessageBox('ValueError，请填写数字！')

        de = str(round(yin1 + yin2, 20))
        self.de.SetValue(de)

def jiafashow(event):
    jiafaframe = JiaFa()
    jiafaframe.Show()

class JianFa(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, frame, id=-1, title='减法', pos=(-1, -1), size=(500, 200))
        panel = wx.Panel(self)
        self.yin1 = wx.TextCtrl(panel, pos=(0, 50))
        self.yin2 = wx.TextCtrl(panel, pos=(150, 50))
        self.de = wx.TextCtrl(panel, pos=(300, 50), size=(150, 25), style=wx.TE_READONLY)
        fufont = wx.Font(15, wx.DEFAULT, wx.DEFAULT, wx.DEFAULT)
        fu = wx.StaticText(panel, label='-', pos=(125, 52))
        fu.SetFont(fufont)
        dengfu = wx.StaticText(panel, label='=', pos=(276, 52))
        dengfu.SetFont(fufont)
        jisuanb = wx.Button(panel, label='计算', pos=(200,100))
        jisuanb.Bind(wx.EVT_BUTTON, self.jisuan)

    def jisuan(self, event):
        try:
            yin1 = float(self.yin1.GetValue())
            yin2 = float(self.yin2.GetValue())
        except ValueError:
            wx.MessageBox('ValueError，请填写数字！')

        de = str(round(yin1 - yin2, 20))
        self.de.SetValue(de)

def jianfashow(event):
    jianfaframe = JianFa()
    jianfaframe.Show()

class ChengFa(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, frame, id=-1, title='乘法', pos=(-1, -1), size=(500, 200))
        panel = wx.Panel(self)
        self.yin1 = wx.TextCtrl(panel, pos=(0, 50))
        self.yin2 = wx.TextCtrl(panel, pos=(150, 50))
        self.de = wx.TextCtrl(panel, pos=(300, 50), size=(150, 25), style=wx.TE_READONLY)
        fufont = wx.Font(15, wx.DEFAULT, wx.DEFAULT, wx.DEFAULT)
        fu = wx.StaticText(panel, label='x', pos=(125, 52))
        fu.SetFont(fufont)
        dengfu = wx.StaticText(panel, label='=', pos=(276, 52))
        dengfu.SetFont(fufont)
        jisuanb = wx.Button(panel, label='计算', pos=(200, 100))
        jisuanb.Bind(wx.EVT_BUTTON, self.jisuan)

    def jisuan(self, event):
        try:
            yin1 = float(self.yin1.GetValue())
            yin2 = float(self.yin2.GetValue())
        except ValueError:
            wx.MessageBox('ValueError，请填写数字！')

        de = str(round(yin1 * yin2, 20))
        self.de.SetValue(de)

def chengfashow(event):
    chengfaframe = ChengFa()
    chengfaframe.Show()

class ChuFa(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, frame, id=-1, title='乘法', pos=(-1, -1), size=(500, 200))
        panel = wx.Panel(self)
        self.yin1 = wx.TextCtrl(panel, pos=(0, 50))
        self.yin2 = wx.TextCtrl(panel, pos=(150, 50))
        self.de = wx.TextCtrl(panel, pos=(300, 50), size=(150, 25), style=wx.TE_READONLY)
        fufont = wx.Font(15, wx.DEFAULT, wx.DEFAULT, wx.DEFAULT)
        fu = wx.StaticText(panel, label='÷', pos=(121, 52))
        fu.SetFont(fufont)
        dengfu = wx.StaticText(panel, label='=', pos=(276, 52))
        dengfu.SetFont(fufont)
        jisuanb = wx.Button(panel, label='计算', pos=(200, 100))
        jisuanb.Bind(wx.EVT_BUTTON, self.jisuan)

    def jisuan(self, event):
        try:
            yin1 = float(self.yin1.GetValue())
            yin2 = float(self.yin2.GetValue())
        except ValueError:
            wx.MessageBox('ValueError，请填写数字！')
        de = str(round(yin1 / yin2, 20))
        self.de.SetValue(de)

def chufashow(event):
    chufaframe = ChuFa()
    chufaframe.Show()

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=-1, title='计算器', pos=(-1, -1), size=(300, 300))
        panel = wx.Panel(self)
        title = wx.StaticText(panel, label='              计算器')
        title.SetFont(wx.Font(12, wx.DEFAULT, wx.DEFAULT, wx.DEFAULT))
        jiafabutton = wx.Button(panel, label='加法', pos=(50,50))
        jianfabutton = wx.Button(panel, label='减法', pos=(150, 50))
        chengfabutton = wx.Button(panel, label='乘法', pos=(50, 150))
        chufabutton = wx.Button(panel, label='除法', pos=(150, 150))
        aboutbutton = wx.Button(panel, label='关于', pos=(0, 17))

        aboutbutton.Bind(wx.EVT_BUTTON, aboutshow)
        jiafabutton.Bind(wx.EVT_BUTTON, jiafashow)
        jianfabutton.Bind(wx.EVT_BUTTON, jianfashow)
        chengfabutton.Bind(wx.EVT_BUTTON, chengfashow)
        chufabutton.Bind(wx.EVT_BUTTON, chufashow)

App = wx.App()
frame = MainFrame()
frame.Show()
App.MainLoop()
