import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(123, 5)

    with pytest.raises(TypeError):
        encrypt_message("teste", "Teste")

    assert encrypt_message("teste", 10) == "etset"

    assert encrypt_message("teste", 2) == "ets_et"

    assert encrypt_message("teste", 3) == "set_et"
