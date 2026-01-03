from checkdmarc.spf import get_spf_record, SPFRecordNotFound


def assert_spf(domain):
    try:
        spf = get_spf_record(domain)
    except SPFRecordNotFound:
        assert False, "No SPF record found"
    else:
        assert len(spf["warnings"]) == 0, "Warnings"
