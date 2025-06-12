* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-collisionDetectionMode.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).collisionDetectionMode
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html "Go to Rigidbody Component in the Manual")
[CollisionDetectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.html) collisionDetectionMode; 
### Description
The Rigidbody's collision detection mode.
Use this to set up a Rigidbody for continuous collision detection. You can use continuous collision detection to prevent fast moving objects from passing through other objects without detecting collisions.   
  
For best results, set this value to [CollisionDetectionMode.ContinuousDynamic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.ContinuousDynamic.html) for fast moving objects. For other objects which these need to collide with, set it to [CollisionDetectionMode.Continuous](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.Continuous.html). These two options impact physics performance. Alternatively, you can use [CollisionDetectionMode.ContinuousSpeculative](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.ContinuousSpeculative.html), which has less of an impact on performance and can also be used on kinematic objects. If you don't have issues with collisions of fast objects, leave it set to the default value of [CollisionDetectionMode.Discrete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.Discrete.html).  
  
Continuous Collision Detection is only supported for Rigidbodies with Sphere-, Capsule- or BoxColliders. Additional resources: [CollisionDetectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.html).
* * *
