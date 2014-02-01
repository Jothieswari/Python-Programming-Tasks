# Queue Implementation
 import deque
 queue = deque(["Eric", "John", "Michael"])
 queue.append("Terry")           
 queue.append("Graham")          
 queue.popleft()                 
'Eric'
 queue.popleft()                 
'John'
 queue                           
deque(['Michael', 'Terry', 'Graham'])

#deque coding

d = deque('ghi')                 
 for elem in d:                   
     print(elem.upper())
G
H
I

d.append('j')                    
 d.appendleft('f')             
 d                               
deque(['f', 'g', 'h', 'i', 'j'])

 d.pop()                         
'j'
 d.popleft()                      
'f'
 list(d)                         
['g', 'h', 'i']
 d[0]                           
'g'
 d[-1]                           
'i'

 list(reversed(d))                
['i', 'h', 'g']
 'h' in d                         
True
 d.extend('jkl')                  
 d
deque(['g', 'h', 'i', 'j', 'k', 'l'])
 d.rotate(1)                      
 d
deque(['l', 'g', 'h', 'i', 'j', 'k'])
 d.rotate(-1)                     
 d
deque(['g', 'h', 'i', 'j', 'k', 'l'])

 deque(reversed(d))               
deque(['l', 'k', 'j', 'i', 'h', 'g'])
 d.clear()                        
 d.pop()                          

             
