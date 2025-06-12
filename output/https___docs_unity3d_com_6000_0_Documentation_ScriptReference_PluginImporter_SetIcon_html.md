* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetIcon.html

#  [PluginImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html).SetIcon
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
public void SetIcon(string className, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) icon); 
### Parameters
Parameter | Description  
---|---  
className | The fully qualified class name of a [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) imported by this managed plugin.  
icon | The custom icon to associate with the imported [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html). When the value is null, Unity restores the default icon.  
### Description
Sets the custom icon to associate with a [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) imported by a managed plugin.
Each [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) imported by managed plugins can have an associated custom icon. This icon is used in the Scene view, the Inspector, and the Project window. To remove a [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html)'s associated custom icon, pass null to this method.  
  
Additional resources: [MonoScript.GetClass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.GetClass.html), Type.FullName, [PluginImporter.GetIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetIcon.html), [MonoImporter.SetIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.SetIcon.html), [EditorGUIUtility.SetIconForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.SetIconForObject.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Set Custom Icon on Managed Plugin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Plugin.html) MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html)")]
    static void SetCustomIconOnManagedPluginMonoScript()
    {
        var dllPath = "Assets/MyManagedPlugin.dll";
        var iconPath = "Assets/MyIcon.png";
        var pluginImporter = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(dllPath) as PluginImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html);
        var monoScript = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html)>(dllPath);
        var icon = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)>(iconPath);  
  
        pluginImporter.SetIcon(monoScript.GetClass().FullName, icon);
        pluginImporter.SaveAndReimport();
    }
}

```

* * *
