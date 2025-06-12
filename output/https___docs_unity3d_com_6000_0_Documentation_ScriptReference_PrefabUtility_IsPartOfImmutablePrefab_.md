* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfImmutablePrefab.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).IsPartOfImmutablePrefab
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
public static bool IsPartOfImmutablePrefab([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) componentOrGameObject); 
### Parameters
Parameter | Description  
---|---  
componentOrGameObject | The object to check. Must be a component or GameObject.  
### Returns
**bool** True if the object is part of a Prefab that cannot be edited. 
### Description
Returns true if the given object is part of a Prefab that cannot be edited.
If the object is part of a Prefab Asset, the asset itself is checked. If the object is part of a Prefab instance, its corresponding asset is checked.  
  
Examples of immutable Prefabs are Model Prefabs and Prefabs in read-only folders.  
  
For Prefab contents loaded in Prefab Mode, this method will not check the Prefab Asset the loaded contents are loaded from, since these Prefab contents are loaded into a preview scene and are not part of an asset while being edited in Prefab Mode. This means that for Prefab contents in Prefab Mode, the method will only return true for objects that are part of a Prefab instance that have corresponding assets that are immutable. To check if an object is part of the Prefab’s contents in Prefab Mode, use [PrefabStage.IsPartOfPrefabContents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage.IsPartOfPrefabContents.html).
* * *
