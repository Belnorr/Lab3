import Lab22.bmi as BMI

def test_calculate_bmi_over_weight():
    expected_result = 1
    weight = 97
    test_result = BMI.calculate_bmi(1.73, weight)
    assert (test_result == expected_result)


def test_calculate_bmi_under_weight():
    expected_result = -1
    weight = 37
    test_result = BMI.calculate_bmi(1.73, weight)
    assert (test_result == expected_result)


def test_calculate_bmi_normal_weight():
    expected_result = 0
    weight = 57
    test_result = BMI.calculate_bmi(1.73, weight)
    assert (test_result == expected_result)