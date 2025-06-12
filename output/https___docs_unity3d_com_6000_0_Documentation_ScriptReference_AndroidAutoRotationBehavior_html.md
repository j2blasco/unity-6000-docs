* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidAutoRotationBehavior.html

# AndroidAutoRotationBehavior
enumeration
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
Options to control the application window orientation when **Default orientation** is set to **Auto rotation**.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Build;  
  
public class AutoRotationBehaviorSample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build/AutoRotationBehavior Sample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.UI.Sample.html)")]
    public static void BuildAutoRotationBehaviorSample()
    {
        PlayerSettings.SetScriptingBackend[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetScriptingBackend.html)(NamedBuildTarget.Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.Android.html), ScriptingImplementation.IL2CPP[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptingImplementation.IL2CPP.html));  
  
        PlayerSettings.Android.targetArchitectures[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-targetArchitectures.html) = AndroidArchitecture.ARM64[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidArchitecture.ARM64.html);
        
        // Set autoRotation behavior to a value from AndroidAutoRotationBehavior[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidAutoRotationBehavior.html) enum
        // Replace with Sensor if needed
        PlayerSettings.Android.autoRotationBehavior[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-autoRotationBehavior.html) = AndroidAutoRotationBehavior.User[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidAutoRotationBehavior.User.html);
        
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
### Properties
Property | Description  
---|---  
[User](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidAutoRotationBehavior.User.html) | Application window rotates based on the device’s auto rotate orientation settings.  
[Sensor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidAutoRotationBehavior.Sensor.html) | Application window rotates based on the device’s orientation sensor.  
* * *
