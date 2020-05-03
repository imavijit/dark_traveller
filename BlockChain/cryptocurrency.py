# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:11:51 2020

@author: avijit saha
"""

#import libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse

# Building the Blockchain

class Blockchain:
    def __init__(self):
        self.chain=[] #initializing the list of blocks
		self.transactions = []
        self.create_block(proof = 1, previous_hash = '0') #genesis block
        self.nodes = set()
		
    def create_block(self, proof, previous_hash):
        #proof/nonce is find during mining the block i.e from proof-of-work
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
				 'transactions': self.transactions
                 }
		self.transactions = [] #after adding transactions to the block the list should be empty again for adding new transactions
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':  #Target": hash should start with 4 leading zeroes
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block= chain[0] #starting from genesis block
        block_index = 1 
        while(block_index < len(chain)):
            current_block = chain[block_index]
            #for validation, previous hash section of current block should match
            #up with hash of previous block
            if(current_block['previous_hash'] != self.hash(previous_block)):
                return False
            #check if proof of each block is valid i.e checking the hash operation
            #is starting from 4 leadinng zeroes or not
            previous_proof = previous_block['proof']
            current_proof = current_block['proof']
            hash_operation = hashlib.sha256(str(current_proof**2 - previous_proof**2).encode()).hexdigest()
            if(hash_operation[:4] != '0000'):
                return False
            
            previous_block = current_block
            block_index += 1
            
        return True
	
	def add_transaction(self, sender, receiver, amount):
		 self.tranasactions.append({ 'sender':sender,
							         'receiver': receiver,
									 'amount' : amount})
		 previous_block = self.get_previous_block()
		 return previous_block['index'] + 1
	 
	def add_node(self, address):
		  parsed_url = urlparse(address)
		  self.nodes.add(parsed_url.netloc) 
                
    def replace_chain(self):
		network = self.nodes #contains all the nodes 
		longest_chain = None
		max_length = len(self.chain) #it will be updated and accordingly longest_chain will be updated
		for node in network:
			response = requests.get(f'http://{node}/get_chain')
			if(response.status_code == 200):
				length = response.json()['length']
				chain = response.json()['chain']
				if(length > max_length and self.is_chain_valid(chain)):
					max_length = length
					longest_chain = chain
		if longest_chain:
			self.chain = longest_chain
			return True
		return False
		
		
      # Mining the Blockchain
        
#creating a web app
app = Flask(__name__)

# Creating an address for the node on Port 5000
node_address = str(uuid4()).replace('-', '')

#creating a blockchain
blockchain = Blockchain()

#Mining a new Block

 #here route decorator is used for to specify the name of the request i.e "mine_block" or basically to specify url of the request 
 #and to specify also that it's a "get" request
@app.route('/mine_block', methods = ['GET'])
 
def mine_block():
    #fisrt we have to get the previous_proof for solving the proof_of_work, solving this will allow us to create a block
    previous_block = blockchain.get_previous_block() 
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof) #get the proof for new block
    
    #get the previous_hash for create_block method
    previous_hash = blockchain.hash(previous_block)
	blockchain.add_transaction(sender = node_address, receiver = 'Avijit', amount = 0.5)
    block = blockchain.create_block(proof, previous_hash)
    responce = {'message' : 'Congratulation, you have mined a new block',
                'index' : block['index'],
                'timestamp' : block['timestamp'],
                'proof' : block['proof'],
                'previous_hash' : block['previous_hash'],
				'transactions': block['transactions']}
    return jsonify(responce), 200   #200(HTTP status code) is standard responce for successful HTTP requests
 
    
#getting the full Blockchain
 
    #route decorator is used for "get_chain" request
@app.route('/get_chain' , methods = ['GET'])

def get_chain():
    responce =  {'chain' : blockchain.chain,
                 'length' : len(blockchain.chain)}
    return jsonify(responce), 200


    #add new request "is_valid" to check is Blockchain valid
@app.route('/is_valid' , methods = ['GET'])

def is_valid():
	if(blockchain.is_chain_valid(blockchain.chain) is True):
		responce = {'message' : 'Congratulation, Your Blockchain is valid.'}
	else:
		responce = {'message' : 'Ooh!! You have a problem, the Blockchain is not valid'}
	return jsonify(responce),  200 

#running the app
app.run(host = '0.0.0.0' , port = 5000)

#Decentalizing the Blockchain

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
            