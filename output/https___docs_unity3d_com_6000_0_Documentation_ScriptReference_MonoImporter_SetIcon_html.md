* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.SetIcon.html

#  [MonoImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html).SetIcon
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
public void SetIcon([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) icon); 
### Parameters
Parameter | Description  
---|---  
icon | The custom icon to associate with the imported [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html). When the value is null, Unity restores the default icon.  
### Description
Sets a custom icon to associate with the imported [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html).
MonoScripts can have an associated custom icon. This icon is used in the Scene view, the Inspector, and the Project window.  
  
Additional resources: [MonoImporter.GetIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.GetIcon.html), [PluginImporter.SetIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetIcon.html), [EditorGUIUtility.SetIconForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.SetIconForObject.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Set Custom Icon on MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html)")]
    static void SetCustomIconOnMonoScript()
    {
        var monoImporter = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)("Assets/MyMonoBehaviour.cs") as MonoImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html);
        var icon = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)>("Assets/MyIcon.png");  
  
        monoImporter.SetIcon(icon);
        monoImporter.SaveAndReimport();
    }
}

```

* * *
