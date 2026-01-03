from dns import resolver
from typing import Generator


def txt(domain) -> Generator[tuple[str, str], None, None]:
    try:
        answers: resolver.Answer = resolver.query(domain, "TXT")
    except resolver.NoAnswer:
        pass
    else:
        for answer in answers:
            for string in answer.strings:
                yield string.split(b"=", 1)


def mx(domain) -> Generator[tuple[str, str], None, None]:
    try:
        answers: resolver.Answer = resolver.query(domain, "MX")
    except resolver.NoAnswer:
        pass
    else:
        for answer in answers:
            yield answer.to_text().split(" ", 1)


if __name__ == "__main__":
    import sys
    from pprint import pprint

    d: str = sys.argv[1]
    print(d)
    pprint(dict(txt(d)))
    pprint(list(mx(d)))
