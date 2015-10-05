import unittest
import os
import json


tests_root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(tests_root)
json_filename = os.path.join(project_root, "tools.json")
classification_filename = os.path.join(
    tests_root,
    "good_for_classification.dat",
)


class JsonTestCase(unittest.TestCase):

    def get_json_string(self):
        with open(json_filename) as stream:
            return stream.read()

    def load_package_list(self):
        json_string = self.get_json_string()
        return json.loads(json_string)

    def load_good_for_classifications(self):
        good_for_classifications = set()
        with open(classification_filename) as stream:
            for line in stream:
                good_for_classifications.add(line.strip())
        return good_for_classifications

    def test_valid_json(self):
        """make sure this is a valid json"""
        # http://stackoverflow.com/a/20725965/564709
        try:
            self.load_package_list()
        except Exception, e:
            self.fail('json invalid\n\n%s' % str(e))

    def test_good_for(self):
        """make sure everything has a good_for key"""
        package_list = self.load_package_list()
        for package in package_list:
            self.assertTrue(package.has_key('good_for'))

    def test_good_for_list(self):
        """make sure good_for is always a list"""
        package_list = self.load_package_list()
        for package in package_list:
            self.assertIsInstance(package['good_for'], list)

    def test_good_for_entries(self):
        """make sure the good_for conforms to our classification"""
        classifications = self.load_good_for_classifications()
        package_list = self.load_package_list()
        for package in package_list:
            for package in package_list:
                for good_for in package['good_for']:
                    self.assertIn(good_for, classifications)
