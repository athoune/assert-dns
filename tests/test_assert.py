from assert_dns import addresses, mx, txt
from assert_dns.asserts import assert_spf


def test_assert():
    assert_spf("free.fr")


def test_addresses_nonexistent():
    # ".invalid" is reserved by RFC 2606: such a name can never exist.
    assert addresses("nonexistent.invalid") == set()


def test_txt_nonexistent():
    # A missing name means no answers, not an NXDOMAIN error.
    assert list(txt("nonexistent.invalid")) == []


def test_mx_nonexistent():
    assert list(mx("nonexistent.invalid")) == []


def test_txt_without_record():
    # www.example.com resolves (A records) but publishes no TXT record.
    assert list(txt("www.example.com")) == []


def test_addresses_example():
    assert len(addresses("example.com")) >= 1
