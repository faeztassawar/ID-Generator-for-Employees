from project import generate_id
from project import generate_initials
from project import ask_ids
from project import check_arguements
import pytest

def test_check_arguements():
    with pytest.raises(SystemExit):
        check_arguements()

def test_generate_initials():
    assert generate_initials('John Marhsal') == 'J'
    assert generate_initials('henry william') == 'h'

def test_generate_id():
    assert generate_id('J', '547') == 'J547'

def test_ask_ids():
    assert ask_ids('yes') == True
    assert ask_ids('YES') == True
    assert ask_ids('Yes') == True
    assert ask_ids('no') == False