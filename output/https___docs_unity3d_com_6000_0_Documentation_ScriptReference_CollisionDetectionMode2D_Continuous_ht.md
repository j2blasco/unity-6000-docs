* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode2D.Continuous.html

#  [CollisionDetectionMode2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode2D.html).Continuous
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
Ensures that all collisions are detected when a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) moves.
When using this mode, the collision detection system will detect all collisions in the path that a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) moves along therefore preventing colliders attached to the rigidbody passing through other colliders at higher speeds. The physics system will also calculate a time-of-time calculation to ensure that the new position of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) is at the correct contact position with no overlaps. This mode however is much more expensive to calculate and should only be used when objects are moving at higher speeds or you are encountering objects overlapping or passing through each other.  
  
Additional resources: [Rigidbody2D.collisionDetectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-collisionDetectionMode.html).
* * *
