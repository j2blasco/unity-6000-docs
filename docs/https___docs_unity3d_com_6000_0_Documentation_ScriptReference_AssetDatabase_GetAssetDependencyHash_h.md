* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetDependencyHash.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetAssetDependencyHash
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
public static [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) GetAssetDependencyHash(string path); 
## Declaration
public static [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) GetAssetDependencyHash(GUID guid); 
### Parameters
Parameter | Description  
---|---  
path | Path to the asset.  
guid | GUID of the asset.  
### Returns
**Hash128** Aggregate hash. 
### Description
Returns the hash of all the dependencies of an asset.
The hash aggregates the following: source asset path, source asset, meta file, target platform and importer version. The change of this hash indicates that the imported asset may have changed so the relevant asset bundles should be rebuilt.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Dependency Hash Example")]
    public static void DependencyHashExample()
    {
        //Load a Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html), change its shader and save it
        var matPath = "Assets/Material.mat";
        var asset = (Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html))AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(matPath);
        asset.shader = Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Unlit/Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)");
        AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();  
  
        //Print out the hash into the console
        var hash = AssetDatabase.GetAssetDependencyHash[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetDependencyHash.html)(matPath);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(hash);  
  
        //Change the Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) on the Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) and save it
        asset.shader = Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard");
        AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();  
  
        //Hash will be different
        hash = AssetDatabase.GetAssetDependencyHash[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetDependencyHash.html)(matPath);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(hash);
    }
}
```

* * *
