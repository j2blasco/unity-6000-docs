* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.Load.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).Load
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
public static Object Load(string path); 
### Description
Load a built-in resource.
This function will look in Assets/Editor Default Resources/ + path for the resource. If not there, it will try the built-in editor resources by name.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class LoadExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Load Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) Example")]
    static void loadExample()
    {
        Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) tex  = (Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html))EditorGUIUtility.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.Load.html)("aboutwindow.mainheader");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Got: " + tex.name + " !");  
  
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) r = GameObject.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html)("Cube").GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
        r.sharedMaterial.mainTexture = tex;
    }
}

```

* * *
