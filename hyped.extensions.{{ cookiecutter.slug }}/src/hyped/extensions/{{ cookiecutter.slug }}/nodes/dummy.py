"""Dummy Processor Implementation"""

from hyped.core import (
    BaseDataProcessor,
    BaseDataProcessorConfig,
    RunContext,
    process_mode,
)
from hyped.typing import Int


class DummyProcessorConfig(BaseDataProcessorConfig):
    """Dummy Processor Config"""

    value: float = 0.0
    """Dummy configuration value"""


class DummyProcessor(BaseDataProcessor[DummyProcessorConfig]):
    """Dummy Processor"""

    @process_mode(batched=False, backend="python")
    def process(self, ctx: RunContext, x: Int) -> Int:
        """Process function.

        This function processes a single integer input and returns an integer
        as the result. It operates in a non-batched mode using the Python backend.

        Args:
            ctx (RunContext): The runtime context providing access to
                configuration, logging, and other runtime-specific utilities.
            x (Int): The input integer to process.

        Returns:
            Int: The processed integer.
        """
        return x
