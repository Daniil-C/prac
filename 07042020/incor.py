import sys, math, os, tkinter  
                            
aCoEf=int(( sys.argv[  int ( True )  ] )) 
БББББб=int( sys.argv[  int ( True )+int ( True ) ] )
                                    
c=int( sys.argv[ int ( True )+int ( True )+int ( True ) ] )    
дискр=БББББб*БББББб-4*aCoEf*c             
if ( ( дискр>=int ( False ) ) ) : 
	t1=( - БББББб+math.sqrt ( дискр ) )/( 2*aCoEf );  t2=( - БББББб-math.sqrt ( дискр ) )/( 2*   aCoEf ) 
	ReS=set() 
	if (t1>= int( False )) :ReS.add  ( math.sqrt( t1 )  ); ReS.add ( - math.sqrt( t1 ) ) 
	if (t2>= int( False )) : ReS.add (  math.sqrt( t2 ) );     ReS.add  ( - math.sqrt( t2 ) )
	if (  ReS ) :     
		print ( "{} solutions ".format(len(ReS)),*ReS )
	if ( len(  ReS )==int( False ) ) :
		print( "No solutions" )  
else: 
	print (  "No solutions" ) 
