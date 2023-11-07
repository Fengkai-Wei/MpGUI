from PySide6.QtCore import QSize
from PySide6.QtGui import QAction,QIcon
from PySide6.QtWidgets import QMainWindow,QToolBar,QPushButton,QStatusBar,QLineEdit,QVBoxLayout,QHBoxLayout, QGroupBox,QFormLayout
import temp_global_var
from sub_Sim_Info import AnotherWindow
import meep as mp

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app #declare an app member
        self.setWindowTitle("Custom MainWindow")
        self.setGeometry(100,100,1000,800)

        #Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu =menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        #A bunch of other menu options just for the fun of it
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")



        #Working with toolbars
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        #Add the quit action to the toolbar
        toolbar.addAction(quit_action)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("start.png"), "Some other action", self)
        action2.setStatusTip("Status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        #action2.setCheckable(True)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here"))


        # Working with status bars
        self.setStatusBar(QStatusBar(self))

        button1 = QPushButton("BUTTON1")
        button1.clicked.connect(self.button1_clicked)


        sim_info = QGroupBox('Sim Info')
        

        self.size_x_input = QLineEdit()
        self.size_x_input.setPlaceholderText('length in um')
        self.size_y_input = QLineEdit()
        self.size_y_input.setPlaceholderText('length in um')
        self.size_z_input = QLineEdit()
        self.size_z_input.setPlaceholderText('length in um')
        button_submit_cell_size = QPushButton('Submit Cell Size')
        button_submit_cell_size.clicked.connect(self.submit_cell_size_clicked)

        v_layout = QVBoxLayout()
        
        v_layout.addWidget(button_submit_cell_size)
        v_layout.addWidget(self.size_x_input)
        v_layout.addWidget(self.size_y_input)
        v_layout.addWidget(self.size_z_input)
        v_layout.addWidget(button1)
        sim_info.setLayout(v_layout)
        
        self.setCentralWidget(sim_info)
        
    
        self.subwin = None
        
    def submit_cell_size_clicked(self):
        try:
            x = eval(self.size_x_input.text())
            y = eval(self.size_y_input.text())
            z = eval(self.size_z_input.text())
            temp_global_var.set_value('cell_size',mp.Vector3(x,y,z))
            print(f"Value submitted! The size of simulation cell is {temp_global_var.get_value('cell_size')}")
        except:
            self.statusBar().showMessage("Invalid Cell Size. Submission Ignored.",3000)
            self.size_x_input.clear()
            self.size_y_input.clear()
            self.size_z_input.clear()

    
    def button1_clicked(self,checked):
        print("Clicked on the button")
        if self.subwin is None:
            self.subwin = AnotherWindow()
        self.subwin.show()
        
    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app",3000)