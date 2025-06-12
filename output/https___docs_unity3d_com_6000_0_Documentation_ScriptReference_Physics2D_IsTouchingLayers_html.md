* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.IsTouchingLayers.html

#  [Physics2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.html).IsTouchingLayers
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
public static bool IsTouchingLayers([Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) collider, int layerMask = Physics2D.AllLayers); 
### Parameters
Parameter | Description  
---|---  
Collider | The Collider to check if it is touching Colliders on the `layerMask`.  
layerMask | Any Colliders on any of these layers count as touching.  
### Returns
**bool** Whether the `Collider` is touching any Colliders on the specified `layerMask` or not. 
### Description
Checks whether the `Collider` is touching any Colliders on the specified `layerMask` or not.
It is important to understand that checking if Colliders are touching or not is performed against the last physics engine update i.e. the state of touching Colliders at that time. If you have just added a new [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) or have moved a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) but a physics update has not yet taken place then the Colliders will not be shown as touching. The touching state is identical to that indicated by the physics collision or trigger callbacks.
* * *
