udactiy-ds-hadoop-mapReduce-intro
================================= 

##Src for Udacity course: Introduction to Hadoop and MapReduce. https://www.udacity.com/course/ud617 

*	mapper_example.py	->	Modified code from Unit 3; 
*	reducer_example.py	-> 	Code from unit 3; 
*	reducer1.py, mapper1.py ->	What is the value of total sales for the following categories: Toys, Consumer Electronics? 

*	reducer2.py, mapper2.py ->	Find the monetary value for the highest individual sale for each separate store; 

*	reducer3.py, mapper3.py -> What is the total number of sales and the total sales value from all the stores? Assume there is only one reducer. Number of Sales? Total Value of Sales? 

###------------------PART II-------------------------- 
---
##LOGFILE 
				
The logfile is in Common Log Format: 
	10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469 
	
Write a MapReduce job to solve the given problems: 

*	p2_reducer1.py, p2_mapper1.py -> How many hits were made to the page /assets/js/the-associates.js ? How many hits were made by the IP address 10.99.99.186 ? 

*	p2_reducer3.py, p2_mapper3.py -> Write out the name of the most popular file and the number of hits into HDFS. 
