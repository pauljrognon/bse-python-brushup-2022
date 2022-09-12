#!/bin/bash

# 1. extract CrimeStory
tar xf CrimeStory.tar.gz

# navigate to mystery folder
cd CrimeStory/mystery/

# from hint 2:
grep CLUE crimescene > clues
rm clues

# from second clue
cd memberships
grep -f AAA Delta_SkyMiles > tmp1
grep -f tmp1 Terminal_City_Library > tmp2 
grep -f tmp2 Museum_of_Bash_History > ../potential_suspects
rm tmp*

# this gives 23 suspects. We know we are looking for a male
cd ../
grep -f potential_suspects people | grep "\sM\s" | cut -f1 > suspects
rm potential_suspects

# which narrows down the list to 13 guys

# from third clue, we search for Annabel in people
grep 'Annabel' people > annabels
rm annabels

# it can be Annabel Sun or Annabel Church. Search where she lives:
interview_number=$(sed -n 179p streets/Buckingham_Place) # SEE INTERVIEW 699607 

# read interview 
# cat interviews/interview-699607

# we are looking for a blue honda with plate that starts with L337 and ends with 9
grep -A 3 "License Plate L337.*9" vehicles | grep -B 1 -A 3 "Make: Honda" | grep -B 2 -A 2 "Color: Blue" | grep 'Owner' | cut -f2 -d':'| awk '{$1=$1};1' > owners_blue_honda

# compare against suspects
grep -f owners_blue_honda suspects

# Done! It's Jeremy Bowers.
rm owners_blue_honda suspects
