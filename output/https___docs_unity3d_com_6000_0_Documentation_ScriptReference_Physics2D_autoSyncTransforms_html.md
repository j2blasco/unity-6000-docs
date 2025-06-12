* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-autoSyncTransforms.html

#  [Physics2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.html).autoSyncTransforms
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
autoSyncTransforms; 
### Description
Set whether to automatically sync changes to the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) component with the physics engine. 
When a [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) component changes, any [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) or [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) on that [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) or its children may need to be repositioned, rotated or scaled depending on the change to the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html). You can control if the changes made to the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) are automatically applied to the correct components by setting this property true. When set to false, synchronization only occurs prior to the physics simulation step during the Fixed Update. You can also manually synchronize transform changes using [Physics2D.SyncTransforms](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.SyncTransforms.html).  
  
**Note** : When autoSyncTransforms is set to true, repeatedly changing a Transform and then performing a physics query can cause performance loss. To avoid affecting performance, set autoSyncTransforms to false if you want to perform multiple Transform changes and queries in succession. You should only set autoSyncTransforms to true for physics backwards compatibility in existing projects made before Unity 2017.2. For projects made in Unity 2017.2 onwards, turn this option off.
* * *
