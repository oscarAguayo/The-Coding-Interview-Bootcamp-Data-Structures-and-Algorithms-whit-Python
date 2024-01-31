import main

def test_reverse():
    assert main.reverse("apple") == "elppa"
    assert main.reverse("hello") == "olleh"
    assert main.reverse("Greetings!") == "!sgniteerG"
