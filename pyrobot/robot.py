import pandas as pdb

from td.client import TDClient
from td.utils import TDUtilities
milliseconds_since_epoch = TDUtilities().milliseconds_since_epoch

from datetime import datetime
from datetime import time
from datetime import timezone

from typing import List
from typing import Dict
from typing import Union


class PyRobot():


    def __init__(self, client_id: str, redirect_uri: str, credentials_path: str = None, trading_account: str = None) -> None:
        """[summary]

        Args:
            client_id (str): [description]
            redirect_uri (str): [description]
            credentials_path (str, optional): [description]. Defaults to None.
            trading_account (str, optional): [description]. Defaults to None.
        """
        self.trading_account: str = trading_account
        self.client_id: str = client_id
        self.redirect_uri: str = redirect_uri
        self.credentials_path: str = credentials_path
        self.session: TDClient = self._create_session()
        self.trades: dict = {}
        self.historical_prices: dict = {}
        self.stock_frame = None

    def _create_session(self) -> TDClient:
        """[summary]

        Returns:
            TDClient: [description]
        """
        td_client = TDClient(
            client_id=self.client_id,
            redirect_uri=self.redirect_uri,
            credentials_path=self.credentials_path
        )

        #Login to the session
        td_client.login()

        return td_client

    @property
    def pre_market_open(self) -> bool:
        """[summary]

        Returns:
            bool: [description]
        """
        pre_market_start_time = datetime.utcnow().replace(hour=8, minute=00,second=00).timestamp()
        market_start_time = datetime.utcnow().replace(hour=13, minute=30, second=00).timestamp()
        right_now = datetime.utcnow().timestamp()

        if market_start_time >= right_now >= pre_market_start_time:
            return True
        else:
            return False

    @property
    def post_market_open(self) -> bool:
        """[summary]

        Returns:
            bool: [description]
        """
        post_market_end_time = datetime.utcnow().replace(
            hour=00,
            minute=00,
            second=00
        ).timestamp()

        market_end_time = datetime.utcnow().replace(
            hour=20,
            minute=00,
            second=00
        ).timestamp()

        right_now = datetime.utcnow().timestamp()

        if post_market_end_time >= right_now >= market_end_time:
            return True
        else:
            return False

    @property
    def regular_market_open(self) -> bool:
        """[summary]

        Returns:
            bool: [description]
        """
        market_start_time = datetime.utcnow().replace(
            hour=13,
            minute=30,
            second=00
        ).timestamp()

        market_end_time = datetime.utcnow().replace(
            hour=20,
            minute=00,
            second=00
        ).timestamp()

        right_now = datetime.utcnow().timestamp()

        if market_end_time >= right_now >= market_start_time:
            return True
        else:
            return False

    def create_portfolio(self):
        pass

    def create_trade(self):
        pass

    def create_stock_frame(self):
        pass

    def grab_current_quotes(self) -> dict:
        pass

    def grab_historical_prices(self) -> List[Dict]:
        pass