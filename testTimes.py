from datetime import datetime
from datetime import time
from datetime import timezone

def test_pre_market_open():   
    pre_market_start_time = datetime.utcnow().replace(hour=8, minute=00,second=00).timestamp()
    market_start_time = datetime.utcnow().replace(hour=13, minute=30, second=00).timestamp()
    right_now = datetime.utcnow().timestamp()

    if market_start_time >= right_now >= pre_market_start_time:
        return True
    else:
        return False

def post_market_open():
    post_market_end_time = datetime.utcnow().replace(
        hour=00,
        minute=00,
        second=00
    ).timestamp()

    market_end_time = datetime.utcnow().replace(
        hour=20,
        minute=00,
        second=00
    ).timestamp()

    right_now = datetime.utcnow().timestamp()

    if post_market_end_time >= right_now >= market_end_time:
        return True
    else:
        return False

def market_open():
    market_start_time = datetime.utcnow().replace(
        hour=13,
        minute=30,
        second=00
    ).timestamp()

    market_end_time = datetime.utcnow().replace(
        hour=20,
        minute=00,
        second=00
    ).timestamp()

    right_now = datetime.utcnow().timestamp()

    if market_end_time >= right_now >= market_start_time:
        return True
    else:
        return False

def market_not_open():
    market_start_time = datetime.utcnow().replace(
        hour=13,
        minute=30,
        second=00
    ).timestamp()

    market_end_time = datetime.utcnow().replace(
        hour=20,
        minute=00,
        second=00
    ).timestamp()

    right_now = datetime.utcnow().timestamp()
    
    if right_now < market_start_time or right_now > market_end_time:
        return True
    else:
        return False

print(test_pre_market_open())
print(post_market_open())
print(market_open())
print(market_not_open())