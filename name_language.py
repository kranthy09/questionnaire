def group_by_language(in_put):
    result = {}
    for name, lan in in_put.items():
        if result.get(lan):
            result[lan].append(name)
        else:
            result[lan] = [name]
    return result


if __name__ == "__main__":
    in_put = {"Ramesh": "Python", "Ravi": "Django", "Ram": "Python", "Rajesh": "Java"}
    result = group_by_language(in_put)
    print(result)
    # Out_put = {"python": ["Ramesh", "Ram"], "Django": ["Ravi"], "Java": ["Rajesh"]}
