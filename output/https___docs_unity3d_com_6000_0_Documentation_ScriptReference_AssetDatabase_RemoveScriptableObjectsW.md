* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RemoveScriptableObjectsWithMissingScript.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).RemoveScriptableObjectsWithMissingScript
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
public static int RemoveScriptableObjectsWithMissingScript(string assetPath); 
### Parameters
Parameter | Description  
---|---  
assetPath | The path to the asset file to check.  
### Returns
**int** The number of ScriptableObject-derived objects in the file which were removed. 
### Description
Removes any ScriptableObject instances from the given asset file which cannot be loaded because their scripts could not be found.
If you delete the script which defines a type of ScriptableObject, all instances of that ScriptableObject in your assets become unloadable. This also happens if you move or rename the script outside of Unity without also moving or renaming the script's .meta file accordingly. This method allows you to remove any such unloadable ScriptableObject instances from an asset. You can check whether there are unloadable ScriptableObject instances in your assets without removing them, by using [AssetDatabase.GetScriptableObjectsWithMissingScriptCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetScriptableObjectsWithMissingScriptCount.html).  
  
Note: This function can only be used with [native asset files](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsNativeAsset.html). If you pass a non-native asset file, it will throw an exception.  
  
You must call [AssetDatabase.SaveAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html) to save the changes to your asset, after using this method.  
  
Additional resources: [AssetDatabase.GetScriptableObjectsWithMissingScriptCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetScriptableObjectsWithMissingScriptCount.html), [GameObjectUtility.RemoveMonoBehavioursWithMissingScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.RemoveMonoBehavioursWithMissingScript.html).
* * *
