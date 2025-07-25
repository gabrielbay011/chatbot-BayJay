from sandbox.processer import Installer

installer = Installer()

def test_check_url():
    assert installer._check_url("https://github.com/baymetrics/") is True

def test_make_clone():
    assert installer.make_clone("https://github.com/baymetrics/") == "INVALID"
