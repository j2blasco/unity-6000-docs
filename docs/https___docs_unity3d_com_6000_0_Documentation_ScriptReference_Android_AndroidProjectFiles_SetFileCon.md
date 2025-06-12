* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.SetFileContents.html

#  [AndroidProjectFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.html).SetFileContents
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
public void SetFileContents(string path, byte[] contents); 
### Parameters
Parameter | Description  
---|---  
path | The file to write to. This path is relative to the Gradle project path.  
contents | Byte array contents.  
### Description
Sets the content of a new file to the specified bytes.
To use this method, you must first declare the new file in [AndroidProjectFilesModifier.Setup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.Setup.html) using the [AndroidProjectFilesModifierContext.AdditionalOutputs.AddFileWithContents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifierContext.AdditionalOutputs.AddFileWithContents.html) method.
* * *
