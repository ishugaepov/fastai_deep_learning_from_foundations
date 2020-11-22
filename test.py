import fire


def test_foo(a, b, c='', d=None, e=1):
    print('a', a)
    print('b', b)
    print('c', c)
    print('d', d)
    print('e', e)


if __name__ == '__main__':
    fire.Fire(test_foo)
