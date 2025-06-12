* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundlesParameters-targetPlatform.html

#  [BuildAssetBundlesParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundlesParameters.html).targetPlatform
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
[BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) targetPlatform; 
### Description
The [BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) to build. (optional)
An AssetBundle is only compatible with the specific platform that it was built for, so you must produce different builds of a given bundle to use the assets on different platforms.  
  
If targetPlatform is not specified, e.g. it is 0, then the targetPlatform and subtarget fields will all be determined from the current build settings.   
  
Additional resources: [EditorUserBuildSettings.activeBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-activeBuildTarget.html).
* * *
