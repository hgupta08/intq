import re
line = "Cats are" \
       "playlistRm39.au" \
       " smarter than dogs" \
       "playlistRm349.au"

p=re.compile('playlistR[\w]{1}[\d]+.[\w]+')
matches=p.findall(line)

print(matches)
