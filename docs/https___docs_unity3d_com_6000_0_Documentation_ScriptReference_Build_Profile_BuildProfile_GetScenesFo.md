* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.GetScenesForBuild.html

#  [BuildProfile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.html).GetScenesForBuild
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
public EditorBuildSettingsScene[] GetScenesForBuild(); 
### Returns
**EditorBuildSettingsScene[]** The list of scenes used when building with the build profile. If the build profile is overriding the global scenes, returns the scenes specified in the build profile. Otherwise, returns the global scenes. 
### Description
Obtains the list of scenes used when building with the build profile.
Additional resources: [BuildProfile.overrideGlobalScenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile-overrideGlobalScenes.html), [BuildProfile.scenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile-scenes.html), [EditorBuildSettings.globalScenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings-globalScenes.html).
* * *
