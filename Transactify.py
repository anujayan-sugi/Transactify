
# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     output = ""
# 5
#     if request.method == 'POST':
#         destination = request.form.get('destination')
#         amount = request.form.get('amount')
#         try:
#             amount = int(amount)
#             output = f"Destination: {destination}\n Amount: {amount}"
#         except ValueError:
#             output = "Invalid input: Amount must be an integer"
#     return render_template('index.html', output=output)

# if __name__ == '__main__':
#     app.run(debug=True)

'''
Short Description:
Enables simplified transactions by making it much easier for
people to view how much a specific transaction will cost them.


Technical Explanation:
I used the substrateinterface library for Polkadot to 
be able to calculate the transaction fee for a given transaction.
The website was built using flask, and I created an extremely 
minimalistic but good looking UI so that newbies to Polkadot
will not be put off by any possible perceived complexity.
'''

from flask import Flask, render_template, request
from substrateinterface import SubstrateInterface, Keypair
keypair = Keypair.create_from_uri('//Alice')
app = Flask(__name__)
substrate = SubstrateInterface(
    url="ws://127.0.0.1:9944",
    ss58_format=0,
    type_registry_preset='polkadot'
)
@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        destination = request.form.get('destination')
        amount = request.form.get('amount')
        try:
            amount = int(amount)

            call = substrate.compose_call(
                call_module='Balances',
                call_function='transfer',
                call_params={
                    'dest': destination,
                    'value': amount * 10**15
                }
            )
            payment_info = substrate.get_payment_info(call=call, keypair=keypair)

            output = f"Destination: {destination}, Amount: {amount}\n, Fee: {payment_info['partialFee']}"
        except ValueError:
            output = "Invalid input: Amount must be an integer"
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
