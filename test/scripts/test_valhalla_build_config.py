from unittest import TestCase

try:
    from test.scripts import helper
except ModuleNotFoundError:
    import helper

valhalla_build_config = helper.import_path('valhalla_build_config')


class TestBuildConfig(TestCase):
    def test_parse_true(self):
        self.assertTrue(valhalla_build_config.parse_bool('t'))