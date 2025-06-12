* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.UnloadUnusedAssetsImmediate.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).UnloadUnusedAssetsImmediate
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
public static void UnloadUnusedAssetsImmediate(); 
## Declaration
public static void UnloadUnusedAssetsImmediate(bool includeMonoReferencesAsRoots); 
### Parameters
Parameter | Description  
---|---  
includeMonoReferencesAsRoots | When true, this method does not unload assets referenced by script properties and static variables.  
### Description
Unloads assets that are not used.
An asset is deemed to be unused if it isn't reached after walking the whole game object hierarchy, including script components. Static variables are also examined.  
  
Set the `includeMonoReferencesAsRoots` parameter to false to ignore asset references from script properties and static variables. The unloaded assets load again on first use. This parameter is true by default.  
  
This method differs from [Resources.UnloadUnusedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html) in that it will wait for asset garbage collection to finish before returning.  
  
Additional resources: [Resources.UnloadUnusedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.UnloadUnusedAssets.html).
* * *
