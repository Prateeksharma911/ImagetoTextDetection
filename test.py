from flask.typing import StatusCode

try:
    from app import app
    import unittest

except Exception as e:
    print("Some modules are missing {}".format(e))


class FlaskTest(unittest.TestCase):

    #check for response 404
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        StatusCode = response.status_code
        self.assertEqual(StatusCode,404)


if __name__ == "__main__":
    unittest.main()