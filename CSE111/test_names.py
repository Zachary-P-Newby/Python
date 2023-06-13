from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

#make_full_name test
def test_make_full_name():
    assert make_full_name ("Zach","Newby")== "Newby;Zach"
    assert make_full_name ("Berick","Smith")== "Smith;Berick"
    assert make_full_name ("Samia","Remanda")== "Remanda;Samia"
    assert make_full_name ("Mary-Jane", "Brown") == "Brown;Mary-Jane"
    assert make_full_name("","") == ";"
    assert make_full_name("John", "Adams-Apple") == "Adams-Apple;John"

#extract Family name text
def test_extract_family_name():
    assert extract_family_name ("Newby; Zack")== "Newby"
    assert extract_family_name ("Smith; Berick")== "Smith"
    assert extract_family_name ("Remanda; Samia")== "Remanda"
    assert extract_family_name(";") == ""
    assert extract_family_name("Carbuncle;Billy-Bob") == "Carbuncle"
    assert extract_family_name("Henderson-Floyd;Gary") == "Henderson-Floyd"

#extract given name text
def test_extract_given_name():
    assert extract_given_name ("Newby; Zack")== "Zack"
    assert extract_given_name ("Smith; Berick")== "Berick"
    assert extract_given_name ("Remanda; Samia")== "Samia"
    assert extract_given_name("; ") == ""
    assert extract_given_name("Finley; Alphonse-Patrick") == "Alphonse-Patrick"
    assert extract_given_name("Johnson-Wilson; Darryl") == "Darryl"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])