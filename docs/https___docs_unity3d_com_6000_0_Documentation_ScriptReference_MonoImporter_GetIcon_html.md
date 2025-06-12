* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.GetIcon.html

#  [MonoImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html).GetIcon
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
public [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetIcon(); 
### Returns
**Texture2D** Returns the custom icon that will be associated with the imported [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html). If no custom icon will be associated with the imported [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html), returns null. 
### Description
Gets the icon to associate with the imported [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html).
Additional resources: [MonoImporter.SetIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.SetIcon.html), [EditorGUIUtility.GetIconForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetIconForObject.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Get Icon for MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) from MonoImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html)")]
    public static void GetIconForMonoScriptFromMonoImporter()
    {
        var assetPath = "Assets/MyMonoBehaviour.cs";
        var monoImporter = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(assetPath) as MonoImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html);
        var icon = monoImporter.GetIcon();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Icon for {assetPath} is {icon}");
    }
}

```

* * *
