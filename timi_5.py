#recurive programming extravaganza II

def length_of_string(string):
    if string == '':
        return 0
    else:
        return 1 + length_of_string(string[1:])


def linear_search(lis, index):
    if lis[0] == index:
        return True

    s = linear_search(lis[1:], index)

    if s is not False:
        return s

    return False


def count_instances(lis, index):
    if lis == []:
        return 0

    if lis[0] == index:
        return 1 + count_instances(lis[1:], index)
    else:
        return 0 + count_instances(lis[1:], index)



def duplicate(lis, index):
    if lis == []:
        return False
    
    if lis[0] == index:
        r = 1 + count_instances(lis[1:], index)
        if r > 1:
            return True
        else:
            return False
    else:
        r =  0 + count_instances(lis[1:], index)
        if r > 1:
            return True
        else:
            return False


def remove_duplicate(old_lis):
    if old_lis == []:
        return old_lis
    
    new_lis = []
    if old_lis[0] not in old_lis[1:]:
        new_lis = [old_lis[0]] + remove_duplicate(old_lis[1:])
    else:
        new_lis = remove_duplicate(old_lis[1:])
    return new_lis

