# Group_13_TOR
ELEC-H417_Group13_Project
This project aims to build a TOR(The Onion Router) network. The step is following, build peer-to-peer network, build TOR network, connect tor network to the outside world. 

 

The functionality we achieved is building a peer-to-peer network. The library we used should be already installed with python. Therefore, to run the code peer_to_peer.py do not need to install the library. The way to run is is open at least three terminal on one computer, with command: 

python3 peer_to_peer.py 

Then wait for few seconds, one of them would become a server, the rest will all become clients. The clients can communicate with each other directly. 

 

We also try to do the encryption in the code encrypt_decrypt.py. The way we choose is AES (Advanced Encryption Standard). To run this code, installing a library is required. With the command: 

pip install PyCryptodome 

Then same as above, open a terminal, enter the command: 

python3 encrypt_decrypt.py 

 

According to the architecture of this project, next step should be use the encrypt and decrypt in the peer to peer to complete the tor network. 
