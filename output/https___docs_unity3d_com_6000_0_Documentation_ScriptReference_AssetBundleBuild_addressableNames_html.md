* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild-addressableNames.html

#  [AssetBundleBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild.html).addressableNames
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
addressableNames; 
### Description
Addressable name used to load an asset.
To provide custom addressable names for assets in the bundle, this array needs to be the same size as [AssetBundleBuild.assetNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild-assetNames.html). Each entry in this array will be matched to the asset in assetNames based on index. If the string in a given index in addressableNames is empty, the value in assetNames at the same index is used instead (default behaviour).  
  
Additional resources: [AssetBundle.LoadAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadAsset.html)
* * *
