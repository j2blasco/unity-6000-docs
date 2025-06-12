* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.GetArtifactFilePath.html

#  [AssetImportContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html).GetArtifactFilePath
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
public string GetArtifactFilePath(GUID guid, string fileName); 
## Declaration
public string GetArtifactFilePath([Experimental.ArtifactKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.ArtifactKey.html) key, string fileName); 
### Parameters
Parameter | Description  
---|---  
guid | The guid of the Artifact File dependency.  
key | The Artifact key of the Artifact File dependency.  
fileName | The name of the Artifact File to depend upon. See [[AssetImportContext.GetOutputArtifactFilePath.  
### Returns
**string** The path inside the Library folder from which you can read the content of the requested Artifact File. 
### Description
Returns the path of the Artifact file that was created by another importer, and adds a dependency to that file.
This method must be used in conjunction with [AssetImportContext.GetOutputArtifactFilePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.GetOutputArtifactFilePath.html). Once an Artifact File has been created by another importer, using this method will return this Artifact File path and add a dependency to it. It is then possible to read this Artifact File's content to generate the import result. The following example shows a ScriptedImporter generating a Material and setting its base color using the first pixel color saved in an Artifact File from the example inside [AssetImportContext.GetOutputArtifactFilePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.GetOutputArtifactFilePath.html). Note: While there is no limit on how many Artifact Files are created using [AssetImportContext.GetOutputArtifactFilePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.GetOutputArtifactFilePath.html), it is only possible to depends upon the first 32 Artifact Files created by a single Asset import.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.IO;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.AssetImporters;
using UnityEngine;  
  
[ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)(1, "pixelMat", 1, AllowCaching = true)]
public class MaterialFromFirstPixel : ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)
{
    public LazyLoadReference<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)> m_Texture;  
  
    public override void OnImportAsset(AssetImportContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) ctx)
    {
        var color = Color.magenta[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-magenta.html);
        if (AssetDatabase.TryGetGUIDAndLocalFileIdentifier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)(m_Texture, out var stringGuid, out var id))
        {
            string path = string.Empty;
            if (GUID.TryParse(stringGuid, out var guid))
                path = ctx.GetArtifactFilePath(guid, "firstpixelcolor");
            else
                path = ctx.GetArtifactFilePath(AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(stringGuid), "firstpixelcolor");
            if (!string.IsNullOrEmpty(path))
            {
                var colorString = File.ReadAllText(path);
                ColorUtility.TryParseHtmlString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUtility.TryParseHtmlString.html)(colorString, out color);
            }
        }  
  
        var mat = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard"));
        mat.color = color;
        ctx.AddObjectToAsset("main", mat);
        ctx.SetMainObject(mat);
    }
}

```

* * *
## Declaration
public string GetArtifactFilePath(string path, string fileName); 
### Parameters
Parameter | Description  
---|---  
path | The path of the Asset whose Artifact File should be the dependency. Note: Although the dependency is the Artifact File (import result) which is stored in the library folder, this parameter is the path to the Asset in the Assets folder, and _not_ a path to the Artifact File in the Library folder.  
fileName | The name of the Artifact File to depend upon. See [[AssetImportContext.GetOutputArtifactFilePath.  
### Returns
**string** The path inside the Library folder from which you can read the content of the requested Artifact File. 
### Description
Returns the path of the Artifact file that was created by another importer, and adds a dependency to that file and the source asset path.
In addition to creating a dependency on the import artifact, this overload of the method also adds a dependency to the asset's path. This means if you rename or move the asset that created the artifact File in the project, Unity will re-import the asset, even if the artifact file is unchanged. This can be useful if you want to implement a functional naming convention as part of your asset import processing. Use the GUID or ArtifactKey overload to avoid depending on the asset path if you do not want this.
* * *
