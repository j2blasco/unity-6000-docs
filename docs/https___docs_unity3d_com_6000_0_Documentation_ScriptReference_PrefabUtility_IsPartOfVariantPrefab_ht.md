* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfVariantPrefab.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).IsPartOfVariantPrefab
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
public static bool IsPartOfVariantPrefab([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) componentOrGameObject); 
### Parameters
Parameter | Description  
---|---  
componentOrGameObject | The object to check. Must be a component or GameObject.  
### Returns
**bool** True if the object is part of a Prefab Variant. 
### Description
Returns true if the given object is part of a Prefab Variant Asset or Prefab Variant instance.
An object is part of a Prefab Variant instance if it has a Prefab Variant as its outermost Prefab instance root. To get the outermost Prefab instance root, use [GetOutermostPrefabInstanceRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetOutermostPrefabInstanceRoot.html).  
  
For Prefab contents loaded in Prefab Mode, this method will not check the Prefab Asset the loaded contents are loaded from, since these Prefab contents are loaded into a preview scene and are not part of an asset while being edited in Prefab Mode. This means that for Prefab contents in Prefab Mode, the method will only return true for objects are part of a Prefab Variant instance. To check if an object is part of the Prefab’s contents in Prefab Mode, use [PrefabStage.IsPartOfPrefabContents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage.IsPartOfPrefabContents.html).
* * *
