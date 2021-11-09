from machine import RTC,WDT
def datetime_now(year,month,day,hour,minute,second,millisecond,microsecond):
    rtc=RTC()
    rtc.datetime((year,month,day,hour,minute,second,millisecond,microsecond,))
    return rtc.datetime()


wdt = WDT(timeout=2000)  # enable it with a timeout of 2s
wdt.feed()