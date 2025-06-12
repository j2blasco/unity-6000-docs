* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-includeLayers.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).includeLayers
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
[LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) includeLayers; 
### Description
The additional layers that all [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)s attached to this [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) should include when deciding if a the [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) can come into contact with another [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).
The Layer Collision Matrix defines which layers can contact other layers. Use this property to specify additional layers that all [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)s attached to this [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html) instance can contact.  
  
**NOTE** : Layers can be included or excluded differently depending on the settings of each [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) instance. As such, there could be a conflicting decision for whether two [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) instances can come into contact with each other. To learn how Unity decides this, see [Collider.layerOverridePriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-layerOverridePriority.html).  
  
Additional resources: [Collider.excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-excludeLayers.html), [ArticulationBody.excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-excludeLayers.html), [Rigidbody.includeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-includeLayers.html), [Rigidbody.excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-excludeLayers.html).
* * *
