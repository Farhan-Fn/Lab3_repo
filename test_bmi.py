from lab2.bmi import calculate_bmi

def test_bmi_under_weight():
    bmi, classification = calculate_bmi(1.75, 45)
    assert classification == 1
    assert bmi < 18.5

def test_bmi_normal_weight():
    bmi, classification = calculate_bmi(1.75, 60)
    assert classification == 0
    assert 18.5 <= bmi <= 25.0

def test_bmi_over_weight():
    bmi, classification = calculate_bmi(1.75, 90)  
    assert classification == -1
    assert bmi > 25.0