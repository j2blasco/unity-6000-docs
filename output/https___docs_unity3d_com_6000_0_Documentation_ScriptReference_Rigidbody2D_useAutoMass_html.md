* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-useAutoMass.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).useAutoMass
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
useAutoMass; 
### Description
Should the total rigid-body [mass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-mass.html) be automatically calculated from the [[[Collider2D.density](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-density.html)]] of attached colliders?
When false, the explicitly set [mass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-mass.html) is used for the rigid-body mass. When true, the mass is automatically calculated from all attached [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) as a product of their [[[Collider2D.density](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-density.html)]] and area.  
  
When true, inside the Unity editor, the [[[Collider2D.density](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-density.html)]] property will appear on any attached [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) and the [mass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-mass.html) property will become read-only.  
  
When false, the [mass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-mass.html) property can be written to and the [[[Collider2D.density](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-density.html)]] property is not shown.  
  
Additional resources: [mass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-mass.html), ::[Collider2D.density](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-density.html).
* * *
