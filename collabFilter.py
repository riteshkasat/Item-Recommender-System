import sys
import itertools
import math

def pearson_correlation(user1,user2):
	user1_avg_rating,user2_avg_rating = (0.0,0.0)
	for k,v in d[user1].iteritems():
		user1_avg_rating +=float(v)
	
	for k,v in d[user2].iteritems():
		user2_avg_rating +=float(v)

	user1_avg_rating/=len(d[user1])
	user2_avg_rating/=len(d[user2])

	user1_rated_movies = set(d[user1].keys())
	user2_rated_movies = set(d[user2].keys())

	corrated_movies = user1_rated_movies & user2_rated_movies

	numerator,denominator_user1,denominator_user2 = (0.0,0.0,0.0)
	for movie in corrated_movies:
		normalised_user1_rating = float(d[user1][movie]) - user1_avg_rating
		normalised_user2_rating = float(d[user2][movie]) - user2_avg_rating
		numerator += (normalised_user1_rating) * (normalised_user2_rating)
		denominator_user1+= (normalised_user1_rating)**2 
		denominator_user2+= (normalised_user2_rating)**2

	pearson_correlation = numerator/(math.sqrt(denominator_user1) * math.sqrt(denominator_user2))
	return pearson_correlation

def K_nearest_neighbors(user1,k):
	result = []
	weight = {}
	for user in listofusers:
		if user!=user1:
			weight.setdefault(user,0)
			weight[user] = pearson_correlation(user1,user);
			
	i=0
	for w in sorted(weight, key=weight.get, reverse=True):
  		if i<k:
  			result.append([w,weight[w]]	)
  			i+=1
  		else:	
  			return result

def Predict(user1, item, k_nearest_neighbors):
	# print (user1,item,k_nearest_neighbors)
	
	weight_times_rating = 0.0
	sum_of_weight = 0.0
	for x in k_nearest_neighbors:
		count = 0
		try:
			count= count+1
			weight = x[1]
			print x[0],weight
			rating = float(d[x[0]][item])
			weight_times_rating+=(weight*rating)
			sum_of_weight+=weight
		except:
			pass	
	print "\n"*2
	return weight_times_rating/sum_of_weight



if __name__== "__main__":
	(inputfile,username,movie,n) = (sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
	d={}
	if int(n)==0:
		print "0"
		sys.exit()
		
	with open(inputfile) as fp:
		for line in fp:
			a=line.split('\t')
			(userid,rating,kmovie) = (a[0],a[1],a[2].strip())
			d.setdefault(userid,{})
			d[userid].setdefault(kmovie,0.0)
			d[userid][kmovie] = rating;
	
	listofusers = set(d.keys())
	
	k = K_nearest_neighbors(username,int(n))

	print Predict(username,movie, k)