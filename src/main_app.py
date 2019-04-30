import sys
from PyQt5 import QtWidgets
from View.MyLogInView import MyLogIn
from Controller.MyLogInViewController import MyLogInViewController

class Application:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)

        log_in_widget = QtWidgets.QWidget()
        log_in_view_controller = MyLogInViewController()
        self.log_in = MyLogIn(log_in_widget, log_in_view_controller)
        log_in_widget.show()

        list_of_patients_widget = QtWidgets.QWidget()


        app.exec_()

def main():
    program = Application()

if __name__ =='__main__':
    main()
