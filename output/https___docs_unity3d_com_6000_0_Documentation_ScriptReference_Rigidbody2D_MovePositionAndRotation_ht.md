* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.MovePositionAndRotation.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).MovePositionAndRotation
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
public void MovePositionAndRotation([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, float angle); 
### Parameters
Parameter | Description  
---|---  
position | The position to move the rigidbody to.  
angle | The angle to move the rigidbody to.  
### Description
Moves the rigidbody position to `position` and the rigidbody angle to `angle`.
This is a combination of calling both [MovePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.MovePosition.html) and [MoveRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.MoveRotation.html). This can be used to increase performance by not having to perform two separate calls to queue movements.  
  
For more details on the operation of movement using these methods, refer to [Rigidbody2D.MovePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.MovePosition.html) and [Rigidbody2D.MoveRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.MoveRotation.html).
* * *
## Declaration
public void MovePositionAndRotation([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
### Parameters
Parameter | Description  
---|---  
position | The position to move the rigidbody to.  
rotation | The rotation to move the rigidbody to. Only the Z-Axis rotation is used from the full 3D Quaternion rotation.  
### Description
Moves the rigidbody position to `position` and the rigidbody angle to `rotation`.
This is a combination of calling both [MovePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.MovePosition.html) and [MoveRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.MoveRotation.html). This can be used to increase performance by not having to perform two separate calls to queue movements.  
  
For more details on the operation of movement using these methods, refer to [Rigidbody2D.MovePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.MovePosition.html) and [Rigidbody2D.MoveRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.MoveRotation.html).
* * *
