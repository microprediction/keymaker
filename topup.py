from microprediction import MicroWriter
import os

SECONDS = 60*15

if __name__=='__main__':
  write_key = os.environ.get('WRITE_KEY')
  if write_key is not None:
      mw = MicroWriter(write_key=write_key)
      balance = float(mw.get_balance())
      if balance<0:
          print('Trying to top up balance for '+mw.animal, ' which is currently '+str(balance))
          throwaway_key = mw.maybe_create_key(difficulty=12, seconds=SECONDS)
          if throwaway_key is None:
              print('Sorry, no luck this time')
          else:
              print('Hit the jackpot ... topping up balance for '+ animal)
              mw.put_balance(source_write_key=throwaway_key)
              print('New balance is '+str(mw.get_balance())
          
           
