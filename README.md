from abc import ABC
from abc import abstractmethod

import pandas as pd


class BaseIndicator(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def calculate(
        self,
        data: pd.DataFrame
    ):
        pass
