def solution(str_list):
    if "l" in str_list and (str_list.index("l") < str_list.index("r") if "r" in str_list else True):
        return str_list[:str_list.index("l")]
    elif "r" in str_list:
        return str_list[str_list.index("r")+1:]
    else:
        return []
