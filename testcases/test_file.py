import pytest
import requests


class TestClass01:

    @pytest.mark.parametrize("hello", [1, 2, 3, 5])
    def test_method01(self, hello):
        print(str(hello) + str(requests.get(url="https://www.baidu.com")))
        result = hello
        assert result

# if __name__ == "__main__":
#     o = Class01()
#     print(o.test_method01(",i have no"))
