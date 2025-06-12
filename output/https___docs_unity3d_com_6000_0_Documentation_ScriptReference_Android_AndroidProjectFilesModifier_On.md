* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.OnModifyAndroidProjectFiles.html

#  [AndroidProjectFilesModifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.html).OnModifyAndroidProjectFiles
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
public void OnModifyAndroidProjectFiles([Android.AndroidProjectFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.html) projectFiles); 
### Description
A callback for modifying files in the Android Gradle project after Unity Editor creates it.
Unity invokes this callback after it creates the Android Gradle project. Use this method to modify Android Gradle project files. This callback passes an [AndroidProjectFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.html) object which contains C# representations of Android Gradle project files. For information on when Unity invokes this method during the build process, refer to [How Unity builds Android applications](https://docs.unity3d.com/6000.0/Documentation/Manual/how-unity-builds-android-applications.html).  
  
**Note** : You can use this method to modify Android Gradle project files in custom modules only. 
* * *
