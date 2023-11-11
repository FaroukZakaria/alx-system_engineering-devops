## Summary:
### Duration:
Ended after a day of debugging
### Lesson:
Never code without planning first!
### Impact:
Recursion errors
### Root cause:
Not using while loops and multiple child creations
## Timeline:
### Detection:
So, I kept debugging and trying to understand how to avoid RecursionErrors.. I kept printing between lines to see where it would stop. It stopped at random times.. turned out there were limit numbers of children created. I noticed later that it was a mistake to call a method inside a method; as this doesn't end the currently running process.
### Actions:
While loops rescued me. I should've thought of them but I did not, I wasn't planning before coding that's why. First time trying made me learn this. I'm glad.
### Resolve:
While loops.
### Root cause:
so many children. More than what my ancestors could have.
