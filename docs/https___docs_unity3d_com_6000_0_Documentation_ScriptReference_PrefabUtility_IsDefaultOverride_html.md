* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsDefaultOverride.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).IsDefaultOverride
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
public static bool IsDefaultOverride([PropertyModification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyModification.html) modification); 
### Parameters
Parameter | Description  
---|---  
modification | The modification for the property in question.  
### Returns
**bool** True if the property is a default override. 
### Description
Returns true if the given modification is considered a [default override](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsDefaultOverride.html).
Certain properties on the root GameObject of a Prefab instance are considered default overrides. These are overridden by default and are usually rarely applied or reverted. Most apply and revert operations will ignore default overrides.  
  
The default overrides are:  
  
Root GameObject - name  
  
Root Transform - localPosition - localRotation - localEulerAnglesHint (internal property) - rootOrder (internal property)  
  
Root RectTransform - same properties as in Transform - anchoredPosition - sizeDelta - anchorMin - anchorMax - pivot  
  
These properties are default overrides in order to prevent common mistakes when applying or reverting an entire Prefab instance. Typically, you will not want the position and rotation of a Prefab instance to get updates from the position and rotation of the Prefab Asset itself. Most of the other properties that are default overrides are similar in nature in that they relate to the basic alignment of the instance.  
  
Using Apply All or Revert All on a Prefab instance will not affect default overrides. The only way to apply or revert a default override is to use the context menu for the property itself. This corresponds to the methods [PrefabUtility.ApplyPropertyOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPropertyOverride.html) and [PrefabUtility.RevertPropertyOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertPropertyOverride.html).  
  
Since they are not affected by most apply and revert operations, default overrides that are overridden don't get a blue margin in the Inspector like other overridden properties do. They also don’t show up as overrides in the Overrides dropdown. They are however bold when overridden in order to make it possible to tell of they are overridden or not.  
  
Default overrides only exists for the root GameObject (and its Transform/RectTransform) in an outermost Prefab instance. This includes outermost Prefab instances inside other Prefabs, as seen in Prefab Mode.
* * *
