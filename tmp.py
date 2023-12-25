def show_args_kwargs(*args, **kwargs):
    print(args, kwargs)


if __name__ == '__main__':
    seq = [1, 2, 3]
    dict_ = {"test": 5, "second_kwargs": 12}
    show_args_kwargs(*seq, **dict_)
