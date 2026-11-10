from dns import resolver
from typing import Generator


def txt(domain) -> Generator[list[bytes], None, None]:
    try:
        answers: resolver.Answer = resolver.resolve(domain, "TXT")
    except (resolver.NoAnswer, resolver.NXDOMAIN):
        pass
    else:
        for answer in answers:
            for string in answer.strings:
                yield string.split(b"=", 1)


def mx(domain) -> Generator[tuple[str, str], None, None]:
    try:
        answers: resolver.Answer = resolver.resolve(domain, "MX")
    except (resolver.NoAnswer, resolver.NXDOMAIN):
        pass
    else:
        for answer in answers:
            yield answer.to_text().split(" ", 1)


def addresses(domain) -> set[str]:
    """IPv4 and IPv6 addresses of domain. Empty set if the name does not exist."""
    found: set[str] = set()
    for record in ("A", "AAAA"):
        try:
            answers: resolver.Answer = resolver.resolve(domain, record)
        except (resolver.NoAnswer, resolver.NXDOMAIN):
            continue
        for answer in answers:
            found.add(answer.address)
    return found


if __name__ == "__main__":
    import sys
    from pprint import pprint

    d: str = sys.argv[1]
    print(d)
    pprint(dict(txt(d)))
    pprint(list(mx(d)))
