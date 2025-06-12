* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.Distance.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).Distance
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
public [ColliderDistance2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D.html) Distance([Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) collider); 
### Parameters
Parameter | Description  
---|---  
collider | A collider used to calculate the minimum separation against this collider.  
### Returns
**ColliderDistance2D** The minimum separation of `collider` and this collider. 
### Description
Calculates the minimum separation of this collider against another collider.
A valid `collider` must be provided for the [ColliderDistance2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D.html) to be valid. If there are any problems with `collider` or this [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) such as they are disabled or do not contain any collision shapes then the separation will be invalid as indicated by [ColliderDistance2D.isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-isValid.html).  
  
Additional resources: [Physics2D.Distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Distance.html) and [Rigidbody2D.Distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Distance.html).
* * *
## Declaration
public [ColliderDistance2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D.html) Distance([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) thisPosition, float thisAngle, [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) collider, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, float angle); 
### Parameters
Parameter | Description  
---|---  
thisPosition | The position to use for this Collider.  
thisAngle | The rotation to use for this Collider.  
collider | A collider used to calculate the minimum separation against this Collider.  
position | The position to use for the specified `collider`.  
angle | The rotation to use for the specified `collider`.  
### Returns
**ColliderDistance2D** The minimum separation of `collider` and this collider. 
### Description
A valid `collider` must be provided for the [ColliderDistance2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D.html) to be valid. If there are any problems with `collider` or this [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) such as they are disabled or do not contain any collision shapes then the separation will be invalid as indicated by [ColliderDistance2D.isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-isValid.html).
A valid `collider` must be provided for the [ColliderDistance2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D.html) to be valid. If there are any problems with `collider` or this [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) such as they are disabled or do not contain any collision shapes then the separation will be invalid as indicated by [ColliderDistance2D.isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-isValid.html).  
  
**NOTE** : The positions and angles used here represent the position of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) the respective [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is attached to. If the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is offset from the center of mass then the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) will use the same offset. This can be confusing so it is recommened that only [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that align with the center of mass are used. If not then you must take this into account. If the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is not attached to a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html), this call cannot be used and will result in a warning.  
  
Additional resources: [Physics2D.Distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Distance.html) and [Rigidbody2D.Distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Distance.html).
* * *
