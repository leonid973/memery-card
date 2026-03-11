from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QHBoxLayout,QRadioButton,QGroupBox,QPushButton,QButtonGroup,QMessageBox
from random import shuffle
app = QApplication([])
quest = QLabel('Здесь будет вопрос')

but = QPushButton('Ответить')

group = QGroupBox('Варианты ответов')

window = QWidget()

result = QLabel()

firstlayout = QVBoxLayout()
secondlayout = QHBoxLayout()
thirdlayout = QHBoxLayout()

rbtn1 = QRadioButton('1')
rbtn2 = QRadioButton('2')
rbtn3 = QRadioButton('3')
rbtn4 = QRadioButton('4')

ansgroup = QGroupBox('Результат теста')
text1 = QLabel('прав ты или нет?')
text2 = QLabel ('ответ будет тут')
anslayout = QVBoxLayout()
anslayout.addWidget(text1,alignment = Qt.AlignLeft)
anslayout.addWidget(text2,alignment = Qt.AlignCenter)
ansgroup.setLayout(anslayout)
anslayout.addWidget(result)


window.rightans_amount = 0



layoutans1 = QHBoxLayout()
layoutans2 = QVBoxLayout()
layoutans3 = QVBoxLayout()

layoutans2.addWidget(rbtn1)
layoutans2.addWidget(rbtn2)

layoutans3.addWidget(rbtn3)
layoutans3.addWidget(rbtn4)

layoutans1.addLayout(layoutans2)
layoutans1.addLayout(layoutans3,stretch = 2)

secondlayout.addWidget(quest)

group.setLayout(layoutans1)
thirdlayout.addWidget(but)

firstlayout.addLayout(secondlayout)
firstlayout.addWidget(group)
firstlayout.addWidget(ansgroup)
ansgroup.hide()
firstlayout.addLayout(thirdlayout)

window.setLayout(firstlayout)

radiogroup = QButtonGroup()
radiogroup.addButton(rbtn1)
radiogroup.addButton(rbtn2)
radiogroup.addButton(rbtn3)
radiogroup.addButton(rbtn4)
spisok = list()
window.cur_question = -1
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
def start_test():
    if but.text() == 'Ответить':
        check_answer()
        if window.cur_question == len(spisok) - 1:
            result.setText('Молодец,ты прошёл тест и набрал ' + str(window.rightans_amount) + ' баллов')
            but.hide()
            
            
    else:
        next_question()
def show_question():
    radiogroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    radiogroup.setExclusive(True)
    ansgroup.hide()
    group.show()
    but.setText('Ответить')
def show_result():
    group.hide()
    ansgroup.show()
    but.setText('Следующий вопрос')
answers = [rbtn1,rbtn2,rbtn3,rbtn4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text2.setText(q.right_answer)
    quest.setText(q.question)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно, молодец')
        window.rightans_amount += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Ответ неверный')
def show_correct(res):
    text1.setText(res)
    show_result()
def next_question():
    window.cur_question += 1
    next = spisok[window.cur_question]
    ask(next)

    




    
    


q1 = Question('Государственный язык Бразилии','Португальский','Испанский','Итальянский','Бразильский')

q2 = Question('Какой национальности не существует?','Смурфы','Алеуты','Чулымцы','Португальцы')
q3 = Question('Какого вида спорта не существует?','Хедбол','Баскетбол','Волейбол','Футбол')
q4 = Question('Государственный язык России','Русский','Английский','Китайский','Итальянский')
q5 = Question('Какой планеты нет в солнечной системе','Небула','Юпитер','Нептун','Сатурн')


spisok.append(q1)
spisok.append(q2)
spisok.append(q3)
spisok.append(q4)
spisok.append(q5)
shuffle(spisok)
but.clicked.connect(start_test)
window.resize(500,400)
window.show()
app.exec()
