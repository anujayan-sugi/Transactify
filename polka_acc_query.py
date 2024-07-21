from substrateinterface import SubstrateInterface

# substrate = SubstrateInterface(url="ws://127.0.0.1:9944")

substrate = SubstrateInterface(
    url="ws://127.0.0.1:9944",
    ss58_format=0,
    type_registry_preset='polkadot'
)

result = substrate.query('System', 'Account', ['5FumiHZXSoJApjES7qZ5pWAJpU54G1Y8p4jCwp4hbWFYjA7d'])
print(result.value['data']['free']) # 635278638077956496