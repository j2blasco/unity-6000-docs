* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.IPostGenerateGradleAndroidProject.OnPostGenerateGradleAndroidProject.html

#  [IPostGenerateGradleAndroidProject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.IPostGenerateGradleAndroidProject.html).OnPostGenerateGradleAndroidProject
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
public void OnPostGenerateGradleAndroidProject(string path); 
### Parameters
Parameter | Description  
---|---  
path | The path to the root of the Unity library Gradle project. Note: when exporting the project, this parameter holds the path to the Unity library in the folder specified for export.  
### Description
Implement this function to receive a callback after the Android Gradle project is generated and before the build process begins. It is not called during an internal build process.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Android;
using UnityEngine;  
  
class MyCustomBuildProcessor : IPostGenerateGradleAndroidProject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.IPostGenerateGradleAndroidProject.html)
{
    public int callbackOrder { get { return 0; } }
    public void OnPostGenerateGradleAndroidProject(string path)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("MyCustomBuildProcessor.OnPostGenerateGradleAndroidProject at path " + path);
    }
}

```

* * *
