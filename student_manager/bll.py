"""
    bll 业务逻辑层
"""
class StudentManagerController:
    """
        用于处理数据类传递的逻辑业务
    """

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu):
        """
            添加学生
        :param stu: 需要添加的学生对象
        :return:
        """
        stu.id = self.__generate_id()
        self.__stu_list.append(stu)

    # 删除学生remove_student
    def remove_student(self, id):
        for stu in self.stu_list:
            if stu.id == id:
                self.stu_list.remove(stu)
        return self.stu_list

    # 修改信息
    def update_student(self, stu):
        for item in self.stu_list:
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score

    # 排序order_by_score
    def order_by_score(self):
        """
            根据成绩进行升序排列
        :return:
        """
        new_list = self.stu_list[:]
        for i in range(len(new_list)):
            for n in range(i + 1, len(new_list)):
                if new_list[i].score > new_list[n].score:
                    new_list[i], new_list[n] = new_list[n], new_list[i]
        return new_list

    def __generate_id(self):
        """
        # 生成编号的需求:新编号,在上次添加对象的编号上加1
        :return:
        """
        # 方法1
        # if len(self.__stu_list) > 0:
        #     id = self.__stu_list[-1].id + 1
        # else:
        #     id = 1
        # return id
        return self.__stu_list[-1].id + 1 if len(self.__stu_list) > 0 else 1


