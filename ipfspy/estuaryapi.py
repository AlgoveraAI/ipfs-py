# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_estuaryapi.ipynb (unless otherwise specified).

__all__ = ['est_get_viewer', 'list_pins', 'add_pin', 'get_pin', 'replace_pin', 'remove_pin', 'create_coll',
           'add_content', 'list_colls', 'list_coll_content', 'list_content_path', 'add_content_path', 'add_key',
           'add_data', 'add_cid', 'add_car', 'make_deal', 'view_data_cid', 'list_data', 'list_deals', 'get_deal_status',
           'get_node_stats', 'get_deal_data', 'get_miner_ask', 'get_failure_logs', 'get_deal_logs',
           'get_provider_stats', 'list_providers', 'get_data']

# Cell
def est_get_viewer(
    api_key: str # Your Estuary API key
):
    "View your Estuary account details"
    headers = {
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.get('https://api.estuary.tech/viewer', headers=headers)
    return response.json()

# Cell
# list pins
def list_pins(
    api_key: str # Your Estuary API key
):
    "List all your pins"

    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.get('https://api.estuary.tech/pinning/pins', headers=headers)
    return response.json()

# Cell
# add pin
def add_pin(
    api_key: str, # Your Estuary API key
    file_name: str, # File name to pin
    cid: str # CID to attach
):
    "Add a new pin object for the current access token."

    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
    }

    json_data = {
        'name': name,
        'cid': cid,
    }

    response = requests.post('https://api.estuary.tech/pinning/pins', headers=headers, json=json_data)
    return response.json()

# Cell
# get pin by ID
def get_pin(
    api_key: str, # Your Estuary API key
    pin_id: str # Unique pin ID
):
    "Get a pinned object by ID"

    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.get(f'https://api.estuary.tech/pinning/pins/{pin_id}', headers=headers)
    return response.json()

# Cell
# replace pin by ID
def replace_pin(
    api_key: str, # Your Estuary API key
    pin_id: str # Unique pin ID
):
    "Replace a pinned object by ID"

    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.post(f'https://api.estuary.tech/pinning/pins/{pin_id}', headers=headers)
    return response.json()

# Cell
# remove pin by ID
def remove_pin(
    api_key: str, # Your Estuary API key
    pin_id: str # Unique pin ID
):
    "Remove a pinned object by ID"

    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.delete(f'https://api.estuary.tech/pinning/pins/{pin_id}', headers=headers)
    return response.json()

# Cell
# create new collection
def create_coll(
    api_key: str, # Your Estuary API key
    name: str, # Collection name
    description: str # Collection description
):
    "Create new collection"

    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
    }

    json_data = {
        'name': name,
        'description': description,
    }

    response = requests.post('https://api.estuary.tech/collections/create', headers=headers, json=json_data)
    return response.json()

# Cell
# add content
def add_content(
    api_key: str, # Your Estuary API key
    collection_id: str, # Collection ID
    data: list, # List of paths to data to be added
    cids: list # List of respective CIDs

):
    "Add data to Collection"

    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
    }

    json_data = {
        'contents': data,
        'cids': cids,
        'collection': collection_id,
    }

    response = requests.post('https://api.estuary.tech/collections/add-content', headers=headers, json=json_data)
    return response.json()

# Cell
# list collections
def list_colls(
    api_key: str # Your Estuary API key
):
    "List your collections"

    headers = {
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.get('https://api.estuary.tech/collections/list', headers=headers)
    return response.json()

# Cell
# list collection content
def list_coll_content(
    api_key: str, # Your Estuary API key
    collection_id: str # Collection ID
):
    "List contents of a collection from ID"

    headers = {
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.get(f'https://api.estuary.tech/collections/content/{collection_id}', headers=headers)
    return response.json()

# Cell
# FS list content of a path
def list_content_path(
    api_key: str, # Your Estuary API key
    collection_id: str, # Collection ID
    path: str # Path in collection to list files from
):
    "List content of a path in collection"

    headers = {
    'Authorization': f'Bearer {api_key}',
    }

    params = {
        'col': collection_id,
    }

    response = requests.get(f'https://api.estuary.tech/collections/fs/list?col=UUID&dir={path}', params=params, headers=headers)
    return response.json()

# Cell
# FS add content to path
def add_content_path(
    api_key: str, # Your Estuary API key
    collection_id: str, # Collection ID
    path: str # Path in collection to add files to
):
    "Add content to a specific file system path in an IPFS collection"

    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
    }

    params = {
        'col': collection_id,
    }

    response = requests.post(f'https://api.estuary.tech/collections/fs/add?col=UUID&content=LOCAL_ID&path={path}', params=params, headers=headers)
    return response.json()

# Cell
# add client safe upload key
def add_key(
    api_key, # Your Estuary API key
    expiry='24h' # Expiry of upload key
):
    "Add client safe upload key"

    headers = {
    'Authorization': f'Bearer {api_key}',
    'Accept': 'application/json',
    }

    params = {
        'perms': 'upload',
        'expiry': expiry,
    }

    response = requests.post('https://api.estuary.tech/user/api-keys', params=params, headers=headers)
    return response.json()

# Cell
def add_data(
    api_key: str, # Your Estuary API key
    path_to_file: str # Path to file you want to upload
):
    "Upload file to Estuary"

    headers = {
    'Authorization': f'Bearer {api_key}',
    'Accept': 'application/json',
    }

    files = {
        'data': open(path_to_file, 'rb'),
    }

    response = requests.post('https://api.estuary.tech/content/add', headers=headers, files=files)
    return response.json()

# Cell
# add CID
def add_cid(
    api_key: str, # Your Estuary API key
    file_name: str, # File name to add to CID
    cid: str # CID for file
):
    "Use an existing IPFS CID to make storage deals."

    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
    }

    json_data = {
        'name': file_name,
        'root': cid,
    }

    response = requests.post('https://api.estuary.tech/content/add-ipfs', headers=headers, json=json_data)
    return response.json()

