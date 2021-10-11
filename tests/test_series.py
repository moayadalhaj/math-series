from math_series import series

def test_fibonacci():
    #Arrange
    number=7
    accepted_value=13
    #Act
    result=series.fibonacci(number)
    #Aseert
    assert result==accepted_value

def test_fibonacci2():
    #Arrange
    number=1
    accepted_value=1
    #Act
    result=series.fibonacci(number)
    #Aseert
    assert result==accepted_value

def test_fibonacci3():
    """
    To try if the result not equal accepted value
    """
    #Arrange
    number=7
    accepted_value=12
    #Act
    result=series.fibonacci(number)
    #Aseert
    assert result==accepted_value

def test_lucas():
    #Arrange
    number=5
    accepted_value=11
    #Act
    result=series.lucas(number)
    #Aseert
    assert result==accepted_value

def test_lucas2():
    #Arrange
    number=1
    accepted_value=1
    #Act
    result=series.lucas(number)
    #Aseert
    assert result==accepted_value

def test_lucas3():
    """
    To try if the result not equal accepted value
    """
    #Arrange
    number=7
    accepted_value=12
    #Act
    result=series.lucas(number)
    #Aseert
    assert result==accepted_value