* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.DetailedBuildReport.html

#  [BuildOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html).DetailedBuildReport
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
Generates detailed information in the [BuildReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html).
The BuildReport object returned by [BuildPipeline.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html) will contain additional data about build times and contents. This might lead to slightly longer build time, typically by a few percents.  
  
The following script example illustrates how to use `DetailedBuildReport` when building a Player. Create a project and add the script under Assets/Editor.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class DetailedBuildReportExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build/DetailedBuildReport example")]
    public static void MyBuild()
    {
        BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html) buildPlayerOptions = new BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html)();
        buildPlayerOptions.scenes = new[] { "Assets/scene.unity" };
        buildPlayerOptions.locationPathName = "DetailedReportBuild/MyGame.exe";
        buildPlayerOptions.target = BuildTarget.StandaloneWindows64[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.StandaloneWindows64.html);  
  
        buildPlayerOptions.options = BuildOptions.DetailedBuildReport[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.DetailedBuildReport.html);  
  
        var buildReport = BuildPipeline.BuildPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html)(buildPlayerOptions);
    }
}

```

  1. Run the `Build/DetailedBuildReport` scripts example.
  2. Access the information about the build process in the `buildReport` variable which you can process using the [BuildReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) API.
  3. Refer to the [Build Report Inspector source script ](https://github.com/Unity-Technologies/BuildReportInspector) to find illustrations on how to query the [BuildReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) API.


* * *
