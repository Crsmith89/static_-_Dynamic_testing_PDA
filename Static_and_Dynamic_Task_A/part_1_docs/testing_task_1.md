### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

  def check_for_ace(self, card):
     if card.value = 1:  # single = is assigning, change == so is comparing. 
      return True
    else                 # missing : after else  
      return False
   

  dif highest_card(self, card1 card2): # Typo dif should be def, comma also needs to be added after card1,
  if card1.value > card2.value: # the if & else should be indented within the def function line
    return card                 # should be card1, card is not defined. 
  else:
    return card2
  


def cards_total(self, cards):
  total                        
  for card in cards:
    total += card.value
    return "You have a total of" + total

# line 36 - should read total = 0, currently doesnt have variable assigned to anything
# line 39 - return is indented wrongly, needs to go back line with for loop. total needs be + str(total) this will return total count in string.  
  
```
