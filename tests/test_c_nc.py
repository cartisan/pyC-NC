from nose.tools import *
from pyCNC.c_nc import C_NC_TermExtractor


class TestTermExtractor:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_execution(self):
        text = "The dog chases it's tail. A big cat watches the scene."
        extractor = C_NC_TermExtractor(text)
        extractor.compute_cnc()

        assert_is_not_none(extractor.c_values)
        assert_is_not_none(extractor.nc_values)
