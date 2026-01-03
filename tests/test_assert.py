from assert_dns.asserts import assert_spf


def test_assert():
    assert_spf("bearstech.com")
