from typing import List, Optional

from terra_sdk.core import AccAddress, Coin, Coins, ValAddress
from terra_sdk.core.oracle import (
    AggregateExchangeRatePrevote,
    AggregateExchangeRateVote,
    ExchangeRatePrevote,
    ExchangeRateVote,
)
from terra_sdk.exceptions import LCDResponseError

from ._base import BaseAPI


class AsyncOracleAPI(BaseAPI):
    async def prevotes(
        self, denom: Optional[str] = None, validator: Optional[ValAddress] = None
    ) -> List[ExchangeRatePrevote]:
        if denom is not None and validator is not None:
            res = await self._c._get(f"/oracle/denoms/{denom}/prevotes/{validator}")
            return [ExchangeRatePrevote.from_data(res)]
        elif validator is not None:
            res = await self._c._get(f"/oracle/voters/{validator}/prevotes")
            return [ExchangeRatePrevote.from_data(d) for d in res]
        elif denom is not None:
            res = await self._c._get(f"/oracle/denoms/{denom}/prevotes")
            return [ExchangeRatePrevote.from_data(d) for d in res]
        else:
            raise TypeError("both denom and validator cannot both be None")

    async def votes(
        self, denom: Optional[str] = None, validator: Optional[ValAddress] = None
    ) -> List[ExchangeRateVote]:
        if denom is not None and validator is not None:
            res = await self._c._get(f"/oracle/denoms/{denom}/votes/{validator}")
            return [ExchangeRateVote.from_data(res)]
        elif validator is not None:
            res = await self._c._get(f"/oracle/voters/{validator}/votes")
            return [ExchangeRateVote.from_data(d) for d in res]
        elif denom is not None:
            res = await self._c._get(f"/oracle/denoms/{denom}/votes")
            return [ExchangeRateVote.from_data(d) for d in res]
        else:
            raise TypeError("both denom and validator cannot both be None")

    async def exchange_rates(self) -> Coins:
        res = await self._c._get("/oracle/denoms/exchange_rates")
        if res:
            return Coins.from_data(res)
        else:
            return Coins({})

    async def exchange_rate(self, denom: str) -> Coin:
        rates = await self.exchange_rates()
        return rates[denom]

    async def active_denoms(self) -> List[str]:
        return await self._c._get("/oracle/denoms/actives")

    async def feeder_address(self, validator: ValAddress) -> AccAddress:
        return await self._c._get(f"/oracle/voters/{validator}/feeder")

    async def misses(self, validator: ValAddress) -> int:
        return int(await self._c._get(f"/oracle/voters/{validator}/miss"))

    async def aggregate_prevote(
        self, validator: ValAddress
    ) -> Optional[AggregateExchangeRatePrevote]:
        try:
            res = await self._c._get(f"/oracle/voters/{validator}/aggregate_prevote")
        except LCDResponseError as e:
            if e.response.status == 404:
                return None
            else:
                raise e
        return AggregateExchangeRatePrevote.from_data(res)

    async def aggregate_vote(
        self, validator: ValAddress
    ) -> Optional[AggregateExchangeRateVote]:
        try:
            res = await self._c._get(f"/oracle/voters/{validator}/aggregate_vote")
        except LCDResponseError as e:
            if e.response.status == 404:
                return None
            else:
                raise e
        return AggregateExchangeRateVote.from_data(res)

    async def parameters(self) -> dict:
        return await self._c._get("/oracle/parameters")


class OracleAPI(BaseAPI):
    def prevotes(
        self, denom: Optional[str] = None, validator: Optional[ValAddress] = None
    ) -> List[ExchangeRatePrevote]:
        if denom is not None and validator is not None:
            res = self._c._get(f"/oracle/denoms/{denom}/prevotes/{validator}")
            return [ExchangeRatePrevote.from_data(res)]
        elif validator is not None:
            res = self._c._get(f"/oracle/voters/{validator}/prevotes")
            return [ExchangeRatePrevote.from_data(d) for d in res]
        elif denom is not None:
            res = self._c._get(f"/oracle/denoms/{denom}/prevotes")
            return [ExchangeRatePrevote.from_data(d) for d in res]
        else:
            raise TypeError("both denom and validator cannot both be None")

    def votes(
        self, denom: Optional[str] = None, validator: Optional[ValAddress] = None
    ) -> List[ExchangeRateVote]:
        if denom is not None and validator is not None:
            res = self._c._get(f"/oracle/denoms/{denom}/votes/{validator}")
            return [ExchangeRateVote.from_data(res)]
        elif validator is not None:
            res = self._c._get(f"/oracle/voters/{validator}/votes")
            return [ExchangeRateVote.from_data(d) for d in res]
        elif denom is not None:
            res = self._c._get(f"/oracle/denoms/{denom}/votes")
            return [ExchangeRateVote.from_data(d) for d in res]
        else:
            raise TypeError("both denom and validator cannot both be None")

    def exchange_rates(self) -> Coins:
        res = self._c._get("/oracle/denoms/exchange_rates")
        if res:
            return Coins.from_data(res)
        else:
            return Coins({})

    def exchange_rate(self, denom: str) -> Coin:
        rates = self.exchange_rates()
        return rates[denom]

    def active_denoms(self) -> List[str]:
        return self._c._get("/oracle/denoms/actives")

    def feeder_address(self, validator: ValAddress) -> AccAddress:
        return self._c._get(f"/oracle/voters/{validator}/feeder")

    def misses(self, validator: ValAddress) -> int:
        return int(self._c._get(f"/oracle/voters/{validator}/miss"))

    def aggregate_prevote(
        self, validator: ValAddress
    ) -> Optional[AggregateExchangeRatePrevote]:
        try:
            res = self._c._get(f"/oracle/voters/{validator}/aggregate_prevote")
        except LCDResponseError as e:
            if e.response.status == 404:
                return None
            else:
                raise e
        return AggregateExchangeRatePrevote.from_data(res)

    def aggregate_vote(
        self, validator: ValAddress
    ) -> Optional[AggregateExchangeRateVote]:
        try:
            res = self._c._get(f"/oracle/voters/{validator}/aggregate_vote")
        except LCDResponseError as e:
            if e.response.status == 404:
                return None
            else:
                raise e
        return AggregateExchangeRateVote.from_data(res)

    def parameters(self) -> dict:
        return self._c._get("/oracle/parameters")
