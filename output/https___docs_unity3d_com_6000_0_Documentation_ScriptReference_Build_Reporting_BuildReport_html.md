* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html

# BuildReport
class in UnityEditor.Build.Reporting
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
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
The BuildReport API gives you information about the Unity build process.
A BuildReport object is returned by [BuildPipeline.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html) and can be used to discover information about the files output, the build steps taken, and other platform-specific information such as native code stripping.  
  
For AssetBundle builds the BuildReport is available by calling [GetLatestReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.GetLatestReport.html) immediately after calling [BuildPipeline.BuildAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html). 
```
using System.IO;
using System.Linq;
using System.Text;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Build;
using UnityEditor.Build.Reporting;
using UnityEngine;  
  
public class BuildReportExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Build AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html)")]
    static public void BuildBundles()
    {
        string buildOutputDirectory = "BuildOutput";
        if (!Directory.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.Exists.html)(buildOutputDirectory))
            Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)(buildOutputDirectory);  
  
        var bundleDefinitions = new AssetBundleBuild[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild.html)[]
        {
            new AssetBundleBuild[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild.html)()
            {
                assetBundleName = "MyBundle",
                assetNames = new string[] { "Assets/Scenes/SampleScene.unity" }
            }
        };  
  
        BuildPipeline.BuildAssetBundles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html)(
            buildOutputDirectory,
            bundleDefinitions,
            BuildAssetBundleOptions.ForceRebuildAssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.ForceRebuildAssetBundle.html),
            EditorUserBuildSettings.activeBuildTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-activeBuildTarget.html));  
  
        BuildReport[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) report = BuildReport.GetLatestReport[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.GetLatestReport.html)();
        if (report != null)
        {
            var sb = new StringBuilder();
            sb.AppendLine("Build result   : " + report.summary.result);
            sb.AppendLine("Build size     : " + report.summary.totalSize + " bytes");
            sb.AppendLine("Build time     : " + report.summary.totalTime);
            sb.AppendLine("Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Error.html) summary  : " + report.SummarizeErrors());
            sb.Append(LogBuildReportSteps(report));
            sb.AppendLine(LogBuildMessages(report));
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(sb.ToString());
        }
        else
        {
            // Certain errors like invalid input can fail the build immediately, with no BuildReport[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) written
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) build failed");
        }
    }  
  
    public static string LogBuildReportSteps(BuildReport[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) buildReport)
    {
        var sb = new StringBuilder();  
  
        sb.AppendLine($"Build steps: {buildReport.steps.Length}");
        int maxWidth = buildReport.steps.Max(s => s.name.Length + s.depth) + 3;
        foreach (var step in buildReport.steps)
        {
            string rawStepOutput = new string('-', step.depth + 1) + ' ' + step.name;
            sb.AppendLine($"{rawStepOutput.PadRight(maxWidth)}: {step.duration:g}");
        }
        return sb.ToString();
    }  
  
    public static string LogBuildMessages(BuildReport[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) buildReport)
    {
        var sb = new StringBuilder();
        foreach (var step in buildReport.steps)
        {
            foreach (var message in step.messages)
                // If desired, this logic could ignore any Info or Warning messages to focus on more serious messages
                sb.AppendLine($"[{message.type}] {message.content}");
        }  
  
        string messages = sb.ToString();
        if (messages.Length > 0)
            return "Messages logged during Build:\n" + messages;
        else
            return "";
    }
}  
  
// For the purpose of demonstration, this callback logs different types of errors and forces a build failure
[BuildCallbackVersion(1)]
class MyTroublesomeBuildCallback : IProcessSceneWithReport[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IProcessSceneWithReport.html)
{
    public int callbackOrder { get { return 0; } }
    public void OnProcessScene(UnityEngine.SceneManagement.Scene scene, BuildReport[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) report)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("MyTroublesomeBuildCallback called for " + scene.name);
        Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Logging an error");  
  
        throw new BuildFailedException[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildFailedException.html)("Forcing the build to stop");
    }
}

```

### Properties
Property | Description  
---|---  
[packedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport-packedAssets.html) | An array of all the PackedAssets generated by the build process.  
[scenesUsingAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport-scenesUsingAssets.html) | An optional array of ScenesUsingAssets generated by the build process if BuildOptions.DetailedBuildReport was used during the build.  
[steps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport-steps.html) | An array of all the BuildSteps that took place during the build process.  
[strippingInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport-strippingInfo.html) | The StrippingInfo object for the build.  
[summary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport-summary.html) | A BuildSummary containing overall statistics and data about the build process.  
### Public Methods
Method | Description  
---|---  
[GetFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.GetFiles.html) | Returns an array of all the files output by the build process.  
[SummarizeErrors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.SummarizeErrors.html) | Returns a string summarizing any errors that occurred during the build  
### Static Methods
Method | Description  
---|---  
[GetLatestReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.GetLatestReport.html) | Return the build report generated by the most recent Player or AssetBundle build  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
