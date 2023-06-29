from aiogram.dispatcher.filters.state import StatesGroup, State

class TrafficLights(StatesGroup):
    stateOn = State()
    stateRed = State()
    stateYellow = State()
    stateGreen = State()
    stateOff = State()

class Flow(StatesGroup):
    RegisterState = State()
    Name = State()
    Email = State()
    pasword = State()
    end = State()
    
