* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-layerOverridePriority.html

#  [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).layerOverridePriority
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
layerOverridePriority; 
### Description
A decision priority assigned to this [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) used when there is a conflicting decision on whether a [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) can contact another [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).
The Layer Collision Matrix defines which layers can contact other layers. Additionally, you can include and exclude layers per [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) or for all [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)s attached to a specific [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) or [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html). Any contact involves two different [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) instances. Unfortunately this can result in one [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) deciding that it should contact the other [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html), but the other [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) deciding it shouldn't. There are rules to decide how these situations are handled.  
  
The rules for making a decision between two [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)s, referred to here as A and B, are made in the following order: 
  1. If both A and B make the same decision then use that decision.
  2. If only A or B are using a layer include or exclude override, then use the decision for A or B that has the include or exclude override specified.
  3. If both A and B are using a layer include or exclude override, then use the decision from A or B that has the higher [Collider.layerOverridePriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-layerOverridePriority.html).
  4. If A and B have the same [Collider.layerOverridePriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-layerOverridePriority.html), then the decision will be to not create a contact.


Additional resources: [Collider.includeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-includeLayers.html), [Collider.excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-excludeLayers.html), [Rigidbody.includeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-includeLayers.html), [Rigidbody.excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-excludeLayers.html), [ArticulationBody.includeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-includeLayers.html), [ArticulationBody.excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-excludeLayers.html).
* * *
