from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import QTimer
#import the interface design generated by Qt designer
from . import Valves_Ui
import time


class Panel(QWidget):
    def __init__(self,parent=None,instr=None,lock=None,title='Instrument Panel'):
        # This class derivates from a Qt Widget so we have to call
        # the class builder ".__init__()"
        QWidget.__init__(self)
        # "self" is now a Qt Widget, then we load the user interface
        # generated with QtDesigner and call it self.ui
        self.ui = Valves_Ui.Ui_Panel()
        # Now we have to feed the GUI building method of this object (self.ui)
        # with the current Qt Widget 'self', but the widgets from the design will actually be built as children
        # of the object self.ui
        self.ui.setupUi(self)
        self.setWindowTitle(title)
        self.reserved_access_to_instr=lock
        self.instr=instr
        self.monitor_timer = QTimer()
        #The timer would not wait for the completion of the task otherwise
        self.monitor_timer.setSingleShot(True)
        self.monitor_timer.timeout.connect(self.monitor)
        self.firsttime=0
        #bug: if the box is checked in the .ui file, the system freezes
        #if self.ui.monitor.isChecked():self.monitor()

        self.vd = {
            'V1' :self.ui.V1,
            'V2' : self.ui.V2,
            'V3' : self.ui.V3,
            'V4' : self.ui.V4,
            'V5' : self.ui.V5,
            'V6' : self.ui.V6,
            'V7' : self.ui.V7,
            # 'V8' : self.ui.V8,
            "V9" : self.ui.V9,
            "V10" :self.ui.V10,
            "V11" :self.ui.V11,
            "V12" :self.ui.V12,
            "V13": self.ui.V13,
            "V14": self.ui.V14,
            "V15": self.ui.V15,
            "V16": self.ui.V16,
            # "V17": self.ui.V17,
            "V18": self.ui.V18,
            "V19": self.ui.V19,
            "V20": self.ui.V20,
            "V21": self.ui.V21,
            "V22": self.ui.V22,
            "V23": self.ui.V23,
            # "V24": self.ui.V24,
            "V25": self.ui.V25,
            "V26": self.ui.V26,
            "V27": self.ui.V27,
            "V28": self.ui.V28,
            "V29": self.ui.V29,
            "V30": self.ui.V30,
            "V31": self.ui.V31,
        }




    def monitor(self,state=1):
        pass


    def check_state(self):
        id=self.sender()
        self.ui.id_name=id.objectName()
        self.valve_number_incorrected = id.objectName().strip('V')
        self.valve_number_corrected = int(self.valve_number_incorrected)+21
        self.ui.valve_instance = self.vd[id.objectName()]
        if self.ui.valve_instance.isChecked():
            self.ui.valve_instance.setStyleSheet(("background-color:green"))
            self.instr.close_valve(int(self.valve_number_corrected))
        elif self.ui.valve_instance.isChecked() is False:
            self.ui.valve_instance.setStyleSheet(("background-color:red"))
            self.instr.open_valve(int(self.valve_number_corrected))
        time.sleep(0.5)


if __name__ == "__main__":
    import sys
    import pyfirmata
    app = QApplication(sys.argv)
    window = Panel(app)
    window.show()

    sys.exit(app.exec_())

