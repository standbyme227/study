

def persistence(n):
    count = 0
    one = 1
    if n > 9:
        n_list = map(int, str(n))
        for n in n_list:
            count += 1
            one *= n
        if one > 9:
            return persistence(one)

        else:
            return count
    else:
        return count


c = persistence(112)

print(c)