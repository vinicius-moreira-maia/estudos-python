import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    url1 = re.search(r'^<iframe width="560" height="315" src="(http|https)://(www.youtube|youtube)\.com/embed/[a-zA-Z0-9]{11}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>$', s)

    url2 = re.search(r'^<iframe src="(http|https)://(www.youtube|youtube)\.com/embed/[a-zA-Z0-9]{11}"></iframe>$', s)

    if url1 == None and url2 == None:
        return None
    elif url1 != None and url2 == None:
        url = url1
    elif url1 == None and url2 != None:
        url = url2

    url = re.search(r'(http|https)://(www.youtube|youtube)\.com/embed/[a-zA-Z0-9]{11}', s)

    # o metodo group() retorna a parte da string onde ocorreu o match
    return shorter(url.group())

def shorter(url):
    return f"https://youtu.be/{url[-11:]}"

if __name__ == "__main__":
    main()