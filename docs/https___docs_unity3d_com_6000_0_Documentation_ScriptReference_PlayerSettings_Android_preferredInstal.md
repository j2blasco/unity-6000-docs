* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-preferredInstallLocation.html

#  [PlayerSettings.Android](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android.html).preferredInstallLocation
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
[AndroidPreferredInstallLocation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidPreferredInstallLocation.html) preferredInstallLocation; 
### Description
Preferred application install location.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Build;  
  
public class PreferredInstallLocationSample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build/Preferred Install Location[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilePathAttribute.Location.html) Sample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.UI.Sample.html)")]
    public static void BuildPreferredInstallLocationSample()
    {
        PlayerSettings.SetScriptingBackend[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetScriptingBackend.html)(NamedBuildTarget.Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.Android.html), ScriptingImplementation.IL2CPP[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptingImplementation.IL2CPP.html));
        PlayerSettings.Android.targetArchitectures[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-targetArchitectures.html) = AndroidArchitecture.ARM64[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidArchitecture.ARM64.html);  
  
        //Set preferredInstallLocation
        PlayerSettings.Android.preferredInstallLocation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-preferredInstallLocation.html) = AndroidPreferredInstallLocation.Auto[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidPreferredInstallLocation.Auto.html);  
  
        BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html) options = new BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html)();
        options.scenes = new[] { "Assets/Scenes/SampleScene.unity" };
        options.locationPathName = "Build/AndroidBuild.apk";
        options.target = BuildTarget.Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.Android.html);
        options.targetGroup = BuildTargetGroup.Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.Android.html);
        BuildPipeline.BuildPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html)(options);
    }
}

```

* * *
