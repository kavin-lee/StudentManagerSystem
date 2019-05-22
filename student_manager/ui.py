"""
    ui 界面
    表示层
"""
from bll import StudentManagerController
from model import StudentModel


class StudentManagerView:
    """
        界面视图类
    """

    def __init__(self):
        # 创建逻辑控制器对象
        self.__manager = StudentManagerController()

    def __input_int(self, msg):
        while True:
            try:
                return int(input(msg))
            except:
                print("您的输入有误!!!")

    def __input_students(self):
        # 1. 在控制台中录入学生信息,存成学生对象StudentModel.
        stu = StudentModel()
        # stu.name = input("请输入学生姓名:")
        # stu.age = int(input("请输入学生年龄:"))
        # stu.score = int(input("请输入学生成绩:"))
        stu.name = input("请输入学生姓名:")
        stu.age =self.__input_int("请输入学生年龄:")
        stu.score =self.__input_int("请输入学生成绩:")
        # 2. 调用逻辑控制器的add_student方法
        self.__manager.add_student(stu)

    def __output_student_by_score(self):
        """
            根据成绩显示学生所有信息
        :return:
        """
        list_target = self.__manager.order_by_score()
        self.__output_students(list_target)

    def __output_students(self, list_target):
        print("+------+---------------+----------+----------+")
        print("|  id  |      name     |   age    |   score  |")
        print("+------+---------------+----------+----------+")
        for item in list_target:
            id = str(item.id).center(6)
            name = item.name.center(15)
            age = str(item.age).center(10)
            score = str(item.score).center(10)
            print("|%s|%s|%s|%s|" % (id, name, age, score))

        print("+------+---------------+----------+----------+")

    def __delete_student(self):
        # id = int(input("请输入要删除的学生ID:"))
        id=self.__input_int("请输入要删除的学生ID:")
        self.__manager.remove_student(id)

    def __modify_student(self):
        stu = StudentModel()
        # stu.id = int(input("请输入要修改的学生ID:"))
        # stu.name = input("请输入学生姓名:")
        # stu.age = int(input("请输入学生年龄:"))
        # stu.score = int(input("请输入学生成绩:"))
        stu.id = self.__input_int("请输入要修改的学生ID:")
        stu.name = input("请输入学生姓名:")
        stu.age = self.__input_int("请输入学生年龄:")
        stu.score = self.__input_int("请输入学生成绩:")
        self.__manager.update_student(stu)

    def __display_menu(self):
        """
            显示菜单
        :return:
        """
        print('+-------------------------+')
        print('| 1)  添加学生信息          |')
        print('| 2)  显示学生信息          |')
        print('| 3)  删除学生信息          |')
        print('| 4)  修改学生成绩          |')
        print('| 5)  按照成绩升序排列       |')
        print('+-------------------------+')

    def __select_menu(self):
        """
        选择菜单
        :return:
        """
        number = input("请输入选项:")
        if number == "1":
            self.__input_students()
        elif number == "2":
            self.__output_students(self.__manager.stu_list)
        elif number == "3":
            self.__delete_student()
        elif number == "4":
            self.__modify_student()
        elif number == "5":
            self.__output_student_by_score()

    def main(self):
        """
            界面入口方法
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()
