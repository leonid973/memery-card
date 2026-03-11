from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QHBoxLayout,QRadioButton,QGroupBox,QPushButton
app = QApplication([])
question = QLabel('Какой национальности не существует?')

label = QLabel()

but = QPushButton('Ответить')

group = QGroupBox('Варианты ответов')

window = QWidget()

firstlayout = QVBoxLayout()
secondlayout = QHBoxLayout()
thirdlayout = QHBoxLayout()

rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')

layoutans1 = QHBoxLayout()
layoutans2 = QVBoxLayout()
layoutans3 = QVBoxLayout()

layoutans2.addWidget(rbtn1)
layoutans2.addWidget(rbtn2)

layoutans3.addWidget(rbtn3)
layoutans3.addWidget(rbtn4)

layoutans1.addLayout(layoutans2)
layoutans1.addLayout(layoutans3,stretch = 2)

secondlayout.addWidget(question)

group.setLayout(layoutans1)
thirdlayout.addWidget(but)

firstlayout.addLayout(secondlayout)
firstlayout.addWidget(group)
firstlayout.addLayout(thirdlayout)

window.setLayout(firstlayout)

window.show()
app.exec()
