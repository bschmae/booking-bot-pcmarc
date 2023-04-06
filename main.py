from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.login('username', 'password')
    bot.nav_to_booking_page()
    day = bot.weekday('Wednesday')
    status = bot.make_res('pickleball', day, '7:30-8am', 'Pickleball 9B')
    print(status)



