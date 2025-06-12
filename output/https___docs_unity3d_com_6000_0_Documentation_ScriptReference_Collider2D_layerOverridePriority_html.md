* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-layerOverridePriority.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).layerOverridePriority
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
A decision priority assigned to this [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) used when there is a conflicting decision on whether a contact between itself and another [Collision2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.html) should happen or not.
The Layer Collision Matrix defines which Layers can and cannot contact other Layers. Addition Layer includes and excludes can be made per [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) or all [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) attached to a specific [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html). Any contact involves two different [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) instances. Unfortunately this can result in one [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) deciding that it should contact the other [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) but the other [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) deciding it should not. There are rules however in determining and ultimately arbitrating the final decision on whether a contact should be created or not.  
  
The rules for a making a decision for contact between two [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html), referred to here as A and B, are made in the following order: 
  1. If both A and B make the same decision then use that decision.
  2. If only A or B are using a Layer include or exclude then use the decision for A or B that has include or exclude specified.
  3. If both A and B are using a Layer include or exclude then use the decision from A or B that has the higher [Collider2D.layerOverridePriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-layerOverridePriority.html).
  4. If A and B have the same [Collider2D.layerOverridePriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-layerOverridePriority.html) then the decision will be to not create a contact.


Additional resources: [Collider2D.includeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-includeLayers.html), [Collider2D.excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-excludeLayers.html), [Rigidbody2D.includeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-includeLayers.html) & [Rigidbody2D.excludeLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-excludeLayers.html).
* * *
