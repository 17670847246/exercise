"""
类和类之间的关系
is-a关系：继承（例子，学生和人）
has-a关系：关联（例子，汽车和引擎）
use-a关系：依赖（例子，人使用汽车）

定义表示银行卡和ATM（自动柜员机）的类，要求ATM可以实现读卡，存钱，取钱，转账的功能
"""

class AccountCard:

    def __init__(self, card_no, expiry_date, card_type='借记卡'):
        self.card_no = card_no
        self.expiry_date = expiry_date
        self.card_type = card_type

    def __repr__(self):
        return f'卡号:{self.card_no}\n' \
               f'有效期:{self.expiry_date}\n' \
               f'类型:{self.card_type}'


class ATM(AccountCard):
    pass

