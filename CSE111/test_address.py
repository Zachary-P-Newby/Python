import pytest
from address import extract_city

#Format:
#In the United States, mailing addresses are supposed to be written
#in this form: number street, city, state zipcode
#For example: 525 S Center St, Rexburg, ID 83460

def test_extract_city():
    assert extract_city(",,") == ""
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("123 Gator Drive, New Orleans, LA 70001") == "New Orleans"
    assert extract_city("134 Chessy, Paris, France 75001") == "Paris"




pytest.main(["-v", "--tb=line", "-rN", __file__])