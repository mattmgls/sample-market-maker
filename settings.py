# The market symbol you want the bot to trade, e.g., "PERP_BTC_USDT"
symbol = "PERP_BTC_USDT"

# The offset for order placement from the mid price in basis points (1 basis point = 0.01%)
offset_bps = 100

# The bot's refresh time in milliseconds, i.e., how often the bot should refresh the orders
refresh_time_ms = 30000

# The step size in basis points for order grid (the price difference between two consecutive orders in the grid)
step_bps = 100

# The number of bid and ask orders the bot should place on either side of the mid price
grid_size = 6

# The size of the first order in the grid
base_size = 0.01

# The increment in size for each subsequent order in the grid
size_step = 0.01

# Your API public key from Woo X
api_public_key = 'j8Y+6YCHDUwYYePMvq1eOg=='

# Your API secret key from Woo X
api_secret_key = 'ORSVONLEMB6IHCRKAG4N4HRWYXBU'

# Your application ID from Woo X
application_id = '194c85b6-8114-465c-829c-9fca81e40bf4'

# The network you want to connect to. Choose 'testnet' for testing or 'mainnet' for real trading
network = 'testnet'