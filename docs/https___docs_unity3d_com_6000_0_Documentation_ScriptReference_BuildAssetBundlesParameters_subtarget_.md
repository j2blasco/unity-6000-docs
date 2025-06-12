* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundlesParameters-subtarget.html

#  [BuildAssetBundlesParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundlesParameters.html).subtarget
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
subtarget; 
### Description
The subtarget to build. (optional)
For some BuildTargets the behaviour of a build can be influenced by using this field. The supported values are based on target-specific enums, for example [MobileTextureSubtarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MobileTextureSubtarget.html).  
  
The subtarget can be assigned using the build settings UI. To build with the current build settings, the [BuildAssetBundlesParameters.targetPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundlesParameters-targetPlatform.html) field should be left unassigned (e.g. with the value 0).  
  
Additional resources: [EditorUserBuildSettings.standaloneBuildSubtarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-standaloneBuildSubtarget.html), [EditorUserBuildSettings.androidBuildSubtarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-androidBuildSubtarget.html), [EditorUserBuildSettings.webGLBuildSubtarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-webGLBuildSubtarget.html).
* * *
