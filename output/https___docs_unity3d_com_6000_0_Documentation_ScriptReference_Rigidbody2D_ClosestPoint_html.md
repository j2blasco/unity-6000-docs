* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.ClosestPoint.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).ClosestPoint
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
public [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) ClosestPoint([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position); 
### Parameters
Parameter | Description  
---|---  
position | The position from which to find the closest point on this Rigidbody.  
### Returns
**Vector2** A point on the perimeter of a Collider attached to this rigidbody that is closest to the specified `position`. 
### Description
Returns a point on the perimeter of all enabled Colliders attached to this Rigidbody that is closest to the specified `position`.
This function provides the ability to calculate the closest point of a specified `position` to the perimeter of any enabled [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) type attached to this Rigidbody.  
  
In the case where the `position` is inside any of the enabled [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) attached to this Rigidbody, the input `position` is returned instead.
* * *
