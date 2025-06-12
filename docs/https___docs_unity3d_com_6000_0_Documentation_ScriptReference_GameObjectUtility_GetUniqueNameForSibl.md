* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.GetUniqueNameForSibling.html

#  [GameObjectUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.html).GetUniqueNameForSibling
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
## Declaration
public static string GetUniqueNameForSibling([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent, string name); 
### Parameters
Parameter | Description  
---|---  
parent | Target parent for a new [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Null means root level.  
name | Requested name for a new [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).  
### Returns
**string** Unique name for a new [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). 
### Description
You can use this method before instantiating a new sibling, or before parenting one GameObject to another, to ensure the new child GameObject has a unique name compared to its siblings in the hierarchy.
To use this method, you must provide a "target parent", and a "requested name". The method uses an incremental numeric suffix appended to the name to avoid duplicate names.  
  
If the target parent that you specify does _not_ already have a child with the requested name that you specify, the method will return the requested name. If the target parent _does_ have a child object matching the requested name, the method will add an incremental number after the requested name until it finds one that is unique. This is useful when trying to avoid duplicate naming.  
  
Note: You should use this method _before_ the GameObject becomes a child of the target parent. If you use this method _after_ the GameObject is already a child of the target parent, it will detect its own name among the siblings as a conflict! If you want to perform the check after the GameObject is a child of the target parent, you can use [GameObjectUtility.EnsureUniqueNameForSibling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.EnsureUniqueNameForSibling.html) instead.  
  
Additional resources: [GameObjectUtility.EnsureUniqueNameForSibling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.EnsureUniqueNameForSibling.html), [ObjectNames.GetUniqueName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.GetUniqueName.html).
* * *
