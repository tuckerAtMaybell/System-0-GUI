from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import QTimer
#import the interface design generated by Qt designer
from . import Arduino_Board_ALL_Ui
import time
import csv


class Panel(QWidget):
    def __init__(self,parent=None,instr=None,lock=None,title='Instrument Panel'):
        # This class derivates from a Qt Widget so we have to call
        # the class builder ".__init__()"
        QWidget.__init__(self)
        # "self" is now a Qt Widget, then we load the user interface
        # generated with QtDesigner and call it self.ui
        self.ui = Arduino_Board_ALL_Ui.Ui_Panel()
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

        self.radio_buttons={
            '1':self.ui.radioButton_1,
            '2':self.ui.radioButton_2,
            '3':self.ui.radioButton_3,
            '4':self.ui.radioButton_4,
            '5':self.ui.radioButton_5,
            '6':self.ui.radioButton_6,
            '7':self.ui.radioButton_7,
            '8':self.ui.radioButton_8,
        }




    def monitor(self):

        state = self.ui.monitor.isChecked()
        # pin = self.instr.analog[0]
        # voltage_raw = (self.instr.io.analog[0].read()) * 5.0 / 1023.0  # converting the analog reading to an actual voltage
        # if voltage_raw <=1.:
        #     self.clear()
        #     # self.ui.lcdNumber_6.display(9999)
        #     # print('voltage raw is:'+str(voltage_raw))
        #     print("This measurement is erroneous.")
        # else:
        #     self.ui.FlowmeterStatus.setText("Measurement is Valid")
        if state != 1:
            # print("frig")
            self.monitor_timer.stop()
            #self.ui.close()
        elif state and not (self.monitor_timer.isActive()):
            self.firsttime += 1
            # print("FRIG")
            #self.ui.open()
            with self.reserved_access_to_instr:
                print("A0 reading is:"+self.instr.io.analog[0].read())
                voltage_raw = (self.instr.io.analog[
                                   0].read()) * (5.0 / 1023.0)  # converting the analog reading to an actual voltage
                print(str(voltage_raw))
                if voltage_raw <= 1.:
                    self.clear()
                    # self.ui.lcdNumber_6.display(9999)
                    # print('voltage raw is:'+str(voltage_raw))
                    print("This measurement is erroneous.")
                else:
                    self.ui.FlowmeterStatus.setText("Measurement is Valid")
                flow_rate = (voltage_raw * -0.25) + 1.
                self.ui.Flow_Meter_Display.display(float(flow_rate))
                with open('FlowRate_log.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([time.strftime("%Y%m%d_%H%M%S"), flow_rate])
            self.monitor_timer.start(self.ui.refresh_rate.value() * 1000)

    def turn_on_PWM(self):
        # sender_button=self.sender()
        # self.ID = sender_button.objectName()
        self.heater=self.sender().objectName().strip("radioButton_") #returns the number of the radio button that was flipped (1-8)
        # print(self.heater)
        self.pin_ID=int(self.heater)+1
        self.heater_id=self.radio_buttons[self.heater] #correlates the name with the radiobutton obj
        # print(self.heater_id)
        self.ui.heater_instance=self.radio_buttons[self.sender().objectName().strip("radioButton_")] #sets the particular instance of valve
        # self.ui.valve_instance = self.vd[id.objectName()]

        if self.ui.heater_instance.isChecked() is True:    #turn on if hit
            self.instr.io.digital[self.pin_ID].write(1)
            print("Heater " + self.heater+ " is powered on")

        elif self.ui.heater_instance.isChecked() is False:     #turn off if hit
            self.instr.io.digital[self.pin_ID].write(0)
            print("Heater " + self.heater+ " is powered off")

    def update_timer_timeout(self,sec):
        # The value must be converted to milliseconds
        secs=float(sec.strip('secs'))
        self.monitor_timer.setInterval( secs * 1000)

    def display(self):
        pass

    def clear(self):
        #self.ui.FlowmeterStatus.setText("Measurement is Erroneous")
        pass


    def check_state(self):
        id=self.sender()
        self.ui.id_name=id.objectName()
        self.valve_number_incorrected = id.objectName().strip('V')
        self.valve_number_corrected = int(self.valve_number_incorrected)+21
        self.ui.valve_instance = self.vd[id.objectName()]
        if self.ui.valve_instance.isChecked() is False:
            if self.valve_number_incorrected=="6":
                self.ui.valve_instance.setStyleSheet(("background-color:green"))
            else:
                self.ui.valve_instance.setStyleSheet(("background-color:red"))
            self.instr.close_valve(int(self.valve_number_corrected))
        elif self.ui.valve_instance.isChecked():
            if self.valve_number_incorrected=="6":
                self.ui.valve_instance.setStyleSheet(("background-color:red"))
            else:
                self.ui.valve_instance.setStyleSheet(("background-color:green"))
            self.instr.open_valve(int(self.valve_number_corrected))
        time.sleep(0.5)


if __name__ == "__main__":
    import sys
    import pyfirmata
    app = QApplication(sys.argv)
    window = Panel(app)
    window.show()

    sys.exit(app.exec_())

