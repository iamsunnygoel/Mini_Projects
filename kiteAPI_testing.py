# '''Basic setup for Kite Connect API'''
# from kiteconnect import KiteConnect
# api_key = "tdw8aewixbuzwv7o"  # Replace with your API Key
# kite = KiteConnect(api_key=api_key)
# print("👉 Open this login URL in browser:\n", kite.login_url())

'''Get access token using request token'''

# from kiteconnect import KiteConnect

# api_key = "tdw8aewixbuzwv7o"
# api_secret = "l7jd2qxz32gxl50vponbfrnspcomwwna"
# request_token = "qHPzVDAFeIbL77kCLMo6m3sgixQ5rvg7"

# kite = KiteConnect(api_key=api_key)

# data = kite.generate_session(request_token, api_secret=api_secret)
# kite.set_access_token(data["access_token"])

# print("✅ Access Token:", data["access_token"])

'''Code to fetch mutual fund returns using Kite Connect API'''




#Replace these with your actual credentials

from kiteconnect import KiteConnect
api_key = "tdw8aewixbuzwv7o"
access_token = "5OvlQk4nZvR1aT4S6oUmucdLCztSHCjl"

# Initialize KiteConnect instance
kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

try:
    my_holdings = kite.holdings()
    print(f"✅ Fetched {len(my_holdings)}  holdings.")
except Exception as e:
    print("❌ Failed to fetch holdings:", e)
    my_holdings = []



# try:
#     # Fetch profile details to test connectivity
#     profile = kite.profile()
#     print("✅ Kite Connect is working!")
#     print("Logged in as:", profile["user_name"])
# except Exception as e:
#     print("❌ Something went wrong!")
#     print("Error:", str(e))
