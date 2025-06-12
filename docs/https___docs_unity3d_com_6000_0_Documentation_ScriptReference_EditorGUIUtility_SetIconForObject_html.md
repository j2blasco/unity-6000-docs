* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.SetIconForObject.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).SetIconForObject
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
public static void SetIconForObject([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) icon); 
### Parameters
Parameter | Description  
---|---  
obj | The [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) or [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) to associate the icon with.  
icon | The custom icon to associate with the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) or [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html). When this value is null, the default icon is restored.  
### Description
Sets a custom icon to associate with a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) or [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html). The custom icon is displayed in the Scene view and the Inspector.
Custom icons for GameObjects are saved in the scene.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Set Custom Icon on GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)")]
    public static void SetCustomIconOnGameObject()
    {
        var go = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)();
        var icon = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)>("Assets/MyIcon.png");  
  
        EditorGUIUtility.SetIconForObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.SetIconForObject.html)(go, icon);
    }
}

```

Using this function, you can set custom icons directly on a [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html). However the next time the script is reimported, the change will be lost.  
  
To make the custom icon persistent, call [MonoImporter.SetIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.SetIcon.html) and [AssetImporter.SaveAndReimport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SaveAndReimport.html). If the script is in a managed plugin, call [PluginImporter.SetIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.SetIcon.html) instead of [MonoImporter.SetIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.SetIcon.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Set Custom Icon on MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html)")]
    public static void SetCustomIconOnMonoScript()
    {
        var monoImporter = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)("Assets/MyMonoBehaviour.cs") as MonoImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html);
        var monoScript = monoImporter.GetScript();
        var icon = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)>("Assets/MyIcon.png");  
  
        EditorGUIUtility.SetIconForObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.SetIconForObject.html)(monoScript, icon);  
  
        // make the custom icon persistent
        monoImporter.SetIcon(icon);
        monoImporter.SaveAndReimport();
    }
}

```

When you set custom icons from a GUI, it is recommended that you defer reimport until the GUI is closed. If you reimport before the GUI is closed, the domain reload caused by recompiling the script could lead to a poor user experience.  
  
Additional resources: [MonoImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html), [PluginImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html).
* * *
