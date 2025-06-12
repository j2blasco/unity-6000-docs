* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.ClosestPoint.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).ClosestPoint
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
position | The position from which to find the closest point on this Collider.  
### Returns
**Vector2** A point on the perimeter of this Collider that is closest to the specified `position`. 
### Description
Returns a point on the perimeter of this Collider that is closest to the specified `position`.
This function provides the ability to calculate the closest point of a specified `position` to the perimeter of any [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) type.  
  
In the case where the `position` is inside this Collider or this Collider is disabled, then the input `position` is returned instead.  
  
Additional resources: [Rigidbody2D.ClosestPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.ClosestPoint.html) & [Physics2D.ClosestPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.ClosestPoint.html).
* * *
