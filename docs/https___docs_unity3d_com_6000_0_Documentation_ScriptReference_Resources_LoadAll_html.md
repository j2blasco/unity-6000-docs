* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.LoadAll.html

#  [Resources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html).LoadAll
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
public static Object[] LoadAll(string path); 
## Declaration
public static Object[] LoadAll(string path, Type systemTypeInstance); 
### Parameters
Parameter | Description  
---|---  
path | Pathname of the target folder. When using the empty string (i.e., ""), the function will load the entire contents of the Resources folder.  
systemTypeInstance | Type filter for objects returned.  
### Description
Loads all assets in a folder or file at `path` in a Resources folder.
If `path` refers to a folder, all assets in the folder will be returned. If `path` refers to a file, only that asset will be returned. The `path` is relative to any Resources folder inside the Assets folder of your project.  
  
**Note:** All asset names and paths in Unity use forward slashes. Paths using backslashes will **not** work.
```
// Loads all assets in the "Resources[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html)/Textures" folder
// Then picks a random one from the list.
// Note: Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html) in this case returns [low,high]
// range, i.e. the high value is not included in the range.
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Object[] textures;
    private GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go;  
  
    void Start()
    {
        textures = Resources.LoadAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.LoadAll.html)("Textures", typeof(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)));  
  
        foreach (var t in textures)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(t.name);
        }  
  
        go = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 70, 150, 30), "Change texture"))
        {
            // change texture on cube
            Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture = (Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html))textures[Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0, textures.Length)];
            go.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().material.mainTexture = texture;
        }
    }
}

```

* * *
## Declaration
public static T[] LoadAll(string path); 
### Parameters
Parameter | Description  
---|---  
path | Pathname of the target folder. When using the empty string (i.e., ""), the function will load the entire contents of the Resources folder.  
### Description
Loads all assets in a folder or file at `path` in a Resources folder.
If `path` refers to a folder, all assets in the folder will be returned. If `path` refers to a file, only that asset will be returned. Only objects of type `T` will be returned. The `path` is relative to any Resources folder inside the Assets folder of your project.  
  
The script example below shows how [LoadAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.LoadAll.html) can be used with Linq.
```
// Loads all assets in the "Resources[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html)/Textures" folder
// using Linq.
using UnityEngine;
using System.Linq;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var textures = Resources.LoadAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.LoadAll.html)("Textures", typeof(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html))).Cast<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)>().ToArray();
        foreach (var t in textures)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(t.name);
    }
}

```

* * *
