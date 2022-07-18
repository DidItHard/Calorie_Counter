import main_window, menu_page1, menu_page2, menu_page3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, main_window.Ui_MainWindow):
    '''Гланое окно'''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('project.ui', self)

        # Заголовок
        self.setWindowTitle('Calorie Counting')

        # Подсказка
        self.prompt.hide()

        # Восклицательные знаки
        self.error_sex.hide()
        self.error_activity.hide()

        # Действие кнопки "Сосчитать"
        self.start_button.clicked.connect(self.count)

        # Подписи к строкам ввода
        self.weight.setPlaceholderText('Ваша масса (кг):')
        self.height.setPlaceholderText('Ваш рост (см):')
        self.age.setPlaceholderText('Ваш возраст (года):')

        # Кнопка диеты
        self.twoWindow = None
        self.diet_button.hide()
        self.diet_button.clicked.connect(self.show_diet)

    # Исполнение после нажатой кнопки
    def count(self):
        error = False
        add = 0
        coefficient = 1
        errors = set()

        try:
            try:
                weight = float(str(self.weight.text()))
                height = float(str(self.height.text()))
                age = float(str(self.age.text()))

                # Если пользователь ввел неположительные значения
                if weight <= 0 or height <= 0 or age <= 0:
                    errors.add(ValueError)
                    # raise ValueError

                if height > 300 or weight > 700 or age > 125:
                    errors.add(ValueError)
                    # raise ValueError
            except:
                errors.add(ValueError)

            sex_index = self.sex.currentIndex()

            if sex_index == 0:
                errors.add((IndexError, 'sex'))
                # raise IndexError
            elif sex_index == 1:
                add = 5
            elif sex_index == 2:
                add = -161
            elif sex_index == 3:
                add = 0

            act_index = self.activity.currentIndex()

            if act_index == 0:
                errors.add((IndexError, 'activity'))
                # raise IndexError
            elif act_index == 1:
                coefficient = 1.2
            elif act_index == 2:
                coefficient = 1.375
            elif act_index == 3:
                coefficient = 1.55
            elif act_index == 4:
                coefficient = 1.725
            elif act_index == 5:
                coefficient = 1.9

            result = round((10 * weight + 6.25 * height - 5 * age + add) * coefficient)
            # Если результат получился отрицательным (введенные данные некоректны)
            if result <= 0:
                raise Warning

            # Если нет ошибок
            if not errors:

                # Вывод результата и меню
                self.output_calories.setText(
                    str(result))

                self.prompt.hide()
                self.error_sex.hide()
                self.error_activity.hide()

                # Раскрываем кнопку меню
                self.diet_button.show()
            else:
                raise Exception
        except:
            # Нет результата и меню
            self.output_calories.setText('-')

            # Cкрываем кнопку диеты
            self.diet_button.hide()

        # Неверные веса, рост, возраст
        if ValueError in errors:
            self.prompt.show()
        else:
            self.prompt.hide()

        # Не введен возраст
        if (IndexError, 'sex') in errors:
            self.error_sex.show()
        else:
            self.error_sex.hide()

        # Не указана активность
        if (IndexError, 'activity') in errors:
            self.error_activity.show()
        else:
            self.error_activity.hide()

    # Показать дочернее окно с диетой
    def show_diet(self):
        calories = int(self.output_calories.text()) if int(
            self.output_calories.text()) < 3000 else 3000

        # Диапозон для нормального рациона (1500 - 2500)
        if calories >= 1800:
            self.dietWindow = DietWindow_1()
            q_labels = [self.dietWindow.mon_brf_g, self.dietWindow.mon_brf_kal,
                        self.dietWindow.mon_lch_g, self.dietWindow.mon_lch_kal,
                        self.dietWindow.mon_dnr_g, self.dietWindow.mon_dnr_kal,

                        self.dietWindow.tue_brf_g, self.dietWindow.tue_brf_kal,
                        self.dietWindow.tue_lch_g, self.dietWindow.tue_lch_kal,
                        self.dietWindow.tue_dnr_g, self.dietWindow.tue_dnr_kal,

                        self.dietWindow.wed_brf_g, self.dietWindow.wed_brf_kal,
                        self.dietWindow.wed_lch_g, self.dietWindow.wed_lch_kal,
                        self.dietWindow.wed_dnr_g, self.dietWindow.wed_dnr_kal,

                        self.dietWindow.thu_brf_g, self.dietWindow.thu_brf_kal,
                        self.dietWindow.thu_lch_g, self.dietWindow.thu_lch_kal,
                        self.dietWindow.thu_dnr_g, self.dietWindow.thu_dnr_kal,

                        self.dietWindow.fri_brf_g, self.dietWindow.fri_brf_kal,
                        self.dietWindow.fri_lch_g, self.dietWindow.fri_lch_kal,
                        self.dietWindow.fri_dnr_g, self.dietWindow.fri_dnr_kal,

                        self.dietWindow.sat_brf_g, self.dietWindow.sat_brf_kal,
                        self.dietWindow.sat_lch_g, self.dietWindow.sat_lch_kal,
                        self.dietWindow.sat_dnr_g, self.dietWindow.sat_dnr_kal,

                        self.dietWindow.sun_brf_g, self.dietWindow.sun_brf_kal,
                        self.dietWindow.sun_lch_g, self.dietWindow.sun_lch_kal,
                        self.dietWindow.sun_dnr_g, self.dietWindow.sun_dnr_kal
                        ]

            # Корекция грамовок с соответсвием с нормой каллорий
            for q_label in q_labels:
                q_label.setText(str(round(
                    calories / 2000 * int(
                        q_label.text()))))
            # # monday_breakfast
            # self.dietWindow.mon_brf_g.setText(str(round(
            #     int(self.output_calories.text()) / 2000 * int(
            #         self.dietWindow.mon_brf_g.text()))))
            # self.dietWindow.mon_brf_kal.setText(str(round(
            #     int(self.output_calories.text()) / 2000 * int(
            #         self.dietWindow.mon_brf_kal.text()))))
            # Показать дочернее окно
            self.dietWindow.show()
        # Диапозон для малого рациона (1000 - 1800)
        elif calories >= 1000 and calories < 1800:
            self.dietWindow = DietWindow_2()
            q_labels = [self.dietWindow.mon_brf_g, self.dietWindow.mon_brf_kal,
                        self.dietWindow.mon_lch_g_2, self.dietWindow.mon_lch_kal_2,
                        self.dietWindow.mon_lch_g, self.dietWindow.mon_lch_kal,
                        self.dietWindow.mon_lch_g_3, self.dietWindow.mon_lch_kal_3,
                        self.dietWindow.mon_dnr_g, self.dietWindow.mon_dnr_kal,
                        self.dietWindow.mon_dnr_g_2, self.dietWindow.mon_dnr_kal_2
                        ]

            # Корекция грамовок с соответсвием с нормой каллорий
            for q_label in q_labels:
                q_label.setText(str(round(
                    calories / 2000 * int(
                        q_label.text()))))

            self.dietWindow.show()

        # Диапозон для малого рациона (0 - 1500)
        elif int(self.output_calories.text()) < 1000:

            self.dietWindow = DietWindow_3()
            self.dietWindow.show()


class DietWindow_1(QMainWindow, menu_page1.Ui_MainWindow):
    '''Дочернее окно с меню'''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('project_menu_page1.ui', self)

        # Заголовок
        self.setWindowTitle('Menu Performance 1800 <')


class DietWindow_2(QMainWindow, menu_page2.Ui_MainWindow):
    '''Дочернее окно с меню'''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('project_menu_page2.ui', self)

        # Заголовок
        self.setWindowTitle('Menu Performance 1000 - 1800')


class DietWindow_3(QMainWindow, menu_page3.Ui_MainWindow):
    '''Дочернее окно с меню'''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('project_menu_page3.ui', self)

        # Заголовок
        self.setWindowTitle('Menu Performance > 1000')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
