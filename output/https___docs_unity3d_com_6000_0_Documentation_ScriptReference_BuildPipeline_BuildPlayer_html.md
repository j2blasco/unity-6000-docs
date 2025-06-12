* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html

#  [BuildPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.html).BuildPlayer
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
public static [Build.Reporting.BuildReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) BuildPlayer([BuildPlayerOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html) buildPlayerOptions); 
### Parameters
Parameter | Description  
---|---  
buildPlayerOptions | Provide various options to control the behavior of [BuildPipeline.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html).  
### Returns
**BuildReport** A [BuildReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) object containing build process information. 
### Description
Builds a player.
Use this function to programatically create a build of your project.  
  
Calling this method will invalidate any variables in the editor script that reference GameObjects, so they will need to be reacquired after the call.  
  
Scripts can run at strategic points during the build by implementing one of the supported callback interfaces, for example [BuildPlayerProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPlayerProcessor.html), [IPreprocessBuildWithReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPreprocessBuildWithReport.html), [IProcessSceneWithReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IProcessSceneWithReport.html) and [IPostprocessBuildWithReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPostprocessBuildWithReport.html).  
  
Note: Be aware that changes to [scripting symbols](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html) only take effect at the next domain reload, when scripts are recompiled.  
  
This means if you make changes to the defined scripting symbols via code using PlayerSettings.SetDefineSymbolsForGroup without a domain reload before calling this function, those changes won't take effect.  
  
It also means that the built-in scripting symbols defined for the current active target platform (such as UNITY_STANDALONE_WIN, or UNITY_ANDROID) remain in place even if you try to build for a different target platform, which can result in the wrong code being compiled into your build.  
  
Additional resources: [BuildPlayerWindow.DefaultBuildMethods.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWindow.DefaultBuildMethods.BuildPlayer.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEditor.Build.Reporting;  
  
// Output the build size or a failure depending on BuildPlayer.  
  
public class BuildPlayerExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build/Build iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS.html)")]
    public static void MyBuild()
    {
        BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html) buildPlayerOptions = new BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html)();
        buildPlayerOptions.scenes = new[] { "Assets/Scene1.unity", "Assets/Scene2.unity" };
        buildPlayerOptions.locationPathName = "iOSBuild";
        buildPlayerOptions.target = BuildTarget.iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.iOS.html);
        buildPlayerOptions.options = BuildOptions.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.None.html);  
  
        BuildReport[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) report = BuildPipeline.BuildPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html)(buildPlayerOptions);
        BuildSummary[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary.html) summary = report.summary;  
  
        if (summary.result == BuildResult.Succeeded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildResult.Succeeded.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Build succeeded: " + summary.totalSize + " bytes");
        }  
  
        if (summary.result == BuildResult.Failed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildResult.Failed.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Build failed");
        }
    }
}

```

* * *
## Declaration
public static [Build.Reporting.BuildReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) BuildPlayer([BuildPlayerWithProfileOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWithProfileOptions.html) buildPlayerWithProfileOptions); 
### Parameters
Parameter | Description  
---|---  
buildPlayerWithProfileOptions | Provide various options to control the behavior of [BuildPipeline.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html) when using a [build profile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.html).  
### Returns
**BuildReport** A [BuildReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) object containing build process information. 
### Description
Builds a player from a specific build profile.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Build.Reporting;
using UnityEditor.Build.Profile;
using UnityEngine;  
  
public class BuildPlayerWithBuildProfileExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build/Build iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS.html) Demo")]
    public static void MyBuild()
    {
        BuildProfile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.html) buildProfile = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<BuildProfile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.html)>("Assets/Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html)/Build Profiles/iOSDemo.asset");
        BuildPlayerWithProfileOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWithProfileOptions.html) options = new BuildPlayerWithProfileOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWithProfileOptions.html)()
        {
            buildProfile = buildProfile,
            locationPathName = "iOSDemoBuild",
            options = BuildOptions.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.None.html),
        };  
  
        BuildReport[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) report = BuildPipeline.BuildPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html)(options);
        BuildSummary[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary.html) summary = report.summary;  
  
        // Output the build size or a failure depending on BuildPlayer.
        if (summary.result == BuildResult.Succeeded[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildResult.Succeeded.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Build succeeded: " + summary.totalSize + " bytes");
        }  
  
        if (summary.result == BuildResult.Failed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildResult.Failed.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Build failed");
        }
    }
}
```

* * *
## Declaration
public static [Build.Reporting.BuildReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) BuildPlayer(string[] levels, string locationPathName, [BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) target, [BuildOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html) options); 
## Declaration
public static [Build.Reporting.BuildReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) BuildPlayer(EditorBuildSettingsScene[] levels, string locationPathName, [BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) target, [BuildOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html) options); 
### Parameters
Parameter | Description  
---|---  
levels | The scenes to include in the build. If empty, the build includes only the current open scene. Paths are relative to the project folder, for example `Assets/MyLevels/MyScene.unity`.  
locationPathName | The path where the application will be built. For information on the platform extensions to include in the path, refer to [Build path requirements for target platforms](https://docs.unity3d.com/6000.0/Documentation/Manual/build-path-requirements.html).  
target | The [BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) to build.  
options | Additional [BuildOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html), like whether to run the built player.  
### Returns
**BuildReport** A [BuildReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) object containing build process information. 
### Description
Builds a Player. These overloads are still supported, but will be replaced. Please use BuildPlayer([BuildPlayerOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html) buildPlayerOptions) and BuildPlayer([BuildPlayerWithProfileOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWithProfileOptions.html) buildPlayerWithProfileOptions) instead.
* * *
