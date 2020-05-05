import importlib

import mymodule

def test_myfunction(monkeypatch):
    def mock_mydeco(f):
        return f
    monkeypatch.setattr('decorators.mydeco', mock_mydeco)
    importlib.reload(mymodule)
    assert mymodule.myfunction() == "ok"