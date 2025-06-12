* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-showAllContacts.html

#  [PhysicsVisualizationSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.html).showAllContacts
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
showAllContacts; 
### Description
Whether the [PhysicsDebugWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsDebugWindow.html) visualizes all contacts.
If you set this property to false, only the following Colliders report collisions to the [PhysicsDebugWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsDebugWindow.html): physics objects that have MonoBehaviour scripts with OnCollisionsEnter, OnCollisionsStay, and OnCollisionExit methods implemented, and Colliders that have Collider.generatesContacts property set to `true`.  
  
If you set this property to true, all physics objects report all collisions to the [PhysicsDebugWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsDebugWindow.html). If this property is set to true, Unity still takes [PhysicsVisualizationSettings.useContactFiltering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-useContactFiltering.html) into account.  
  
In Play mode, if you switch this property from false to true, this doesn't affect the Colliders that have already been initialized. In Play mode, if you switch this property from true to false, this hides the contact visualization but the Colliders remain subscribed.
* * *
