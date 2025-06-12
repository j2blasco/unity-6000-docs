* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundlesParameters-bundleDefinitions.html

#  [BuildAssetBundlesParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundlesParameters.html).bundleDefinitions
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
bundleDefinitions; 
### Description
Array defining the name and contents of each AssetBundle. (optional)
An array of [AssetBundleBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild.html) structs that define the names and contents of each AssetBundle, e.g. the "Build Map". When provided Unity builds only the AssetBundles as specified, and ignores any AssetBundle assignments that had been made in the Editor user interface. This approach makes it convenient to programmatically define AssetBundle contents or to perform builds with different content within the same project.  
  
This field can be left unassigned, e.g. null, in which case [BuildPipeline.BuildAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html) uses the AssetBundle assignments made in the Editor to determine the AssetBundles and their contents. Those assignments are stored in the AssetDatabase and in the .meta files and can also be accessed programmatically, see [AssetImporter.assetBundleName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetBundleName.html), [AssetDatabase.GetAssetPathsFromAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPathsFromAssetBundle.html) and [AssetDatabase.GetImplicitAssetBundleName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImplicitAssetBundleName.html). 
* * *
