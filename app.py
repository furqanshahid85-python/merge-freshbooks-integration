from datetime import datetime
from pprint import pprint

import MergeAccountingClient
from MergeAccountingClient.api import invoices_api
from MergeAccountingClient.model.invoice_request import InvoiceRequest
from MergeAccountingClient.model.invoice_endpoint_request import InvoiceEndpointRequest

configuration = MergeAccountingClient.Configuration()

# Swap YOUR_API_KEY below with your production key:
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'
configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Swap YOUR-X-ACCOUNT-TOKEN below with your account token:
x_account_token = 'YOUR-X-ACCOUNT-TOKEN'

# Create Merge API client
api_client = MergeAccountingClient.ApiClient(configuration)

# Create InvoiceApi instance
invoice_api_instance = invoices_api.InvoicesApi(api_client)

# GET request to List Invoices from FreshBooks account 
cursor = True
while cursor != None:
    api_response = invoice_api_instance.invoices_list(x_account_token)
    pprint(api_response)
    cursor = api_response.next

# Filter Invoices based on search criteria
cursor = True
while cursor != None:
    api_response = invoice_api_instance.invoices_list(
        x_account_token,
        contact_id="5fbcd5ca-0890-4bd8-9e9e-6570558d7835"
    )
    pprint(api_response)
    cursor = api_response.next

# Create New Invoice
invoice_endpoint_request = InvoiceEndpointRequest(
        model=InvoiceRequest(
            remote_id='750428',
            type='ACCOUNTS_RECEIVABLE',
            contact='5fbcd5ca-0890-4bd8-9e9e-6570558d7835',
            number="AIQ12546",
            issue_date="2023-08-09T13:45:48.165Z",
            due_date="2023-09-09T13:45:48.165Z",
            paid_on_date="2023-09-09T13:45:48.165Z",
            memo="Weekly Payment",
            currency='USD',
            total_discount=0,
            total_tax_amount=0,
            sub_total=105,
            total_amount=105,
            balance=105,
            remote_updated_at="2023-09-09T13:45:48.165Z",
            payments=[],
        ),
)
api_response = invoice_api_instance.invoices_create(x_account_token, invoice_endpoint_request, is_debug_mode = True)
pprint(api_response)