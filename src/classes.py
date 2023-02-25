from typing import Any, NoReturn


class Employee:
    def __init__(self, joined: int):
        self.joined = joined

    roles = {
        'manager': 1,
        'leader': 2,
        'staff': 3
    }

    allowance = [
        1.3,
        1.2,
        1.1
    ]

    def calc_fiction(
        self,
        role: str,
        hourly_salary: int,
        is_include_allowance: bool = True
    ):
        '''
        Args:
            @role: 役職
            @hourly_salary: 時給
            @is_include_allowance: 役職手当の有無
        '''
        def calc(_n: int):
            '''
            Args:
                @_n: role number
            '''
            # manager ----------------------------------------------------
            if role == self.roles[_n]:
                def auto_calc(days: int, is_include: bool):
                    if is_include:
                        return (hourly_salary * days) + (hourly_salary * self.allowance[_n])
                    else:
                        return hourly_salary * days

                # * 役職手当込み
                if is_include_allowance:
                    return auto_calc(30, True)
                # * ウィズアウト役職手当
                else:
                    return auto_calc(365, False)

            # # leader ----------------------------------------------------
            # if role == self.roles[1]:
            #     def auto_calc(days: int, is_include: bool):
            #         if is_include:
            #             return hourly_salary * days + hourly_salary * _role
            #         else:
            #             return hourly_salary * days

            #     # * 役職手当込み
            #     if is_include_allowance:
            #         return auto_calc(30, True)
            #     # * ウィズアウト役職手当
            #     else:
            #         return auto_calc(365, False)

            # # staff ----------------------------------------------------
            # if role == self.roles[3]:
            #     def auto_calc(days: int, is_include: bool):
            #         if is_include:
            #             return hourly_salary * days + hourly_salary * _role
            #         else:
            #             return hourly_salary * days

            #     # * 役職手当込み
            #     if is_include_allowance:
            #         return auto_calc(30, True)
            #     # * ウィズアウト役職手当
            #     else:
            #         return auto_calc(365, False)
        # calc_salaries = []
        # for i in range(3):
        # calc_salaries.append(calc(i))
        # return sum(calc_salaries)
        return calc(role)


if __name__ == '__main__':
    from random import randint
    # emp-1
    randomize = Employee(randint(128, 512))
    randomize_calc = randomize.calc_fiction(
        role=Employee.roles['manager'],
        hourly_salary=randint(1200, 5000),
        is_include_allowance=True
    )
    print(randomize_calc)
