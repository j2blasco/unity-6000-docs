* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-sharedMaterial.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).sharedMaterial
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
[PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html) sharedMaterial; 
### Description
The [PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html) that is applied to this collider.
If no [PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html) is specified then the [Rigidbody2D.sharedMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-sharedMaterial.html) on the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) that the collider is attached to is used. If the collider is not attached to a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) or no [Rigidbody2D.sharedMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-sharedMaterial.html) is specified then the global [PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html) is used. If no global [PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html) is specified then the defaults are: [PhysicsMaterial2D.friction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D-friction.html) = 0.4 and [PhysicsMaterial2D.bounciness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D-bounciness.html) = 0.  
  
In other words, a [PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html) specified on the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) has priority over a [PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html) specified on a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) which has priority over the global [PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html).  
  
Additional resources: [Rigidbody2D.sharedMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-sharedMaterial.html) & [PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html).
* * *
