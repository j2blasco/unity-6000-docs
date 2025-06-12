* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html

# BuildPlayerOptions
struct in UnityEditor
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
Provide various options to control the behavior of [BuildPipeline.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html).
Additional resources: [EditorBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.html), [BuildPlayerWindow.DefaultBuildMethods.GetBuildPlayerOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWindow.DefaultBuildMethods.GetBuildPlayerOptions.html)
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class BuildPlayerOptionsExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build/Log Build Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html)")]
    public static void MyBuild()
    {
        // Log some of the current build options retrieved from the Build Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) Window
        BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html) buildPlayerOptions = BuildPlayerWindow.DefaultBuildMethods.GetBuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWindow.DefaultBuildMethods.GetBuildPlayerOptions.html)(new BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html)());
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html)\n"
            + "Scenes: " + string.Join(",", buildPlayerOptions.scenes) + "\n"
            + "Build location: " + buildPlayerOptions.locationPathName + "\n"
            + "Options[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Options.html): " + buildPlayerOptions.options + "\n"
            + "Target[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.html): " + buildPlayerOptions.target);
    }
}

```

### Properties
Property | Description  
---|---  
[assetBundleManifestPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions-assetBundleManifestPath.html) | The path to an manifest file describing all of the asset bundles used in the build (optional).  
[extraScriptingDefines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions-extraScriptingDefines.html) | The additional preprocessor defines you can specify while compiling assemblies for the Player. These defines are appended to the existing Scripting Define Symbols list configured in the Player settings.  
[locationPathName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions-locationPathName.html) | The path where the application will be built.  
[options](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions-options.html) | Additional BuildOptions, like whether to run the built player.  
[scenes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions-scenes.html) | The Scenes to be included in the build.  
[subtarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions-subtarget.html) | The Subtarget to build.  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions-target.html) | The BuildTarget to build.  
[targetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions-targetGroup.html) | The BuildTargetGroup to build.  
* * *
