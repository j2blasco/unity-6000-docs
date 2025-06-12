* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.GetIcon.html

#  [PluginImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html).GetIcon
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
public [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetIcon(string className); 
### Parameters
Parameter | Description  
---|---  
className | The fully qualified class name of a [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) imported by this plugin.  
### Returns
**Texture2D** Returns the custom icon that will be associated with the imported [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html). If no custom icon will be associated with the imported [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html), returns null. 
### Description
Gets the custom icon to associate with a MonoScript at import time.
Additional resources: [MonoScript.GetClass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.GetClass.html), Type.FullName, [PluginImporter.SetIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetIcon.html), [EditorGUIUtility.GetIconForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetIconForObject.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Get Icon for MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) from PluginImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html)")]
    public static void GetIconForMonoScriptFromPluginImporter()
    {
        var assetPath = "Assets/MyManagedPlugin.dll";
        var pluginImporter = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(assetPath) as PluginImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html);
        var monoScript = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html)>(assetPath);  
  
        var icon = pluginImporter.GetIcon(monoScript.GetClass().FullName);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Icon for " + monoScript.GetClass().FullName + " in " + assetPath + " is " + icon);
    }
}

```

* * *
