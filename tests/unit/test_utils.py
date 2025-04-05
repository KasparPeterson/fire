from fire import utils


def test_sha256():
    result = utils.sha256("abc")
    assert result == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
