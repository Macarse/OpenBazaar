import zmq
# secret = 45c18922a7c2fe9997335fd1758acf2c6ba6a30f76d085c9a9ccabd84fe5efeb
c = zmq.Context()
s = c.socket(zmq.PUSH)
s.connect("tcp://localhost:5557")
s.send("novaprospekt", flags=zmq.SNDMORE)
s.send("03f881d01573c94ce7a92132479c612448140330aadbfad447543319d95af4ccc7".decode("hex"))

