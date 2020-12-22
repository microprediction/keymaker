from microprediction import MicroWriter
import os
import random

SECONDS = 60*15  # How long to spend making a throwaway key


if __name__=='__main__':
    # WRITE_KEY is injected into environ by GitHub action. Grab it. 
    write_key = os.environ.get('WRITE_KEY')
    if ',' in write_key:          
        write_keys = write_key.split(',')
        write_key = random.choice(write_keys)
        
    # Create a throwaway key and use it to bolster the balance, using a transfer. 
    if write_key is not None:
        mw = MicroWriter(write_key=write_key)
        balance = float(mw.get_balance())
        if balance<0:
            print('Trying to top up balance for '+mw.animal, ' which is currently '+str(balance))
            throwaway_key = mw.maybe_create_key(difficulty=11, seconds=SECONDS)
            if throwaway_key is None:
                print('Sorry, no luck this time')
            else:
                print('Hit the jackpot ... topping up balance for '+ mw.animal)
                mw.put_balance(source_write_key=throwaway_key, amount=256)
                print('New balance is '+str(mw.get_balance()))
        else:   
            print('Balance for '+mw.animal+' is '+str(balance)+' so no need to top up.')

