from typing import Any, NoReturn


class Employee:
    def __init__(self, joined: int) -> NoReturn:
        self.joined = joined

    roles = [
        'manager',
        'leader',
        'staff'
    ]

    allowance = [
        1.3,
        1.2,
        1.1
    ]

    def calc_fiction(
        self,
        role: Any,
        hourly_salary: int,
        calc_type: int,
        is_include_allowance: bool = True
    ):
        '''
        Args:
            @role: 役職
            @hourly_salary: 時給
            @calc_type: 0: 月給, 1: 年給
            @is_include_allowance: 役職手当の有無
        '''
        def calc(_role: int):
            if role == self.roles[_role] | _role:
                if is_include_allowance:
                    if calc_type == 0:
                        return hourly_salary * 30 + hourly_salary * _role
                    elif calc_type == 1:
                        return hourly_salary * 365 + hourly_salary * _role
        # manager, leader, staff
        calc_salaries = []
        for i in range(3):
            calc_salaries.append(calc(i))
        return sum(calc_salaries)


if __name__ == '__main__':
    # emp-1
    tadokoro = Employee(334)
    tadokoro_calc = tadokoro.calc_fiction(0, 3500, 1, True)
    print(tadokoro_calc)
