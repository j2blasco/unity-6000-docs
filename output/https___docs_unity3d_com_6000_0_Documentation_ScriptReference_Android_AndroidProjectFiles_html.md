* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.html

# AndroidProjectFiles
class in UnityEditor.Android
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
A class to store C# representations of all Gradle project files.
The class is used to pass Gradle configuration files objects to the [AndroidProjectFilesModifier.OnModifyAndroidProjectFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.OnModifyAndroidProjectFiles.html) callback.
### Properties
Property | Description  
---|---  
[AdditionalLibrariesBuildGradleFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.AdditionalLibrariesBuildGradleFiles.html) | A representation of the build.gradle files that were added to plugins (libraries) that didn't have a build.gradle file.  
### Public Methods
Method | Description  
---|---  
[GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.GetData.html) | Gets data that was set in the Setup method.  
[SetBuildGradleFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.SetBuildGradleFile.html) | Sets a new build.gradle file.  
[SetFileContents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.SetFileContents.html) | Sets the content of a new file to the specified bytes.  
[SetGradlePropertiesFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.SetGradlePropertiesFile.html) | Sets a new gradle.properties file.  
[SetGradleSettingsFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.SetGradleSettingsFile.html) | Sets a new settings.gradle file.  
[SetManifestFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.SetManifestFile.html) | Sets a new Android Manifest file.  
* * *
