* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfModelPrefab.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).IsPartOfModelPrefab
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
public static bool IsPartOfModelPrefab([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) componentOrGameObject); 
### Parameters
Parameter | Description  
---|---  
componentOrGameObject | The object to check. Must be a component or GameObject.  
### Returns
**bool** True if the object is part of a Model Prefab. 
### Description
Returns true if the given object is part of a Model Prefab Asset or Model Prefab instance.
An object is part of a Model Prefab instance if it has a Model Prefab as outermost Prefab instance root. To get the outermost Prefab instance root, use [GetOutermostPrefabInstanceRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetOutermostPrefabInstanceRoot.html).
* * *
