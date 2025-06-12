* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.Setup.html

#  [AndroidProjectFilesModifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.html).Setup
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
public [Android.AndroidProjectFilesModifierContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifierContext.html) Setup(); 
### Description
A callback for setting up prerequisites for modifying custom Android Gradle project files.
You must use `Setup` if your [AndroidProjectFilesModifier.OnModifyAndroidProjectFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.OnModifyAndroidProjectFiles.html) callback depends on external dependencies such as an asset or any other file, or if it produces new files, such as custom Gradle project files.  
  
This callback should not do any modifications or produce any files by itself.
* * *
