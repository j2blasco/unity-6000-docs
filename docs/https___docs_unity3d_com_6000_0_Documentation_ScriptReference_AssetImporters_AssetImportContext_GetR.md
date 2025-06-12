* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.GetReferenceToAssetMainObject.html

#  [AssetImportContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html).GetReferenceToAssetMainObject
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
public Object GetReferenceToAssetMainObject(string path); 
### Parameters
Parameter | Description  
---|---  
path | The location of the asset to get the reference from.  
### Returns
**Object** Returns the main asset instance if it exists and is already imported, returns null otherwise. 
### Description
Returns the main asset from the given path (if it exists) and automatically adds a dependency on its path if it is the main asset type.
Calling this method during an import will make the current imported asset re-import if: - An asset is added at the given path, - The type of the asset at the given path changes, - An existing asset at the given path is deleted or moved.  
  
If the returned asset is used for more than referencing, like reading its content and using its values, [AssetImportContext.DependsOnArtifact](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.DependsOnArtifact.html) or [AssetImportContext.DependsOnSourceAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.DependsOnSourceAsset.html) should be used instead.  
  
For example, this method should be used to reference Textures added to or created during an import. Since we are only setting a reference to the texture from the Material, it is not necessary to re-import when the texture itself changes, only when it is added or removed from the project.
```
using UnityEngine;
using UnityEditor.AssetImporters;  
  
[ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)(1, "customMaterial")]
public class MaterialCreatorExample : ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)
{
    public override void OnImportAsset(AssetImportContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) ctx)
    {
        var mat = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard"));
        var texturePath = $"{System.IO.Path.GetDirectoryName(ctx.assetPath)}/{System.IO.Path.GetFileNameWithoutExtension(ctx.assetPath)}_Diffuse.png";
        mat.mainTexture = ctx.GetReferenceToAssetMainObject(texturePath) as Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html);
        ctx.AddObjectToAsset("mat", mat);
    }
}
```

* * *
