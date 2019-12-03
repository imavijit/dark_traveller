# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:42:37 2019

@author: avijit saha
"""

#import libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Building the Blockchain

class Blockchain:
    def __init__(self):
        self.chain=[] #initializing the list of blocks
        self.create_block(proof = 1, previous_hash = '0') #genesis block
        
    def create_block(self, proof, previous_hash):
        #proof/nonce is find during mining the block i.e from proof-of-work
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash
                 }
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
                
# Mining the Blockchain
        
 #craeting a web app
app = Flask(__name__)

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
    block = blockchain.create_block(proof, previous_hash)
    responce = {'message' : 'Congratulation, you have mined a new block',
                'index' : block['index'],
                'timestamp' : block['timestamp'],
                'proof' : block['proof'],
                'previous_hash' : block['previous_hash']}
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


	
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
            