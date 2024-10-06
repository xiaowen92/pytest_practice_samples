import pytest

def div_calcs(x, y):
    
    if y ==0:
        raise ZeroDivisionError("Cannot take 0 as denorminator") 
    return x/y 



def test_div_calcs_zero_exception():
    """
    pytest.raises can assert that exceptions are raised (catching them)
    """
    with pytest.raises(ZeroDivisionError):
        div_calcs(1,0)



def test_keyerror_details():
    """
    The raised exception can be referenced, and further inspected (or asserted)
    """
    my_map = {"foo": "bar"}

    with pytest.raises(KeyError) as ke:
        baz = my_map["baz"]
        
    print  (f'here contains {str(ke.traceback)}'  )

    # Our KeyError should reference the missing key, "baz"
    assert "baz" in str(ke)


def test_approximate_matches():
    """
    pytest.approx can be used to assert "approximate" numerical equality
    (compare to "assertAlmostEqual" in unittest.TestCase)
    """
    assert 0.1 + 0.2 +0.00000000001 == pytest.approx(0.3)
