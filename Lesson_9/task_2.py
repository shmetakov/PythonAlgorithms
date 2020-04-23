# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import defaultdict, OrderedDict


class MyNode:

    def __init__(self, data, priority, left=None, right=None):
        self.data = data
        self.priority = priority
        self.left = left
        self.right = right
        self.char_code = defaultdict(str)

    def __str__(self):
        return f"'{self.data}': {self.priority}"

    def __getattr__(self, name):
        if name == 'priority':
            return self.priority

    def get_dict_bin_code(self, code=''):

        if self.data:
            self.char_code[self.data] = code
            return self.char_code

        if self.left:
            self.char_code.update(self.left.get_dict_bin_code(code + '0'))

        if self.right:
            self.char_code.update(self.right.get_dict_bin_code(code + '1'))

        return self.char_code


def Haffman(s):
    char_freq = defaultdict(int)

    for char in s:
        char_freq[char] += 1

    queue = list()

    for k, v in char_freq.items():
        queue.append(MyNode(k, v))

    print('Частота всех символов: ')
    for item in queue:
        print(item)
    print('*' * 50)

    while len(queue) != 1:
        queue = sorted(queue, key=lambda my_node: my_node.priority, reverse=True)

        el_1 = queue.pop()
        el_2 = queue.pop()

        queue.append(MyNode(None, el_1.priority + el_2.priority, el_1, el_2))

    bin_tree = queue.pop()
    char_code = bin_tree.get_dict_bin_code()

    print('Коды для символов: ')
    for k, v in char_code.items():
        print(f'{k}: {v}')
    print('*' * 50)

    spam_str = ''

    for char in s:
        spam_str = spam_str + char_code[char]

    return spam_str


print(f'Закодированная строка: {Haffman("beep boop beer!")}')
print(f'Исходная строка: "beep boop beer!"')
