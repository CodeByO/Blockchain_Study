#!/usr/bin/python
import time
import json
import hashlib
import urlparse
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transations = []

        # genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self,proof,previous_hash=None):
        # Creates a new Block and adds it to the chain
        block = {
                'index': len(self.chain) + 1,
                'timestamp': time(),
                'transaction': self.current_transations,
                'proof': proof,
                'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.current_transations = []
        self.chain.append(block)
        return block
    def new_transaction(self,sender,recipient,amount):
        # Adds a new transaction to the list of transactions
        self.current_transations.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            }
        )
        return self.last_block['index'] + 1
    @staticmethod
    def hash(block):
        # Hashes a Block
        block_string = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass

