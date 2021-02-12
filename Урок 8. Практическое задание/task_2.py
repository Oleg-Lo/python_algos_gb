"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""


class BinaryTree:
    def __init__(self, root_obj, parent=None):
        # корень
        self.root = root_obj
        # добавим информацию о родительском узле чтобы делать валидацию в функции set_root_val
        self.parent = parent
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # будем использовать одну функцию которая сама определит влево или вправо вставлять ноду
    def insert(self, new_node):
        if new_node < self.root:
            self.__insert_left(new_node)
            print("left")
        else:
            self.__insert_right(new_node)
            print("right")

    # добавить левого потомка
    def __insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node, parent=self.root)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node, parent=self.root)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def __insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node, parent=self.root)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node, parent=self.root)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        if int(self.root) < int(self.parent):  # значит это левый узел по отношению к родителю
            if obj < self.parent:
                self.root = obj
            else:
                print("ERROR! You cannot set this value as a left node")
        else:  # значит это правый узел по отношению к родителю
            if obj > self.parent:
                self.root = obj
            else:
                print("ERROR! You cannot set this value as a right node")

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
r.insert(4)
print(r.get_left_child().get_root_val())
r.insert(12)
print(r.get_left_child().get_root_val())
r.get_left_child().set_root_val(16)
r.get_right_child().set_root_val(7)
r.get_right_child().insert(11)
print(r.get_right_child().get_left_child().get_root_val())
print(r.get_right_child().get_left_child().set_root_val(10))
# -----------------------------------------------------------------
print("--------------------------------------")
print(r.get_root_val())
print(r.get_left_child())
# r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
# r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
print(r.get_root_val())
print(r.get_right_child().get_left_child())
