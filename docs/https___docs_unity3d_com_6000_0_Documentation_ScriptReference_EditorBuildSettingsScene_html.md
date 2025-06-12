* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettingsScene.html

# EditorBuildSettingsScene
class in UnityEditor
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
### Description
Represents entries in the Scenes list, as displayed in the [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html) window.
This class contains the path of a Scene and an enabled flag that indicates whether the Scene is enabled in the Build Profiles window or not.  
  
You can use this class in combination with [EditorBuildSettings.scenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings-scenes.html) to populate the list of Scenes to include in the build via script. This is useful when you create custom editor scripts to automate your build pipeline.  
  
See [EditorBuildSettings.scenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings-scenes.html) for an example script. Additional resources: [BuildPipeline.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html).
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettingsScene-enabled.html) | Whether this Scene is enabled for inclusion in the build.  
[path](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettingsScene-path.html) | The file path of the Scene.  
* * *
