from block import Block
from blockchain_functions import create_genesis_block, new_block

blockchain = [create_genesis_block()]
prev_block = blockchain[0]

for i in range(20):
    block_to_add = new_block(prev_block, "data of block " + str(i))
    prev_block = block_to_add
    blockchain.append(block_to_add)

    print("Block no.{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))