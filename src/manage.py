import typing


class Manage:
    def __init__(self, joined: int):
        self.joined = joined

    role_numbers = [
        0,
        1,
        2
    ]

    role_names = [
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
        role: int,
        hourly_salary: int,
        is_include_allowance: bool = True
    ):
        '''
        Args:
            @role: 役職
            @hourly_salary: 時給
            @is_include_allowance: 役職手当の有無
        '''
        def yearly_calc(_n: str):
            '''
            Args:
                @_n: role number
            '''
            if role == self.role_numbers[_n]:

                def auto_calc(days: int, is_include: bool):
                    if is_include:
                        return (hourly_salary * 8 * days) + (hourly_salary * self.allowance[_n])
                    else:
                        return hourly_salary * 8 * days

                if is_include_allowance:
                    return auto_calc(30, True)
                else:
                    return auto_calc(365, False)
        return yearly_calc(role)


if __name__ == '__main__':
    from random import randint

    high_octane = Manage(randint(128, 512))
    octane = high_octane.calc_fiction(
        role=Manage.role_numbers[0],
        hourly_salary=randint(1200, 5000),
        is_include_allowance=True
    )
    print(f'yearly: {octane} jpy')
