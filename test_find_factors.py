import find_factors

class TestClass:

    def test_one(self):
        assert find_factors.find_factors(10) == [1,2,5,10]
    
    def test_two(self):
        assert 0 in find_factors.find_factors(10)