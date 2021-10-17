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
    #Arrange
    number=8
    accepted_value=21
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
    #Arrange
    number=0
    accepted_value=2
    #Act
    result=series.lucas(number)
    #Aseert
    assert result==accepted_value

def test_sum_series():
    #Arrange
    number=5
    accepted_value=11
    #Act
    result=series.sum_series(number,2,1)
    #Aseert
    assert result==accepted_value

def test_sum_series2():
    #Arrange
    number=7
    accepted_value=13
    #Act
    result=series.sum_series(number)
    #Aseert
    assert result==accepted_value

def test_sum_series3():
    #Arrange
    number=1
    accepted_value=1
    #Act
    result=series.sum_series(number,2,1)
    #Aseert
    assert result==accepted_value