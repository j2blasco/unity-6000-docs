* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Static.html

#  [RigidbodyType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.html).Static
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
Sets the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) to have static behaviour.
Static behaviour stops the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) from reacting to gravity or applied forces including contacts with any other [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).  
  
This type of [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) should never repositioned explicitly. It is designed to never move.  
  
A static [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) will only collide with a dynamic [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) body type. The exception to this is if [Rigidbody2D.useFullKinematicContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-useFullKinematicContacts.html) is set to true in which case it will also collide with any [[[Kinematic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Kinematic.html)]] body types.  
  
When an attached [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is set to trigger, it will always produce a trigger for any [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) attached to [[[Dynamic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Dynamic.html)]] or [[[Kinematic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Kinematic.html)]] body types.  
  
Additional resources: [Rigidbody2D.bodyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-bodyType.html), [Rigidbody2D.useFullKinematicContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-useFullKinematicContacts.html).
* * *