# Cell
# add CAR
def add_car(
    api_key: str, # Your Estuary API key
    path_to_file: str # Path to file to store
):
    "Write a Content-Addressable Archive (CAR) file, and make storage deals for its contents."

    headers = {
    'Authorization': f'Bearer {api_key}',
    'Accept': 'application/json',
    }

    with open(path_to_file, 'rb') as f:
        data = f.read()

    response = requests.post('https://api.estuary.tech/content/add-car', headers=headers, data=data)
    return response.json()

# Cell
# make deal with specific provider
def make_deal(
    api_key: str, # Your Estuary API key
    content_id: str, # Content ID on Estuary
    provider_id: str, # Provider ID
):
    "Make a deal with a storage provider and a file you have already uploaded to Estuary"

    headers = {
    'Authorization': f'Bearer {api_key}',
    }

    json_data = {
        'content': content_id,
    }

    response = requests.post(f'https://api.estuary.tech/deals/make/{provider_id}', headers=headers, json=json_data)
    return response.json()

# Cell
# data by CID
def view_data_cid(
    api_key: str, # Your Estuary API key
    cid: str # CID
):
    "View CID information"

    headers = {
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.get(f'https://api.estuary.tech/content/by-cid/{cid}', headers=headers)
    return response.json()

# Cell
# list data
def list_data(
    api_key: str # Your Estuary API key
):
    headers = {
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.get('https://api.estuary.tech/content/stats', headers=headers)
    return response.json()

# Cell
# list deals
def list_deals(
    api_key: str # Your Estuary API key
):
    headers = {
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.get('https://api.estuary.tech/content/deals', headers=headers)
    return response.json()

# Cell
# get deal status by id
def get_deal_status(
    api_key: str, # Your Estuary API key
    deal_id: str # Deal ID
):
    "Get deal status by id"

    headers = {
    'Authorization': f'Bearer {api_key}',
    }

    response = requests.get(f'https://api.estuary.tech/content/status/{deal_id}', headers=headers)
    return response.json()

# Cell
# get Estuary node stats
def get_node_stats():
    "Get Estuary node stats"

    response = requests.get('https://api.estuary.tech/public/stats')
    return response.json()

# Cell
# get on chain deal data
def get_deal_data():
    "Get on-chain deal data"

    response = requests.get('https://api.estuary.tech/public/metrics/deals-on-chain')
    return response.json()

# Cell
# get miner query ask
def get_miner_ask(
    miner_id: str # Miner ID
):
    "Get the query ask and verified ask for any miner"

    response = requests.get(f'https://api.estuary.tech/public/miners/storage/query/{miner_id}')
    return response.json()

# Cell
# get failure logs by provider
def get_failure_logs(
    miner_id: str # Miner ID
):
    "Get all of the failure logs for a specific miner"

    response = requests.get(f'https://api.estuary.tech/public/miners/failures/{miner_id}')
    return response.json()

# Cell
# get deal logs by provider
def get_deal_logs(
    provider_id: str # Provider ID
):
    "Get deal logs by provider"

    response = requests.get(f'https://api.estuary.tech/public/miners/deals/{provider_id}')
    return response.json()

# Cell
# get provider stats
def get_provider_stats(
    provider_id: str # Provider ID
):
    "Get provider stats"

    response = requests.get(f'https://api.estuary.tech/public/miners/stats/{provider_id}')
    return response.json()

# Cell
# list providers
def list_providers():
    "List Estuary providers"

    response = requests.get('https://api.estuary.tech/public/miners')
    return response.json()

# Cell
def get_data(
    cid: str, # Data CID
    path_name: str # Path and filename to store the file at
):
    "Download data from Estuary CID"

    url = f'https://dweb.link/ipfs/{cid}'
    response = requests.get(url, allow_redirects=True)  # to get content
    with open(path_name, 'wb') as f:
        f.write(response.content)
    return response.json()