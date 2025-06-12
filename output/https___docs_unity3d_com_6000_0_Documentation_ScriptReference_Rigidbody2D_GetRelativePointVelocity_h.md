* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetRelativePointVelocity.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).GetRelativePointVelocity
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
public [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) GetRelativePointVelocity([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) relativePoint); 
### Parameters
Parameter | Description  
---|---  
relativePoint | The local space point to calculate velocity for.  
### Description
The velocity of the rigidbody at the point `Point` in local space.
GetRelativePointVelocity will take the angularVelocity of the rigidbody into account when calculating the velocity.
* * *
