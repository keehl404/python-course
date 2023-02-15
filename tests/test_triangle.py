from src.Triangle import Triangle


class TestTriangle:
    def test_create_regular_triangle(self):
        triangle = Triangle(4, 5, 6)
        assert isinstance(triangle, Triangle)
        assert triangle.name == "Triangle"
        assert triangle.side_a == 4
        assert triangle.side_b == 5
        assert triangle.side_c == 6

    def test_create_isosceles_triangle(self):
        triangle = Triangle(2, 1, 2)
        assert isinstance(triangle, Triangle)
        assert triangle.name == "Triangle"
        assert triangle.side_a == 2
        assert triangle.side_b == 1
        assert triangle.side_c == 2

    def test_create_irregular_triangle(self):
        triangle = Triangle(4, 5, 1)
        assert triangle is None

    def test_perimeter_triangle(self):
        triangle = Triangle(4, 5, 6)
        assert triangle.perimeter == 15

    def test_area_triangle(self):
        triangle = Triangle(4, 5, 6)
        assert triangle.area == 9.921567416492215

    def test_add_area_to_triangle(self):
        triangle1 = Triangle(4, 5, 6)
        triangle2 = Triangle(8, 10, 10)
        assert triangle1.add_area(triangle2) == 46.582172976138935
