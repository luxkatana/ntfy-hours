import requests
from datetime import datetime
from json import dumps
from typing import NamedTuple
from time import sleep as wait
class Shift(NamedTuple):
    until: tuple[int, int]
    weekday: int

shifts: tuple[Shift, ...]  = (
    Shift((18, 30), 3), # Wednesday
    Shift((19, 30), 6),  # Saturday
    Shift((19, 30), 7),  # Sunday
)
HEADERS = {
    'Content-Type': 'application/json',
}
def main():
    now = datetime.now()

    for shift in shifts:
        if (now.weekday() + 1) == shift.weekday and (now.hour, now.minute) == shift.until:
            data = {
                'topic': 'luxkatanaworking',
                'message': f'Shift klaar, begonnen vanaf 16:30 tot {now.hour}:{now.minute}',
                'actions': [
                    {
                        'action': 'view',
                        'label': 'Open',
                        'url': f'https://thetrojanhorse3.pythonanywhere.com/?begin={now.hour}:{now.minute}'
                    }
                ]
                
            }
            requests.post('https://ntfy.sh', headers=HEADERS, data=dumps(data))
            break
            

    wait(60) # each minute check

if  __name__  ==  '__main__':
    main()