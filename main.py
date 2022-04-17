from fastapi import FastAPI
from Model import TradeSignal, UserInputs
from Database import Insert_Trade, get_all_trades, remove_trade, Insert_userinput, get_all_userinputs, remove_userinput, update_userInput
app = FastAPI()

@app.get('/')
def root():
    return {"message": "Hello World"}

@app.get('/v1/bot1')
async def Bot1():
    return await get_all_trades()

@app.post('/v1/bot1')
async def Post_Bot1(tradeSignal: TradeSignal):
    response = await Insert_Trade(tradeSignal.dict())
    return response

@app.delete('/v1/bot1')
async def Delete_Bot1(symbol: str):
    response = await remove_trade(symbol)
    return response



@app.get('/v1/bot1/userinput')
async def URINPT():
    return await get_all_userinputs()  

@app.post('/v1/bot1/userinput')
async def Post_URINPT(userinput: UserInputs):
    response = await Insert_userinput(userinput.dict())
    return response 

@app.delete('/v1/bot1/userinput')
async def Delete_URINPT(ticker: str):
    response = await remove_userinput(ticker)
    return response       

@app.put('/v1/bot1/userinput{ticker}', response_model=UserInputs)
async def put_userinput(ticker: str,stoploss: float , takeprofit: float, amount: float):
    response = await update_userInput(ticker, stoploss, takeprofit, amount)
    return response
