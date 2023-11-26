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
        self.createActions()
        self.createMenuBar()
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

        self.folderpath = ' '

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


    def createMenuBar(self) -> None:
        """
        Создание строки меню
        Данная функция создает меню и добавляет к нему действия
        """
        menuBar = self.menuBar()

        self.fileMenu = menuBar.addMenu('&File')
        self.fileMenu.addAction(self.exitAction)
        self.fileMenu.addAction(self.changeAction)

        self.annotMenu = menuBar.addMenu('&Annotation')
        self.annotMenu.addAction(self.createAnnotAction)

        self.dataMenu = menuBar.addMenu('&Dataset')
        self.dataMenu.addAction(self.createData2Action)


    def createActions(self) -> None:
        """
        Создание действий, связанных с меню
        Данная функция создает действия и связывает их с методами класса или другими функциями
        """
        self.exitAction = QAction('&Exit')
        self.exitAction.triggered.connect(qApp.quit)

        self.changeAction = QAction('&Change dataset')
        self.changeAction.triggered.connect(self.changeDataset)

        self.createAnnotAction = QAction('&Create annotation for current dataset')
        self.createAnnotAction.triggered.connect(self.createAnnotation)

        self.createData2Action = QAction('&Create dataset2')
        self.createData2Action.triggered.connect(self.createDataset2)

        self.createData3Action = QAction('&Create dataset3')
        self.createData3Action.triggered.connect(self.createDataset3)

    def createAnnotation(self) -> None:
        """
        Данная функция создает аннотацию для текущего датасета
        """
        if 'dataset2' in str(self.folderpath):
            make_annotation2()
        elif 'dataset3' in str(self.folderpath):
            make_annotation3()
        elif 'dataset' in str(self.folderpath):
            make_annotation()

    def createDataset2(self) -> None:
        """
        Создание датасета №2
        Данная функция создает новый датасет, соединяя имя класса с порядковым номером
        """
        make_dataset2()
        self.dataMenu.addAction(self.createData3Action)

    def createDataset3(self) -> None:
        """
        Создание датасета №3
        Данная функция создает новый датасет с рандомными числами
        """
        make_dataset3()

    def changeDataset(self) -> None:
        """
        Изменение датасета
        Данная функция изменяет текущий датасет
        """

        reply = QMessageBox.question(self, 'Warning', f'Are you sure you want to change current dataset?\nCurrent dataset: {str(self.folderpath)}',
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        else:
            pass

    def closeEvent(self, event: QEvent) -> None:
        """
        Функция позволяет спросить пользователя, уверен ли он в том, что хочет закрыть окно
        """
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main() -> None:
    """
    Данная функция создает объект приложения
    """
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
        

if __name__ == '__main__':
    main()