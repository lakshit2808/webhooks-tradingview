from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class TradeSignal(BaseModel):
    symbol: Optional[str] = None
    price: Optional[float] = None
    time: Optional[datetime] = None


class UserInputs(BaseModel):
    ticker: str
    StopLoss: float
    TakeProfit: float
    AmountToBeInvested: float

# {
# "symbol": "{{ticker}}",
# "price": {{close}},
# "time": "{{time}}"
# }