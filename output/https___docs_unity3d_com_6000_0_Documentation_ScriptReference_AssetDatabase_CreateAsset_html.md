* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).CreateAsset
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
public static void CreateAsset([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) asset, string path); 
### Parameters
Parameter | Description  
---|---  
asset | Object to use in creating the asset.  
path | Filesystem path for the new asset.  
### Description
Creates a new native Unity asset.
Use this method to create a native Unity asset. Native assets are those created by Unity (either in the editor or via script), and are in Unity’s serialized format.  
  
If an asset already exists the path you specify it will be overwritten with your new asset. The path is relative to the project folder, for example: "Assets/MyStuff/hello.mat".  
  
An asset file can contain multiple assets. After you create an asset file, you can add more assets to the file using AssetDatabase.AddObjectToAsset.  
  
You cannot use this method to create an asset from a GameObject. To do this, use the [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html) class instead.  
  
Be aware that if you are adding multiple objects to an asset, the order in which the objects are added does not matter. In other words, the first asset added will not be special within the asset file, and there is no "root" asset or object to which other assets are added to.  
  
Note: You must ensure that the path you provide uses a native asset extension. For example, ".mat" for materials, ".cubemap" for cubemaps, ".GUISkin" for skins, ".anim" for animations and ".asset" for arbitrary other assets. The full list of native asset extensions can be found [here under the details for NativeFormatImporter](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabaseRefreshing.html). This method is not intended for creating non-native assets, such as text files or image files.  
  
Note: You cannot create assets inside the streaming assets folder (Assets/StreamingAssets).  
  
Note: You should not create assets during import, for example from within a ScriptedImporter or Postprocessor. Doing so can prevent the import process from producing consistent (deterministic) results. See [Importer Consistency](https://docs.unity3d.com/6000.0/Documentation/Manual/ImporterConsistency.html) for more information.  
  
_This method reports an error in the console if you use an incorrect extension, or if you try to create an asset in the streaming assets folder. These errors will become exceptions in a future release of Unity._  
  
_This method reports a warning in the console if used during an import, but this will become an exception in a future release of Unity._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CreateMaterialExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)/Create Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)")]
    static void CreateMaterial()
    {
        // Create a simple material asset  
  
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Specular"));
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(material, "Assets/MyMaterial.mat");  
  
        // Print the path of the created asset
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(material));
    }
}

```

* * *
