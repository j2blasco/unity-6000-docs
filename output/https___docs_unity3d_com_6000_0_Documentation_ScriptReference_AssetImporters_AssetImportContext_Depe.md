* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.DependsOnArtifact.html

#  [AssetImportContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html).DependsOnArtifact
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
public void DependsOnArtifact(string path); 
## Declaration
public void DependsOnArtifact(GUID guid); 
## Declaration
public void DependsOnArtifact([Experimental.ArtifactKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.ArtifactKey.html) key); 
### Parameters
Parameter | Description  
---|---  
path | The path of the Asset whose artifact should be the dependency. Note: Although the dependency is the artifact (import result) which is stored in the library folder, this parameter is the path to the Asset in the Assets folder, and _not_ a path to the artifact in the Library folder.  
guid | The guid of the artifact dependency.  
key | The artifact key of the artifact dependency.  
### Description
Setup artifact dependency to an asset.
An artifact dependency is a dependency where an Asset depends on the import result (known as an artifact) of another Asset. If you change an Asset that has been marked as a dependency, all Assets which depend on it will also get reimported (after the dependency has been imported).  
  
Note: If you specify an Asset as a dependency that doesn't exist or hasn't yet been imported, the dependency is still registered. It is registered as an un-imported Asset. When the Asset is later imported, all Assets which depend on it will also get reimported.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.AssetImporters;  
  
class TextureInfo : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public int height;
}  
  
[ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)(1, "cube")]
public class CubeWithTextureImporter : ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)
{
    public override void OnImportAsset(AssetImportContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) ctx)
    {
        var assetDependency = "Assets/MyTexture.png";  
  
        ctx.DependsOnArtifact(assetDependency);  
  
        var texture = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)>(assetDependency);  
  
        if (texture != null)
        {
            var textureInfo = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<TextureInfo>();
            textureInfo.height = texture.height;
            ctx.AddObjectToAsset("TextureInfo", textureInfo);
        }
    }
}

```

* * *
