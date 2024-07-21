
from substrateinterface import SubstrateInterface, Keypair


# import logging
# logging.basicConfig(level=logging.DEBUG)


# substrate = SubstrateInterface(
#     url="ws://127.0.0.1:9944"
# )

substrate = SubstrateInterface(
    url="ws://127.0.0.1:9944",
    ss58_format=0,
    type_registry_preset='polkadot'
)


keypair = Keypair.create_from_uri('//Alice')

call = substrate.compose_call(
    call_module='Balances',
    call_function='transfer',
    call_params={
        'dest': '5FHneW46xGXgs5mUiveU4sbTyGBzmstUspZC92UhjJM694ty',
        'value': 1 * 10**15
    }
)

# Get payment info
payment_info = substrate.get_payment_info(call=call, keypair=keypair)

print("Payment info: ", payment_info)
