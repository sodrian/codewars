def fake_bin(x):
    print(x)
    return ''.join([str(int(d) // 5) for d in x]) 