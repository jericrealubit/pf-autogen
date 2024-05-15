from promptflow.entities import CustomConnection
from promptflow.client import PFClient

# client can help manage your runs and connections.
client = PFClient()

# Initialize a custom connection object
connection = CustomConnection(
    name="my_custom_connection",
    # Secrets is a required field for custom connection
    secrets={"my_key": "38Jlls53zw400jG8OQKKYBfu5AGD3sXZNAzCaH2A9LU="},
    configs={"endpoint": "promptflow-redis.redis.cache.windows.net", "other_config": "other_value"},
)
# Create the connection, note that all secret values will be scrubbed in the returned result
result = client.connections.create_or_update(connection)
print(result)

connections = client.connections.list()
for connection in connections:
    print(connection)