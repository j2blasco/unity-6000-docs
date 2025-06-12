* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).SaveAssets
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
public static void SaveAssets(); 
### Description
Writes all unsaved asset changes to disk.
Identical to [EditorApplication.SaveAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.SaveAssets.html) except not permitted to be called during serialization.  
  
When calling this function, [AssetModificationProcessor.OnWillSaveAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.OnWillSaveAssets.html) will be invoked, allowing you to override which files are saved to disk.  
  
[EditorApplication.SaveAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.SaveAssets.html) will be deprecated in a future release. Please use [SaveAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html) to maintain future compatibility.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.Text;  
  
public class SaveAssetsExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("APIExamples/SaveAssets")]
    static void AssetsToBeSaved()
    {
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] colorList = new[] { Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html), Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html), Color.black[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-black.html), Color.gray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-gray.html) };  
  
        for (int i = 0; i < colorList.Length; ++i)
        {
            Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Specular"));
            var materialName = "material_" + i + ".mat";
            AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(material, "Assets/Artifacts/" + materialName);  
  
            material.SetColor("_Color", colorList[i]);
        }  
  
        AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();
    }
}  
  
public class OutputListOfFilesToSave : UnityEditor.AssetModificationProcessor
{
    //Will be invoked once for each call to CreateAsset()
    //and once for calling AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)()
    static string[] OnWillSaveAssets(string[] paths)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnWillSaveAssets invoked");  
  
        StringBuilder assetsToBeSaved = new StringBuilder();
        assetsToBeSaved.AppendLine();  
  
        foreach (string path in paths)
        {
            assetsToBeSaved.Append(path);
            assetsToBeSaved.AppendLine();
        }  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Assets to be saved:" + assetsToBeSaved.ToString());  
  
        return paths;
    }
}

```

* * *
