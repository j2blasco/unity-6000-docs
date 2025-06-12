* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWithProfileOptions-assetBundleManifestPath.html

#  [BuildPlayerWithProfileOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWithProfileOptions.html).assetBundleManifestPath
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
assetBundleManifestPath; 
### Description
The path to a manifest file describing all the AssetBundles used in the build (optional).
When you call [BuildPipeline.BuildAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html) to create your AssetBundles, Unity will also generate a .manifest file with a file name matching the parent directory. You can assign the path to this manifest file to `assetBundleManifestPath` to ensure that a player build doesn't strip any types used in your AssetBundles.  
  
You don't need to set this property when using `link.xml` files, or when generating AssetBundles using the [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest) package.  
  
For more information about code stripping, refer to [Managed code stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/ManagedCodeStripping.html).
* * *
