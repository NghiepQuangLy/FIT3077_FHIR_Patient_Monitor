from View.PyQt5GeneratedUis.LogInView import UiLogIn
from Controller import MyLogInViewController


class MyLogIn(UiLogIn):

    def __init__(self, widget, controller: MyLogInViewController):
        super().__init__()
        self._controller = controller
        self.setupUi(widget)

        self.submitButton.clicked.connect(lambda: controller.id_submitted(self.inputIdLineEdit.text()))


