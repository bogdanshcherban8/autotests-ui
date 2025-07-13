import pytest

system_version = "v1.2.1"

@pytest.mark.skipif(system_version == "v1.2.1", reason="Тут версия совпдает и скип")
def test_system_version_valid():
    ...
@pytest.mark.skipif(system_version == "v1.3.0", reason="Тут не совпадает и остается")
def test_system_version_invalid():
    ...