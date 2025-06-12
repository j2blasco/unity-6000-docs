* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfNonAssetPrefabInstance.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).IsPartOfNonAssetPrefabInstance
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
public static bool IsPartOfNonAssetPrefabInstance([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) componentOrGameObject); 
### Parameters
Parameter | Description  
---|---  
componentOrGameObject | The object to check. Must be a component or GameObject.  
### Returns
**bool** True if the object is part of a Prefab instance that is not inside a Prefab Asset. 
### Description
Returns true if the given object is part of a Prefab instance that is not part of a Prefab Asset.
Returns true if the object is part of a Prefab instance in a scene.   
  
If the given object is part of a Prefab instance where the asset is missing, it will still return true.
* * *
