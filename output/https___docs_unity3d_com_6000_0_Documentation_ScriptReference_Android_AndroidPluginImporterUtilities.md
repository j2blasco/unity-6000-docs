* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidPluginImporterUtilities.SetAndroidSharedLibraryType.html

#  [AndroidPluginImporterUtilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidPluginImporterUtilities.html).SetAndroidSharedLibraryType
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
public static void SetAndroidSharedLibraryType([PluginImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html) importer, [Android.AndroidSharedLibraryType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidSharedLibraryType.html) type); 
### Description
Sets the type of content that the shared library contains.
This is only applicable for plugins that use the `.so` file extension.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Android;  
  
public class SharedLibraryTypes : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    const string SharedLibraryPath = "Insert_Path_To_SharedLibrary.so";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SharedLibraryTypes")]
    static void Init()
    {
        SharedLibraryTypes window = (SharedLibraryTypes)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(SharedLibraryTypes), true, "SharedLibraryTypes");
        window.Show();
    }  
  
    void SetFileToBe(AndroidSharedLibraryType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidSharedLibraryType.html) type)
    {
        PluginImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html) imp = (PluginImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html))PluginImporter.GetAtPath(SharedLibraryPath);
        imp.SetAndroidSharedLibraryType(type);
    }  
  
    void OnGUI()
    {
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Set file to be symbol"))
            SetFileToBe(AndroidSharedLibraryType.Symbol[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidSharedLibraryType.Symbol.html));  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Set file to be executable"))
            SetFileToBe(AndroidSharedLibraryType.Executable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidSharedLibraryType.Executable.html));
    }
}

```

* * *
