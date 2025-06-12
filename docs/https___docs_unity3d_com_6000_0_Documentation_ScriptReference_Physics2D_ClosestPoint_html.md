* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.ClosestPoint.html

#  [Physics2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.html).ClosestPoint
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) ClosestPoint([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) collider); 
### Parameters
Parameter | Description  
---|---  
position | The position from which to find the closest point on the specified `Collider`.  
Collider | The Collider on which to find the closest specified `position`.  
### Returns
**Vector2** A point on the perimeter of the `Collider` that is closest to the specified `position`. 
### Description
Returns a point on the perimeter of the `Collider` that is closest to the specified `position`.
This function provides the ability to calculate the closest point of a specified `position` to the perimeter of any [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) type.  
  
In the case where the `position` is inside the `Collider` or the `Collider` is disabled, then the input `position` is returned instead.
* * *
## Declaration
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) ClosestPoint([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) rigidbody); 
### Parameters
Parameter | Description  
---|---  
position | The position from which to find the closest point on the specified `rigidbody`.  
rigidbody | The Rigidbody on which to find the closest specified `position`.  
### Returns
**Vector2** A point on the perimeter of a Collider attached to the `rigidbody` that is closest to the specified `position`. 
### Description
Returns a point on the perimeter of all enabled Colliders attached to the `rigidbody` that is closest to the specified `position`.
This function provides the ability to calculate the closest point of a specified `position` to the perimeter of any enabled [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) type attached to the specified [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).  
  
In the case where the `position` is inside any of the enabled [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) attached to the `rigidbody`, the input `position` is returned instead.
* * *
