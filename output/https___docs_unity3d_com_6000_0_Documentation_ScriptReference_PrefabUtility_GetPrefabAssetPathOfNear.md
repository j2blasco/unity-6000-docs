* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetPrefabAssetPathOfNearestInstanceRoot.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).GetPrefabAssetPathOfNearestInstanceRoot
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
public static string GetPrefabAssetPathOfNearestInstanceRoot([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) instanceComponentOrGameObject); 
### Parameters
Parameter | Description  
---|---  
instanceComponentOrGameObject | An object in the Prefab instance to get the asset path of.  
### Returns
**string** The asset path. 
### Description
Retrieves the asset path of the nearest Prefab instance root the specified object is part of.
The method will look in the Transform hierarchy for the GameObject or its nearest ancestor which is the root GameObject of any Prefab instance and return the asset path of that Prefab Asset.  
  
For a Prefab Variant, the variant is returned, and not its base.  
  
The method returns null if the object is not part of a Prefab instance.
* * *
