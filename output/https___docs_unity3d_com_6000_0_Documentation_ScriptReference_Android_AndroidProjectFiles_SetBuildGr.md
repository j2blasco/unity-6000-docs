* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.SetBuildGradleFile.html

#  [AndroidProjectFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.html).SetBuildGradleFile
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
public void SetBuildGradleFile(string path, [Unity.Android.Gradle.ModuleBuildGradleFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.ModuleBuildGradleFile.html) buildGradle); 
### Parameters
Parameter | Description  
---|---  
path | The file path to place the `build.gradle` file at. This path is relative to the gradle project path.  
buildGradle | The representation of module build.gradle file.  
### Description
Sets a new `build.gradle` file.
To use this method, you must also declare your new file in [AndroidProjectFilesModifier.Setup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.Setup.html) using the [AndroidProjectFilesModifierContext.AdditionalOutputs.AddBuildGradleFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifierContext.AdditionalOutputs.AddBuildGradleFile.html) method.
* * *
