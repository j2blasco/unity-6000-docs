* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-useFullKinematicContacts.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).useFullKinematicContacts
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
useFullKinematicContacts; 
### Description
Should kinematic/kinematic and kinematic/static collisions be allowed?
By default, colliders attached to a pair of [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) that are either both set to be kinematic or kinematic and static will not collide with each other. Only [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) where one is kinematic and the other is dynamic will collide by default.  
  
This default behaviour happens when this property is set to false however, when set to true then kinematic [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) are allowed to collide with other kinematic or static [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html). When this happens, collision callbacks will be produced when kinematic/kinematic or kinematic/static pairs collide although no actual collision response will happen. In other words, callbacks will happen but the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) will allow colliders to overlap similar to the situation when a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is set to be a trigger.  
  
This can be a useful feature if detecting collisions is required with details of the contact points and collision normal but without the automatic collision response.  
  
This is only used when the [bodyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-bodyType.html) is set to [[[RigidbodyType2D.Kinematic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Kinematic.html)]].  
  
Additional resources: [bodyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-bodyType.html).
* * *
