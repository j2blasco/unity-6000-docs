* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-enableCollision.html

#  [Joint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html).enableCollision
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
enableCollision; 
### Description
Should the two [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) connected with this joint collide with each other?
When this is disabled, the two [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) connected with this joint will never produce collision or trigger contacts with each other. When this is enabled, the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) are allowed to produce collision or trigger contacts should they be configured to do so.  
  
NOTE: When this is disabled but no [Joint2D.connectedBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-connectedBody.html) is specified then no collision or trigger contacts are produced with any implicitly Static [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) i.e. [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that are not attached to any [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).  
  
Additional resources: [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) class, [connectedBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-connectedBody.html).
* * *
