import datetime as date
from block import Block

def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis block", "0")

def new_block(prev_block, data):
    index = prev_block.index
    timestamp = date.datetime.now()
    block_data = data
    prev_hash = prev_block.hash
    return Block(index, timestamp, block_data, prev_hash)

