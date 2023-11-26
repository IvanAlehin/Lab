import sys

from task1 import make_annotation
from task2 import make_dataset2, make_annotation2
from task3 import make_dataset3, make_annotation3
from task5 import Iterator

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import  *


class Window(QMainWindow):

    def __init__(self) -> None:
        """
        Данная функция вызывает все необходимые методы для создания окна
        """
        super().__init__()
        self.initUI()
        self.initIterators()
        self.setGeometry(450, 200, 1000, 700)

    def initUI(self) -> None:
        """
        Инициализация главного окна и кнопок
        Данная функция создает главный виджет и размещает кнопки по макету
        """
        self.setWindowTitle('Cat&Dog')
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        cat_btn = QPushButton('Next Cat', self)
        dog_btn = QPushButton('Next Dog', self)

        self.lbl = QLabel(self)
        self.lbl.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addSpacing(1)
        hbox.addWidget(cat_btn)
        hbox.addWidget(dog_btn)

        vbox = QVBoxLayout()
        vbox.addSpacing(1)
        vbox.addWidget(self.lbl)
        vbox.addLayout(hbox)

        self.centralWidget.setLayout(vbox)

        cat_btn.clicked.connect(self.nextCat)
        dog_btn.clicked.connect(self.nextDog)


        self.show()

    def initIterators(self) -> None:
        """
        Данная функция создает два объекта-итератора для показа изображений
        """
        self.cat = Iterator('cat', 'dataset')
        self.dog = Iterator('dog', 'dataset')

    def nextCat(self) -> None:
        """
        Показ следующего экземпляра cat
        Данная функция получает следующий экземпляр(путь к нему) изображения и размещает на главном окне
        """

        lbl_size = self.lbl.size()
        next_image = next(self.cat)
        if next_image != None:
            img = QPixmap(next_image).scaled(lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:
            self.initIterators()
            self.nextCat()

    def nextDog(self) -> None:
        """
        Показ следующего экземпляра dog
        Данная функция получает следующий экземпляр(путь к нему) изображения и размещает на главном окне
        """

        lbl_size = self.lbl.size()
        next_image = next(self.dog)
        if next_image != None:
            img = QPixmap(next_image).scaled(lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:
            self.initIterators()
            self.nextDog()



def main() -> None:
    """
    Данная функция создает объект приложения
    """
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
        

if __name__ == '__main__':
    main()