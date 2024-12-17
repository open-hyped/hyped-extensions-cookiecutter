from hyped.extensions.{{ cookiecutter.extension_slug }} import DummyProcessor
from hyped.core.testing.processor import BaseDataProcessorTest
from hyped.core.typing import Int


class TestInvert(BaseDataProcessorTest):
    """Test case for the DummyProcessor class.

    This test verifies the behavior of the DummyProcessor when it processes input
    data with a single feature, 'x'. The test checks that the output matches the
    expected values for the input data provided.

    The base class, :class:`BaseDataProcessorTest`, handles the test setup, 
    input-output validation, and execution of the processor. For more details on 
    the functionality of the base test class and how to write similar tests, 
    refer to the core testing framework and its documentation (hyped.core.testing).
    """
    processor = DummyProcessor()
    input_features = {"x": Int}
    input_data = [{"x": 5}, {"x": 10}]
    expected_output_feature = Int
    expected_output_data = [5, 10]
