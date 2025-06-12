* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableMassProperties.html

# ModifiableMassProperties
struct in UnityEngine
/
Implemented in:[UnityEngine.PhysicsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PhysicsModule.html)
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
Mass-related modifiable properties of a contact pair.
Mostly useful to make a collider appear lighter to the solver than it actually is when the bodies in this contact pair have very different mass values.
### Properties
Property | Description  
---|---  
[inverseInertiaScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableMassProperties-inverseInertiaScale.html) | The inverse inertia scaling that the solver should apply to the first body of this contact pair.  
[inverseMassScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableMassProperties-inverseMassScale.html) | The inverse mass scaling that the solver should apply to the first body of this contact pair.  
[otherInverseInertiaScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableMassProperties-otherInverseInertiaScale.html) | The inverse inertia scaling that the solver should apply to the second body of this contact pair.  
[otherInverseMassScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableMassProperties-otherInverseMassScale.html) | The inverse mass scaling that the solver should apply to the second body of this contact pair.  
* * *
