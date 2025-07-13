import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [5, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'linux', 'windows', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'firefox', 'safari'])
def test_mult_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0


@pytest.fixture(params=['chromium', 'firefox', 'safari'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Bob', 'Charlie'])
class TestOperation:
    def test_user_with_operations(self, user: str):
        print(f'Running test on user: {user}')

    @pytest.mark.parametrize('account', ['Credit Card', 'Debit Card'])
    def test_user_without_operations(self, user: str, account: str):
        print(f'Running test without user: {user}')

users = {'+7': 'User with money on bank account', '+8':'User without money on bank account', '+9': 'User with operation on bank account'}
@pytest.mark.parametrize('phone_number', users.keys(), ids=lambda phone_number: f'{phone_number}: {users[phone_number]}')
def test_identifiers(phone_number: str):
    ...
