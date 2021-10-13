'''
Mst=>libs=>color
'''
from os import name
if name == 'nt':
    '''windows color table'''
    #global BLACK,BLUE,GREEN,CYAN,RED,PURPLE,YELLOW,WHITE,GREY
    BLACK = 0x0
    BLUE  = 0x01
    GREEN = 0x02
    CYAN  = 0x03
    RED   = 0x04
    PURPLE= 0x05
    YELLOW= 0x06
    WHITE = 0x07
    GREY  = 0x08
else:
    '''other os color table'''
    #global BLACK,BLUE,GREEN,CYAN,RED,PURPLE,YELLOW,WHITE,GREY
    BLACK = '\033[0m'
    BLUE  = '\033[34m'
    GREEN = '\033[32m'
    CYAN  = '\033[36m'
    RED   = '\033[31m'
    PURPLE= '\033[35m'
    YELLOW= '\033[33m'
    WHITE = '\033[37m'
    GREY  = '\033[38m'
wincode   = """
class ntcolor:
    '''windows cmd color'''
    try:
        STD_INPUT_HANDLE = -10
        STD_OUTPUT_HANDLE= -11
        STD_ERROR_HANDLE = -12
        import ctypes
        std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        def set_cmd_text_color(self,color, handle=std_out_handle):
            '''set color'''
            bool = self.ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
            return bool
        def resetColor(self):
            '''reset color'''
            self.set_cmd_text_color(RED|GREEN|BLUE)
        def cprint(self,msg,color=BLACK,enter=1):
            '''print color message'''
            self.set_cmd_text_color(color|color|color)
            if enter == 1:
                print msg
            else:
                print msg,
            self.resetColor()
    except:
        pass
"""
otcode    = """
class otcolor:
    '''other os terminal color'''
    def cprint(self,msg,color=BLACK,enter=1):
        '''print color message'''
        if enter == 1:
            print color+msg+BLACK
        else:
            print color+msg+BLACK,
"""
if __name__ == '__main__':
    print __doc__
else:
    if name == 'nt':
        exec(wincode)
        color = ntcolor()
    else:
        exec(otcode)
        color = otcolor()
