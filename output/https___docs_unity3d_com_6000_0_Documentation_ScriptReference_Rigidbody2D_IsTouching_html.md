* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.IsTouching.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).IsTouching
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
public bool IsTouching([Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) collider); 
### Parameters
Parameter | Description  
---|---  
collider | The collider to check if it is touching any of the collider(s) attached to this rigidbody.  
### Returns
**bool** Whether the `collider` is touching any of the collider(s) attached to this rigidbody or not. 
### Description
Checks whether the `collider` is touching any of the collider(s) attached to this rigidbody or not.
It is important to understand that checking whether colliders are touching or not is performed against the last physics system update; that is the state of touching colliders at that time. If you have just added a new [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) or have moved a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) but a physics update has not yet taken place then the colliders will not be shown as touching. This function returns the same collision results as the physics collision or trigger callbacks.
* * *
## Declaration
public bool IsTouching([Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) collider, [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter); 
### Parameters
Parameter | Description  
---|---  
collider | The collider to check if it is touching any of the collider(s) attached to this rigidbody.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
### Returns
**bool** Whether the `collider` is touching any of the collider(s) attached to this rigidbody or not. 
### Description
Checks whether the `collider` is touching any of the collider(s) attached to this rigidbody or not with the results filtered by the `ContactFilter2D`.
It is important to understand that checking whether colliders are touching or not is performed against the last physics system update; that is the state of touching colliders at that time. If you have just added a new [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) or have moved a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) but a physics update has not yet taken place then the colliders will not be shown as touching. This function returns the same collision results as the physics collision or trigger callbacks.
* * *
## Declaration
public bool IsTouching([ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter); 
### Parameters
Parameter | Description  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
### Returns
**bool** Whether any collider is touching any of the collider(s) attached to this rigidbody or not. 
### Description
Checks whether any collider is touching any of the collider(s) attached to this rigidbody or not with the results filtered by the `ContactFilter2D`.
It is important to understand that checking whether colliders are touching or not is performed against the last physics system update; that is the state of touching colliders at that time. If you have just added a new [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) or have moved a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) but a physics update has not yet taken place then the colliders will not be shown as touching. This function returns the same collision results as the physics collision or trigger callbacks.
* * *
