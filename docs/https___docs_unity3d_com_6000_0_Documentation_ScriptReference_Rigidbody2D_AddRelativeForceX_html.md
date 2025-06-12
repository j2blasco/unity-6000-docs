* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddRelativeForceX.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).AddRelativeForceX
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
public void AddRelativeForceX(float force, [ForceMode2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.html) mode = ForceMode2D.Force); 
### Parameters
Parameter | Description  
---|---  
force | The force to add to the X component of the Linear Velocity in the local space of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).  
mode | The method used to apply the specified force.  
### Description
Adds a force to the X component of the [Rigidbody2D.linearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-linearVelocity.html) in the local space of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) only leaving the Y component of the local space [Rigidbody2D.linearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-linearVelocity.html) untouched.
Additional resources: [Rigidbody2D.AddRelativeForceY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddRelativeForceY.html) and [Rigidbody2D.AddRelativeForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddRelativeForce.html).
* * *
