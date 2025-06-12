* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetPropertyModifications.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).GetPropertyModifications
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
public static PropertyModification[] GetPropertyModifications([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) targetPrefab); 
### Parameters
Parameter | Description  
---|---  
targetPrefab | Can be a Prefab instance in the scene or a Prefab instance in an Prefab Asset (e.g a Variant asset).  
### Description
Returns all modifications that have been applied to a particular Prefab instance in a Scene or modifications for a Prefab instance in an Asset.  
  
See [SetPropertyModifications](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SetPropertyModifications.html) for details about the fields of the returned [PropertyModification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyModification.html) objects.  
  
An alternative approach to getting property overrides information for a Prefab instance is to use the [GetObjectOverrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetObjectOverrides.html) API which also has Apply and Revert functionality.  
  
When using GetPropertyModifications bear in mind that: 
  * it will return both default and non-default overrides
  * It can return overrides for all child GameObjects and their Components
  * it can return overrides that are no longer valid.


Additional resources: [GetObjectOverrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetObjectOverrides.html) [GetAddedComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetAddedComponents.html) [GetRemovedComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetRemovedComponents.html) [GetAddedGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetAddedGameObjects.html) [GetRemovedGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetRemovedGameObjects.html).
* * *
