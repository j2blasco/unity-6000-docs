* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.SetManifestFile.html

#  [AndroidProjectFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.html).SetManifestFile
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
public void SetManifestFile(string path, [Unity.Android.Gradle.Manifest.AndroidManifestFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.AndroidManifestFile.html) manifest); 
### Parameters
Parameter | Description  
---|---  
path | The file path to place the `Manifest` file at. This path is relative to the gradle project path.  
manifest | The representation of Android Manifest file.  
### Description
Sets a new `Android Manifest` file.
To use this method, you must also declare your new file in [AndroidProjectFilesModifier.Setup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.Setup.html) using the [AndroidProjectFilesModifierContext.AdditionalOutputs.AddManifestFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifierContext.AdditionalOutputs.AddManifestFile.html) method.
* * *
