* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane-ctor.html

# Plane Constructor
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public Plane([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) inNormal, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) inPoint); 
### Description
Creates a plane.
Resulting plane has normal `inNormal` and goes through a point `inPoint`.  
  
`inNormal` must be a normalized vector.
* * *
## Declaration
public Plane([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) inNormal, float d); 
### Description
Creates a plane.
Resulting plane has normal `inNormal` and distance `d`.  
  
The distance is measured from the Plane to the origin, along the Plane's normal.  
  
Note, this means a positive value for distance results in the Plane facing towards the origin. A negative distance value results in the Plane facing away from the origin.  
  
`inNormal` must be a normalized vector.
* * *
## Declaration
public Plane([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) a, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) b, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) c); 
### Description
Creates a plane.
The resulting plane goes through the given three points. The points go around clockwise as you look down on the top surface of the plane.
* * *
