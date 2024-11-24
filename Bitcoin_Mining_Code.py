from hashlib import sha256

max_iter=1000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mining(block_no,transaction,prev_hash,prefix_zeros):
    prefix_hash='0'*prefix_zeros
    for nonce in range(max_iter):
        text=str(block_no)+transaction+prev_hash+str(nonce)
        new_hash=SHA256(text)
        if new_hash.startswith(prefix_hash):
            print(f"Yeah we are successfully mining our bitcoin and nonce is:{nonce}")
            return new_hash

    raise BaseException("we are done and out of our computational power")

if __name__=='__main__':
    transaction='''
    rimon->hasib=20
    somel->naim=100
    '''
    difficulty=5
    import time
    present_time=time.time()
    print(f"Current time is:{present_time}")
    new_hash=mining(10,transaction,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7',difficulty)
    total_time=str(time.time()-present_time)
    print(f"Total time needed for mining is:{total_time}")

    print(new_hash)