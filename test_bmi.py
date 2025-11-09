import lab2.bmi as calculate_bmi

def test_bmi_under_weight():
    bmi, classification = calculate_bmi(45, 1.75)
    assert classification == -1
    assert bmi < 18.5

def test_bmi_normal_weight():
    bmi, classification = calculate_bmi(70, 1.75)
    assert classification == 0
    assert 18.5 <= bmi <= 25.0

def test_bmi_over_weight():
    bmi, classification = calculate_bmi(90, 1.75)  # BMI ≈ 29.4
    assert classification == 1
    assert bmi > 25.0