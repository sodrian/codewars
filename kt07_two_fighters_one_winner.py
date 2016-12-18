def decr_and_check(f1, f2):
    f2.health -= f1.damage_per_attack
    if f2.health <= 0:
        raise AssertionError(f1.name)


def declare_winner(f1, f2, f_a):
    lst = [f1, f2] if f1.name == f_a else [f2, f1]

    while True:
        try:
            decr_and_check(lst[0], lst[1])
            decr_and_check(lst[1], lst[0])
        except AssertionError as err:
            return str(err)