def get_text():
    return "plain-text"

def get_pdf():
    return "pdf"

def get_csv():
    return "csv"

def convert_to_text(data):
    print("[Преобразование]")
    return f"{data} as text"

def saver():
    print("[Сохранено]")

def template_function(getter, converter=False, to_save=False):
    data = getter()
    print(f"Got `{data}`")

    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        print("Пропустить преобразование")

    if to_save:
        saver()

    print(f"`{data}` был обратотан")


def main():
    """
    >>> template_function(get_text, to_save=True)
    Получить `plain-text`
    Пропустить преобразование
    [Сохранено]
    `plain-text` был преобразован

    >>> template_function(get_pdf, converter=convert_to_text)
    Got `pdf`
    [CONVERT]
    `pdf as text` был преобразован

    >>> template_function(get_csv, to_save=True)
    Получить `csv`
    Пропустить преобразование
    [SAVE]
    `csv` был преобразован
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
