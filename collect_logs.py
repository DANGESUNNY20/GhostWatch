import subprocess 
class logcollect :
   def collection (self , keyword , log) :
    result= subprocess.run ([ "grep" ,keyword , log],
     capture_output=True,
            text=True)
return result.stdout
 
  class ctl :
     def journel (self):
     result= subprocess.run( 'journelctl -fo |grep -iE "failed|invalid|authentication failure|sudo|error|denied|fatal"'
      shell=True ,
      capture_output=True ,
       text=True
     )
        return result.stdout

 

      
