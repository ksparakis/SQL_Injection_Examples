# SQL_Injection_Examples
This comes from Lab4 of Boston Universities CS558 Network Security Course taught by. Dr. Sharon Goldberg

#### Sources:
http://www.unixwiz.net/techtips/sql-injection.html
http://www.comsecglobal.com/FrameWork/Upload/SQL\_Smuggling.pdf
http://blog.kotowicz.net/2013/01/abusing-mysql-string-arithmetic-for.html
https://docs.python.org/2/library/md5.html
https://stackoverflow.com/questions/1557571/how-to-get-time-of-a-python-program-execution
https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method

#### Question 1.0 No protection:	
http://cs558web.bu.edu/sqlinject0/
Solution:</br>
username=victim\&password=hi\%27\%20OR\%20\%271\%27\%3D\%271
<br><br>
I used the following input for password:
<br><br>
hi' OR '1'='1
<br><br>
The reason this works is because the php code that checks this most likely looks like this
<br><br>
"Select * WHERE username='+usernam+' AND password='+password+';"	
<br><br>
by closing out hi with the ' it messes the parsing to 		
<br><br>
"Select * WHERE username='username' AND password='mom' OR '1'='1';"	
<br><br>
so now if password = false becase the 1=1 it will always return true so it returns the user as long as we know the username.

#### 1.1 single quote to two single quote:
http://cs558web.bu.edu/sqlinject1/
Solution:<br>
username=victim\&password=hi\%5C\%27\%20OR\%201\%3D1\%20$--$\%20
<br><br>
Injection used:
<br><br>
"hi\textbackslash' OR 1=1 $--$ "
<br><br>
the "$--$ " makes anything afterward a comment, also note there is a space at the end of that. We do \textbackslash' since it will turn into \textbackslash' ' so sql will escape the first \textbackslash'  but leave the 2nd quote free to still do this attack.

#### 1.2 with hashing:
Solution:
http://cs558web.bu.edu/sqlinject2/
<br>
username=victim\&password=6365540
<br><br>
takes about 14 seconds to compute, with script sql_1-2.py.
<br><br>
I quickly came to the conclusion that I would need to find an md5 hash that would output an sqlinjection in its binary raw format. But to compute this it could take years given that up to this point all my sql injections where of about 14 or characters and given my machine is a laptop.
<br><br>
First Thing I did was look for the shortest possible sql injection, and luckily I was able to find this blog post
<br><br>
http://blog.kotowicz.net/2013/01/abusing-mysql-string-arithmetic-for.html
<br><br>
it outlines how '-' will evaluate to 0 which in turn give our php code will execute to be the equivalent of 1=1, and I even went ahead and tested it on the sqlinjection0 site to see that it in fact works.
<br><br>
username=victim\&password=\%27-\%27
<br><br>
so now from here all I had to do was create a quick and dirty python program that would brute force search for a string that when hashed with md5 it's hash contained '-' and that should work.
<br><br>
My script took about 14 seconds to execute and returns:
<br><br>
Sql injection = 6365540 with hash= '-'De ????Jϥ2C Time taken:13.7294299603
<br><br>
so the password 6365540 works.
<br><br>
My script works by simply incrementing a number converting that into a string and hashing it it, checking to see if the hash contains '-'. with enough increments we find a collision. The reason I increment was to avoid having to deal with dictionaries and generating random words.
