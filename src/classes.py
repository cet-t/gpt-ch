from typing import Any, NoReturn


class Employee:
    def __init__(self, joined: int):
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
        sum_type: int,
        is_include_allowance: bool = True
    ):
        '''
        Args:
            @role: 役職
            @hourly_salary: 時給
            @sum_type: 0: 月給, 1: 年給
            @is_include_allowance: 役職手当の有無
        '''
        def calc(_role: int):
            if role == self.roles[_role] | _role:
                def auto_calc(days: int, is_include: bool):
                    if is_include:
                        return hourly_salary * days + hourly_salary * _role
                    else:
                        return hourly_salary * days
                if is_include_allowance:  # 役職手当込み
                    if sum_type == 0:  # 月収
                        return auto_calc(30, True)
                    elif sum_type == 1:  # 年収
                        return auto_calc(365, True)
                else:  # ウィズアウト役職手当
                    if sum_type == 0:
                        return auto_calc(30, False)
                    elif sum_type == 1:
                        return auto_calc(365, False)
        calc_salaries = []
        for i in range(3):
            calc_salaries.append(calc(i))
        return sum(calc_salaries)


if __name__ == '__main__':
    # emp-1
    tadokoro = Employee(334)
    tadokoro_calc = tadokoro.calc_fiction(0, 3500, 1, True)
    print(tadokoro_calc)
