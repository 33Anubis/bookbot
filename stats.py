def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def count_words(contents):
    book = get_book_text(contents)
    return f"{len(book.split())}"


def letter_stats(contents):
    dic = {}
    for letter in contents:
        if letter.lower() not in dic:
            dic[letter.lower()] = 1
        else:
            dic[letter.lower()] += 1
    return dic


def sort_on(items):
    return items["num"]


def sort_dictionary(diccy):
    result = []
    for k, v in diccy.items():
        result.append({"char": k, "num": v})
    result.sort(reverse=True, key=sort_on)
    return result


def final_report(sorted):
    for i in sorted:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
