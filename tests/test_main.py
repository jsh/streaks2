# import statment to import hello() from expt/hello.py
from expt.hello import hello

# unit tests for expt::main
def test_main(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "hello, world\n"
