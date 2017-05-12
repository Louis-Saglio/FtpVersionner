def del_first_letters(word, letters):
    return word[len(letters)::]


def unix_to_windows_path_style(path: str):
    copie = ''
    for lettre in path:
        copie += lettre if lettre != '/' else '\\'
    return copie
