import binascii
from nacl.signing import SigningKey

sk = SigningKey.generate()
pk = sk.verify_key

print("--- SIMPAN DATA INI ---")
print(f"AGENT_ID   : miner_peanut_{binascii.hexlify(sk.encode()[:2]).decode()}") 
print(f"PUBLIC_KEY : {binascii.hexlify(pk.encode()).decode()}")
print(f"PRIVATE_KEY: {binascii.hexlify(sk.encode()).decode()}")
print("-----------------------")
