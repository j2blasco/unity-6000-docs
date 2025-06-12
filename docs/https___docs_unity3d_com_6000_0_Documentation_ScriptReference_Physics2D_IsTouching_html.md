* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.IsTouching.html

#  [Physics2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.html).IsTouching
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
public static bool IsTouching([Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) collider1, [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) collider2); 
### Parameters
Parameter | Description  
---|---  
collider1 | The Collider to check if it is touching `collider2`.  
collider2 | The Collider to check if it is touching `collider1`.  
### Returns
**bool** Whether `collider1` is touching `collider2` or not. 
### Description
Checks whether the passed Colliders are in contact or not.
It is important to understand that checking whether Colliders are touching or not is performed against the last physics engine update; that is the state of touching Colliders at that time. If you have just added a new [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) or have moved a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) but a physics update has not yet taken place then the Colliders will not be shown as touching. This function returns the same collision results as the physics collision or trigger callbacks.
* * *
## Declaration
public static bool IsTouching([Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) collider, [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter); 
### Parameters
Parameter | Description  
---|---  
Collider | The Collider to check if it is touching any other Collider filtered by the `contactFilter`.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
### Returns
**bool** Whether the `Collider` is touching any other Collider filtered by the `contactFilter` or not. 
### Description
Checks whether the passed Colliders are in contact or not.
It is important to understand that checking whether Colliders are touching or not is performed against the last physics engine update; that is the state of touching Colliders at that time. If you have just added a new [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) or have moved a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) but a physics update has not yet taken place then the Colliders will not be shown as touching. This function returns the same collision results as the physics collision or trigger callbacks.
* * *
## Declaration
public static bool IsTouching([Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) collider1, [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) collider2, [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter); 
### Parameters
Parameter | Description  
---|---  
collider1 | The Collider to check if it is touching `collider2`.  
collider2 | The Collider to check if it is touching `collider1`.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
### Returns
**bool** Whether `collider1` is touching `collider2` or not. 
### Description
Checks whether the passed Colliders are in contact or not.
It is important to understand that checking whether Colliders are touching or not is performed against the last physics engine update; that is the state of touching Colliders at that time. If you have just added a new [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) or have moved a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) but a physics update has not yet taken place then the Colliders will not be shown as touching. This function returns the same collision results as the physics collision or trigger callbacks.
* * *
