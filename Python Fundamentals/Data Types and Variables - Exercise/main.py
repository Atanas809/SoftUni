# import webbrowser as wb

# def automatic_opener():
#     chrome_path = "C://Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
#     URLS = ("softuni.bg", "judge.org")

    for url in URLS:
        print("Opening: " + url)
        wb.get(chrome_path).open(url)

automatic_opener()
