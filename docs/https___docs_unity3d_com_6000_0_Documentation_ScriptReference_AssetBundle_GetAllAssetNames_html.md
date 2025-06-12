* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.GetAllAssetNames.html

#  [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).GetAllAssetNames
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
public string[] GetAllAssetNames(); 
### Description
Return all Asset names in the AssetBundle.
Only works for normal AssetBundles (non-streamed Scene AssetBundle), otherwise an empty string array is returned. The names are the project-relative path of each Asset file, unless a different name was specified at build time.  
  
Additional resources: [AssetBundleBuild.addressableNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild-addressableNames.html)
* * *
