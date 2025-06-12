* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LazyLoadReference_1.html

# LazyLoadReference<T0>
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Serializable lazy reference to a UnityEngine.Object contained in an asset file.
Allows an asset to reference another asset but delays loading the referenced asset until it is used, instead of loading it when the referencing object is deserialized.  
  
**Typical use cases** :  
- For importer settings that need to reference assets but reading the settings from disk cannot load the referenced assets because they may not be imported and are not yet accessible.  
- For reducing the time it takes to open a scene by loading only the assets needed for the initial set up, or display, in Edit Mode.  
  
**Notes:**
  * A lazy reference has a slight performance overhead compared to a direct reference.
  * In a standalone player, all assets are loaded when the player is loaded, or when asset bundles are loaded.


```
using UnityEditor.AssetImporters;
using UnityEngine;  
  
[ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)(1, "foo")]
public class FooImporter : ScriptedImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html)
{
    public LazyLoadReference<Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)> m_DefaultMaterial;  
  
    public override void OnImportAsset(AssetImportContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) ctx)
    {
        // At this point, 'm_DefaultMaterial' may refer to a material that has yet to be loaded into memory  
  
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat;
        if (!m_DefaultMaterial.isSet) // 'isSet' Does not load the referenced material even if not in memory.
        {
            mat = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Transparent/Diffuse"));
            ctx.AddObjectToAsset("mat", mat);
        }
        else
        {
            mat = m_DefaultMaterial.asset; // Will load referenced material if it is not already in memory.
        }  
  
        var obj = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        obj.transform.GetComponent<MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)>().material = mat;  
  
        ctx.AddObjectToAsset("main", obj);
        ctx.SetMainObject(obj);
    }
}

```

### Properties
Property | Description  
---|---  
[asset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LazyLoadReference_1-asset.html) | Accessor to the referenced asset.  
[instanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LazyLoadReference_1-instanceID.html) | Returns the instance id to the referenced asset.  
[isBroken](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LazyLoadReference_1-isBroken.html) | Convenience property that checks whether the reference is broken: refers to an object that is either not available or not loadable.  
[isSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LazyLoadReference_1-isSet.html) | Determines if an asset is being targeted, regardless of whether the asset is available for loading.  
### Constructors
Constructor | Description  
---|---  
[LazyLoadReference_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LazyLoadReference_1-ctor.html) | Construct a new LazyLoadReference.  
### Operators
Operator | Description  
---|---  
[LazyLoadReference<T>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LazyLoadReference_1-operator_T.html) | Implicit conversion from asset reference to LazyLoadReference.  
[LazyLoadReference<T>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LazyLoadReference_1-operator_int.html) | Implicit conversion from instance ID to LazyLoadReference.  
* * *
