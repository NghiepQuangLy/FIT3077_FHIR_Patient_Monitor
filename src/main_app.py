import sys
from PyQt5 import QtWidgets
from View.MyLogInView import MyLogIn
from Controller.MyLogInViewController import MyLogInViewController


class Application(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(Application, self).__init__(sys_argv)
        self._views = {}

        log_in_view_controller = MyLogInViewController()
        self._views["log_in"] = MyLogIn(log_in_view_controller)

        self._views["log_in"].show()


if __name__ =='__main__':
    app = Application(sys.argv)
    sys.exit(app.exec())
