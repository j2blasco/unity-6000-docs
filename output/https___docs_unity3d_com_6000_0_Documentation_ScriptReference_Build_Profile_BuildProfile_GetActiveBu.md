* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.GetActiveBuildProfile.html

#  [BuildProfile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.html).GetActiveBuildProfile
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
public static [Build.Profile.BuildProfile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.html) GetActiveBuildProfile(); 
### Returns
**BuildProfile** The active build profile. Returns null when a platform profile is active. 
### Description
Gets the active build profile.
Additional resources: [Platform profile](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Build.Profile;  
  
public static class Builder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.Builder.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build/Build Active Profile")]
    public static void BuildActiveProfile()
    {
        var options = new BuildPlayerWithProfileOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWithProfileOptions.html)
        {
            buildProfile = BuildProfile.GetActiveBuildProfile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.GetActiveBuildProfile.html)(),
            locationPathName = "Builds/MyBuild"
        };  
  
        BuildPipeline.BuildPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html)(options);
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build/Set macOS Build Profile")]
    public static void SetActiveBuildProfile()
    {
        var specificBuildProfile = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<BuildProfile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.html)>(
            "Assets/Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html)/Build Profiles/macOS.asset"
        );
        BuildProfile.SetActiveBuildProfile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.SetActiveBuildProfile.html)(specificBuildProfile);
    }
}

```

* * *
