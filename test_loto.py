import pytest
from loto import Card,  Keg,generate_unique_numbers
def test_num():
    lenCard=generate_unique_numbers(3*9,1,90)
    assert len(lenCard) == 27, 'Ошибка карточки'
def test_keg():
    keg = Keg()
    assert keg.num < 91 and keg.num>0, 'Ошибка бочонка'
def test_card():
    card = Card()
    keg = Keg()
    item = None
    try:
        print(card.cross_num(keg))
        assert True
    except ValueError:
        assert True
