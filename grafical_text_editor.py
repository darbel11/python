import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTextEdit


class MainWindow(QMainWindow):

    def __init__(self, window_title):
        super().__init__()

        self.setWindowTitle(window_title)

        self.opened_file_names = []
        self.tab = QTabWidget()
        self.setCentralWidget(self.tab)

        self.create_actions()
        self.create_menu_bar()

        self.connect_actions()

    def create_actions(self):
        self.new_action = QAction("&New", self)
        self.open_action = QAction("&Open...", self)
        self.save_action = QAction("&Save", self)
        self.save_as_action = QAction("&Save as...", self)
        self.close_action = QAction("&Close", self)
        self.exit_action = QAction("&Exit", self)
        self.copy_action = QAction("&Copy", self)
        self.paste_action = QAction("&Paste", self)
        self.cut_action = QAction("&Cut", self)

    def create_menu_bar(self):
        menu_bar = QMenuBar(self)

        file_menu = QMenu('&File', self)
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.save_as_action)
        file_menu.addAction(self.close_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)
        menu_bar.addMenu(file_menu)

        self.setMenuBar(menu_bar)

    def connect_actions(self):
        self.new_action.triggered.connect(self.new_file)
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save)
        self.save_as_action.triggered.connect(self.save_as)
        self.close_action.triggered.connect(self.close_file)
        self.exit_action.triggered.connect(self.close)

    def new_file(self):
        tab_title = 'untitled'
        tab_index = self.tab.addTab(QTextEdit(), tab_title)
        self.opened_file_names.append('~UNTITLED~')
        self.tab.widget(tab_index).setPlainText('')
        self.tab.setCurrentIndex(tab_index)

    def open_file(self):
        file_name = QFileDialog.getOpenFileName()[0]

        if not file_name:
            return

        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()

        tab_title = file_name[file_name.rfind('/') + 1:]
        tab_index = self.tab.addTab(QTextEdit(), tab_title)
        self.opened_file_names.append(file_name)
        self.tab.widget(tab_index).setPlainText(text)
        self.tab.setCurrentIndex(tab_index)

    def save(self):
        tab_index = self.tab.currentIndex()
        file_name = self.opened_file_names[tab_index]

        if file_name != '~UNTITLED~':
            text = self.tab.currentWidget().toPlainText()
            with open(file_name,
                      'w', encoding='utf-8') as file:
                file.write(text)
        else:
            self.save_as()

    def save_as(self):
        file_name = QFileDialog.getSaveFileName()[0]

        if not file_name:
            return

        tab_index = self.tab.currentIndex()
        self.opened_file_names[tab_index] = file_name
        tab_title = file_name[file_name.rfind('/') + 1:]
        self.tab.setTabText(tab_index, tab_title)

        text = self.tab.currentWidget().toPlainText()
        with open(file_name,
                  'w', encoding='utf-8') as file:
            file.write(text)

    def close_file(self):
        tab_index = self.tab.currentIndex()
        self.tab.widget(tab_index)
        self.tab.removeTab(tab_index)
        del self.opened_file_names[tab_index]


def run_application():
    application = QApplication(sys.argv)
    window = MainWindow(window_title="Simple Text Editor")

    window.resize(640, 480)
    window.show()

    sys.exit(application.exec_())


if __name__ == '__main__':
    run_application()
