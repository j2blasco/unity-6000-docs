* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-includeLayers.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).includeLayers
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
[LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) includeLayers; 
### Description
The additional Layers that this [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) should include when deciding if a contact with another [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) should happen or not.
The Layer Collision Matrix defines which Layers can and cannot contact other Layers. This property allows you to specify additional Layers that this specific [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) instance can contact.  
  
**NOTE** : Because Layers can be included or excluded differently depending on the settings of each [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) instance, there is the potential for a conflicting decision for whether contact should happen or not when two [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) instances come into contact with each other. You can find the detailed rules for how Unity arbitrates this decision in the [Collider2D.layerOverridePriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-layerOverridePriority.html) documentation.  
  
Additional resources: [Collider2D.excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-excludeLayers.html), [Rigidbody2D.includeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-includeLayers.html) & [Rigidbody2D.excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-excludeLayers.html).
* * *
