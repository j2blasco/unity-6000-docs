* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary.html

# BuildSummary
struct in UnityEditor.Build.Reporting
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
Contains overall summary information about a build.
### Properties
Property | Description  
---|---  
[buildEndedAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-buildEndedAt.html) | The time the build ended.  
[buildStartedAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-buildStartedAt.html) | The time the build was started.  
[buildType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-buildType.html) | The type of build.  
[guid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-guid.html) | The Application.buildGUID of the build.  
[multiProcessEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-multiProcessEnabled.html) | Whether the multi-process option was enabled for the build.  
[options](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-options.html) | The BuildOptions used for the build, as passed to BuildPipeline.BuildPlayer.  
[outputPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-outputPath.html) | The output path for the build, as provided to BuildPipeline.BuildPlayer.  
[platform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-platform.html) | The platform that the build was created for.  
[platformGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-platformGroup.html) | The platform group the build was created for.  
[result](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-result.html) | The outcome of the build.  
[totalErrors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-totalErrors.html) | The total number of errors and exceptions recorded during the build process.  
[totalSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-totalSize.html) | The total size of the build output, in bytes.  
[totalTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-totalTime.html) | The total time taken by the build process.  
[totalWarnings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary-totalWarnings.html) | The total number of warnings recorded during the build process.  
### Public Methods
Method | Description  
---|---  
[GetSubtarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary.GetSubtarget.html) | The subtarget that the build was created for.  
* * *
