* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetIconForObject.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).GetIconForObject
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
public static [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetIconForObject([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
### Parameters
Parameter | Description  
---|---  
obj | The [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) or [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) to query  
### Returns
**Texture2D** Returns the custom icon associated with the object. If there is no custom icon associated with the object, returns null. 
### Description
Gets the custom icon associated with an object. Only GameObjects and MonoScripts have associated custom icons.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Get Icon for GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)")]
    public static void GetIconForGameObject()
    {
        var go = GameObject.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html)("Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)");
        var icon = EditorGUIUtility.GetIconForObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetIconForObject.html)(go);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Icon for " + go + " is " + icon);
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Get Icon for MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html)")]
    public static void GetIconForMonoScript()
    {
        var monoScript = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html)>("Assets/MyMonoBehaviour.cs");
        var icon = EditorGUIUtility.GetIconForObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetIconForObject.html)(monoScript);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Icon for " + monoScript.GetClass().FullName + " is " + icon);
    }
}

```

* * *
