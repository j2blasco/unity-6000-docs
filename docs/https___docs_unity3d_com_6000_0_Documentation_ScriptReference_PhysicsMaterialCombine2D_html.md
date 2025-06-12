* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.html

# PhysicsMaterialCombine2D
enumeration
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
### Description
Describes how [PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html) friction and bounciness are combined when two [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) come into contact.
When two [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) come into contact, each might has its own [PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html) assigned, and each with its own [PhysicsMaterial2D.friction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D-friction.html) and [PhysicsMaterial2D.bounciness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D-bounciness.html). To calculate the collision response, both friction and bounciness values must be combined using the [PhysicsMaterialCombine2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.html) provides multiple algorithms.  
  
**Note:** Each [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) can have a unique [PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html) with different combine modes for friction and bounciness. When different modes are set, the mode with the highest priority is used in this order: [Maximum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.Maximum.html), [Minimum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.Minimum.html), [Multiply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.Multiply.html), [Mean](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.Mean.html), and [Average](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.Average.html). For example, if one [PhysicsMaterial2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D.html) uses [Average](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.Average.html) while the other uses [Maximum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.Maximum.html), the [Maximum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.Maximum.html) combine function is used because it has higher priority.  
  
Additional resources: [PhysicsMaterial2D.frictionCombine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D-frictionCombine.html), [PhysicsMaterial2D.bounceCombine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial2D-bounceCombine.html)
### Properties
Property | Description  
---|---  
[Average](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.Average.html) | Uses an Average algorithm when combining friction or bounciness.  
[Mean](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.Mean.html) | Uses a Geomtric Mean algorithm when combining friction or bounciness.  
[Multiply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.Multiply.html) | Uses a Multiply algorithm when combining friction or bounciness i.e. the product of the two values is used.  
[Minimum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.Minimum.html) | Uses a Minimum algorithm when combining friction or bounciness i.e. the minimum of the two values is used.  
[Maximum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterialCombine2D.Maximum.html) | Uses a Maximum algorithm when combining friction or bounciness i.e. the maximum of the two values is used.  
* * *
