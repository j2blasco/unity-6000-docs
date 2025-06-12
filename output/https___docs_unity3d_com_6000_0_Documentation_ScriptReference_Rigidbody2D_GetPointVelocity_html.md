* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetPointVelocity.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).GetPointVelocity
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
public [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) GetPointVelocity([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) point); 
### Parameters
Parameter | Description  
---|---  
point | The global space point to calculate velocity for.  
### Description
The velocity of the rigidbody at the point `Point` in global space.
GetPointVelocity will take the angularVelocity of the rigidbody into account when calculating the velocity.
* * *
