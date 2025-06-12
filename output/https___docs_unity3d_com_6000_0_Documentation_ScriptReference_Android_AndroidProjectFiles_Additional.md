* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.AdditionalLibrariesBuildGradleFiles.html

#  [AndroidProjectFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.html).AdditionalLibrariesBuildGradleFiles
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
AdditionalLibrariesBuildGradleFiles; 
### Description
A representation of the `build.gradle` files that were added to plugins (libraries) that didn't have a `build.gradle` file.
Files are located in `unityLibrary/{pluginName}/build.gradle`.  
  
If you have a plugin called `myLibrary` that doesn't contain `build.gradle` file, the file will be generated and placed in `unityLibrary/mylibrary.androidlib/build.gradle`. You can use this path to access the file object in this dictionary.
```
using System.IO;
using UnityEditor.Android;
using Unity.Android.Gradle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.html);  
  
public class ModifyProjectScript : AndroidProjectFilesModifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.html)
{
    public override void OnModifyAndroidProjectFiles(AndroidProjectFiles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFiles.html) projectFiles)
    {
        // Add a Google() repository to a build.gradle file in mylibrary.androidlib library
        var myLibraryBuildGradle = projectFiles.AdditionalLibrariesBuildGradleFiles[Path.Combine("unityLibrary", "mylibrary.androidlib", "build.gradle")];
        myLibraryBuildGradle.Repositories.AddRepository(Repositories.Google[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Repositories.Google.html));
    }
}

```

* * *
