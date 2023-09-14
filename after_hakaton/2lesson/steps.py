from aiogram.dispatcher.filters.state import StatesGroup, State

class Flow(StatesGroup):
      Card = State()
      pasword = State()
      operation = State()
      perevirka = State()
      end = State()