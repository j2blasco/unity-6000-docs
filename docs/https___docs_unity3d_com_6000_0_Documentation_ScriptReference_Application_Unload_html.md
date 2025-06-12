* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.Unload.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).Unload
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
public static void Unload(); 
### Description
Unloads the Unity Player.
Unity triggers an [Application.unloading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-unloading.html) event and releases memory acquired by the Unity Player while keeping the current process alive. The amount of memory that is released depends on the platform. This is useful when Unity is integrated into another application (see [Unity as a Library](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary.html) as its component (for example, to display 2D/3D/AR content). When the application doesn't need content displayed by Unity anymore, you can release the associated memory by calling this method.  
  
This is currently supported on iOS, Android, and the Universal Windows Platform. On the Web platform, use the `unityInstance.Quit()` JavaScript function to shut down Unity content on a web page.  
  
On iOS and Android, Unload releases memory used by Scenes and GameObjects, but reserves some memory which is necessary for running Unity in the same process again. To learn more, see documentation on Unity as a Library for [iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-iOS.html) and [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-Android.html).  
  
On the Universal Windows Platform, unloads the Unity runtime and release all engine memory. This is similar to quitting, except that the application process doesn't exit.  
  
**Note:** This function does not return.
```
using UnityEngine;
using System.Collections;  
  
// Unload Unity when the user clicks the button. Exit is not applied to the application.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 200, 75), "Unload"))
            Application.Unload[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.Unload.html)();
    }  
  
    static void OnUnload()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Unloading the Player");
    }  
  
    [RuntimeInitializeOnLoadMethod]
    static void RunOnStart()
    {
        Application.unloading[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-unloading.html) += OnUnload;
    }
}

```

Additional resources: [Application.unloading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-unloading.html).
* * *
