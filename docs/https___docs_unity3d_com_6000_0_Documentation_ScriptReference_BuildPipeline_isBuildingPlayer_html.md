* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline-isBuildingPlayer.html

#  [BuildPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.html).isBuildingPlayer
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
isBuildingPlayer; 
### Description
Is a player currently being built?
This returns true during Player builds and AssetBundle builds.  
  
It can be used to check the context inside script code that could be triggered during a build, for example when [ExecuteAlways](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteAlways.html) is being used on a [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).  
  
Additional resources: [BuildPipeline.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html), [BuildPipeline.BuildAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html)
* * *
