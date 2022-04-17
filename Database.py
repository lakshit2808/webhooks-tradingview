from Model import TradeSignal, UserInputs
import motor.motor_asyncio as MMA
import asyncio

client = MMA.AsyncIOMotorClient('mongodb+srv://venkatesh:8Sak9ymyb6PIw2F0@venkateshdb.15dgn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
client.get_io_loop = asyncio.get_event_loop

database = client.BinanceTradingView
Collection = database.WebHooks

async def get_all_trades():
    trades = []
    cursor = Collection.find({})
    async for document in cursor:
        trades.append(TradeSignal(**document))
    return trades

async def Insert_Trade(trade):
    document = trade
    await Collection.insert_one(document)
    return document    

async def remove_trade(trade):
    await Collection.delete_one({"symbol": trade})
    return True    



Collection2 = database.UserInputs
async def get_all_userinputs():
    userinputs = []
    cursor = Collection2.find({})
    async for document in cursor:
        userinputs.append(UserInputs(**document))
    return userinputs

async def Insert_userinput(userinput):
    document = userinput
    await Collection2.insert_one(document)
    return document

async def remove_userinput(ticker):
    await Collection2.delete_one({"ticker": ticker})
    return True

async def update_userInput(ticker, stoploss, takeprofit, amount):
    await Collection2.update_one({"ticker": ticker}, {"$set":{
        "StopLoss": stoploss,
        "TakeProfit": takeprofit,
        "AmountToBeInvested": amount        
    }})
    document = await Collection.find_one({"ticker": ticker})
    return document