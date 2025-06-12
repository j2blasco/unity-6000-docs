* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-collisionDetectionMode.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).collisionDetectionMode
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html "Go to ArticulationBody Component in the Manual")
[CollisionDetectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.html) collisionDetectionMode; 
### Description
The ArticulationBody's collision detection mode.
Use this property to set up an ArticulationBody for continuous collision detection, in order to prevent fast moving objects from passing through other objects without detecting collisions. For best results, set this property to [CollisionDetectionMode.ContinuousDynamic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.ContinuousDynamic.html) for fast moving objects, and set it to [CollisionDetectionMode.Continuous](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.Continuous.html) for other objects these fast moving objects need to collide with.  
  
Note: These two options have a big impact on the physics engine processing resources. To consume fewer processing resources, you can alternatively use [CollisionDetectionMode.ContinuousSpeculative](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.ContinuousSpeculative.html) (which you can also use on kinematic objects). However, if you don't have issues with collisions of fast objects, you should leave this property set to the default value [CollisionDetectionMode.Discrete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.Discrete.html).  
  
Restriction: You can use Continuous Collision Detection only for ArticulationBodies with Sphere-, Capsule- or BoxColliders.  
  
Additional resources: [CollisionDetectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.html).
* * *
