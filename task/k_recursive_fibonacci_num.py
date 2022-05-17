def get_commit_count(n):
    if n in (1, 2):
        return 1
    return get_commit_count(n - 1) + get_commit_count(n - 2)


if __name__ == '__main__':
    n = int(input()) + 1
    print(get_commit_count(n))
