* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html

# ScriptedImporter
class in UnityEditor.AssetImporters
/
Inherits from:[AssetImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.html)
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
### Description
Abstract base class for custom Asset importers.
Scripted importers are scripts that are associated with specific file extensions. They are invoked by Unity's Asset pipeline to convert the contents of associated files into Assets.  
  
Use the [ScriptedImporterAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporterAttribute.html) class to register custom importers with the Asset pipeline.  
  
The C# fields of a ScriptedImporter are serialized, exactly like fields on a MonoBehaviour. See [Script Serialization](https://docs.unity3d.com/6000.0/Documentation/Manual/script-serialization.html) for details. You can see these properties in the Inspector and use them to control the behaviour of the importer for each asset. To programmatically access the value of an asset's properties, use [AssetImporter.GetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html) and type cast the return value to the correct class derived from ScriptedImporter. After changing values, trigger a fresh import by calling [EditorUtility.SetDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetDirty.html) and then [AssetImporter.SaveAndReimport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SaveAndReimport.html). 
```
using UnityEngine;
using UnityEditor.AssetImporters;
using System.IO;  
  
[ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)(1, "cube")]
public class CubeImporter : ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)
{
    public float m_Scale = 1;  
  
    public override void OnImportAsset(AssetImportContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) ctx)
    {
        var cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        var position = JsonUtility.FromJson[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.FromJson.html)<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)>(File.ReadAllText(ctx.assetPath));  
  
        cube.transform.position = position;
        cube.transform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(m_Scale, m_Scale, m_Scale);  
  
        // 'cube' is a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and will be automatically converted into a Prefab
        // (Only the 'Main Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)' is eligible to become a Prefab.)
        ctx.AddObjectToAsset("main obj", cube);
        ctx.SetMainObject(cube);  
  
        var material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard"));
        material.color = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);  
  
        // Assets must be assigned a unique identifier string consistent across imports
        ctx.AddObjectToAsset("my Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)", material);  
  
        // Assets that are not passed into the context as import outputs must be destroyed
        var tempMesh = new Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)();
        DestroyImmediate(tempMesh);
    }
}

```

### Public Methods
Method | Description  
---|---  
[OnImportAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.OnImportAsset.html) | This method must by overriden by the derived class and is called by the Asset pipeline to import files.  
[SupportsRemappedAssetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.SupportsRemappedAssetType.html) | Override this method if your ScriptedImporter supports remapping specific asset types.  
### Messages
Message | Description  
---|---  
[GatherDependenciesFromSourceFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.GatherDependenciesFromSourceFile.html) | A static callback that you can implement to set up artifact dependencies to other Assets, and optimize the order your assets are imported.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.OnValidate.html) | This function is called when the importer is loaded or a value is changed in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.Reset.html) | Reset to default values.  
### Inherited Members
### Properties
Property | Description  
---|---  
[assetBundleName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetBundleName.html) | Get or set the AssetBundle name.  
[assetBundleVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetBundleVariant.html) | Get or set the AssetBundle variant.  
[assetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-assetPath.html) | The path name of the asset for this importer. (Read Only)  
[importSettingsMissing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-importSettingsMissing.html) | The value is true when no meta file is provided with the imported asset.  
[userData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter-userData.html) | Get or set any user data.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[AddRemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.AddRemap.html) | Map a sub-asset from an imported asset (such as an FBX file) to an external Asset of the same type.  
[GetExternalObjectMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetExternalObjectMap.html) | Gets a copy of the external object map used by the AssetImporter.  
[RemoveRemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.RemoveRemap.html) | Removes an item from the map of external objects.  
[SaveAndReimport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SaveAndReimport.html) | Save asset importer settings if asset importer is dirty.  
[SetAssetBundleNameAndVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.SetAssetBundleNameAndVariant.html) | Set the AssetBundle name and variant.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[GetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html) | Retrieves the asset importer for the asset at path.  
[GetImportLog](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetImportLog.html) | Retrieves logs generated during the import of the asset at path.  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
