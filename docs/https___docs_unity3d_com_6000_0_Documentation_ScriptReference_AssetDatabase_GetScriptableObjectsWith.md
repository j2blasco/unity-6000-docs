* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetScriptableObjectsWithMissingScriptCount.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetScriptableObjectsWithMissingScriptCount
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
public static int GetScriptableObjectsWithMissingScriptCount(string assetPath); 
### Parameters
Parameter | Description  
---|---  
assetPath | The path to the asset file to check.  
### Returns
**int** The number of ScriptableObject instances in the file which are missing their associated scripts. 
### Description
Checks how many unloadable ScriptableObject instances are present in the specified asset.
If you delete the script which defines a type of ScriptableObject, all instances of that ScriptableObject in your assets become unloadable. This also happens if you move or rename the script outside of Unity without also moving or renaming the script's .meta file accordingly. This method allows you to check whether an asset contains any such unloadable ScriptableObject instances due to missing scripts. You can remove unloadable ScriptableObject instances from your assets by using [AssetDatabase.RemoveScriptableObjectsWithMissingScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RemoveScriptableObjectsWithMissingScript.html).  
  
Note: This function can only be used with [native asset files](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsNativeAsset.html). If you pass a non-native asset file, it will throw an exception.  
  
Additional resources: [AssetDatabase.RemoveScriptableObjectsWithMissingScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RemoveScriptableObjectsWithMissingScript.html), [GameObjectUtility.GetMonoBehavioursWithMissingScriptCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.GetMonoBehavioursWithMissingScriptCount.html).
* * *
