def test_Tuple():
    a: i32
    b: i32
    b1: i32

    a = (1, 2, 3)
    a = (-3, -2, -1)
    a = ("a", "b", "c")

    b = a[0]
    b, b1 = a[2], a[1]
