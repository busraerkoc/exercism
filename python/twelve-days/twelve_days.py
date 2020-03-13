def recite(start_verse, end_verse):
	num = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

	right = ["a Partridge in a Pear Tree.",
                 "two Turtle Doves, ",
                 "three French Hens, ",
                 "four Calling Birds, ",
                 "five Gold Rings, ",
                 "six Geese-a-Laying, ",
                 "seven Swans-a-Swimming, ",
                 "eight Maids-a-Milking, ",
                 "nine Ladies Dancing, ",
                 "ten Lords-a-Leaping, ",
                 "eleven Pipers Piping, ",
                 "twelve Drummers Drumming, "]

    poem = [] 
    lyrics = 'On the {} day of Christmas my true love gave to me: '.format(num[start_verse-1])
    poem.append(lyrics)
    
	if end_verse !=1:
		for i in range(end_verse-1,1):
			lyrics += right[i]
		lyrics += "and "+right[0]
    
	poem.append(lyrics)
	return poem

print(recite(4,6))
