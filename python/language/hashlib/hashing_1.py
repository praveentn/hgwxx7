# hashing using hashlib

# load library
import hashlib

# hashing (SHA-256) in Python
hashlib.sha256(b"hello world").hexdigest()
'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'

# hashing (SHA-512) in Python
hashlib.sha512(b"hello world").hexdigest()
# '309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f9
# 89dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f'
