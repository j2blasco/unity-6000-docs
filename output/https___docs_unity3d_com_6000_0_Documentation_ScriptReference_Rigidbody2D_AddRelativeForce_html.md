* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddRelativeForce.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).AddRelativeForce
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
public void AddRelativeForce([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) relativeForce, [ForceMode2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceMode2D.html) mode = ForceMode2D.Force); 
### Parameters
Parameter | Description  
---|---  
relativeForce | Components of the force in the X and Y axes.  
mode | The method used to apply the specified force.  
### Description
Adds a force to the local space [Rigidbody2D.linearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-linearVelocity.html). In other words, the force is applied in the rotated coordinate space of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).
Additional resources: [Rigidbody2D.AddForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddForce.html), [Rigidbody2D.AddForceAtPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddForceAtPosition.html) and [Rigidbody2D.AddTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.AddTorque.html).
* * *
