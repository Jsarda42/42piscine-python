import time

timestamp = time.time()
seconds_str = f"{timestamp:,.4f}"
sci_str = f"{timestamp:.2e}"
date_str = time.strftime("%b %d %Y", time.localtime(timestamp))
print(f"Seconds since January 1, 1970: {seconds_str} or {sci_str} in scientific notation")
print(date_str)