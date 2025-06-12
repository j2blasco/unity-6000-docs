* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ModifyingSourceAssetsThroughScripting.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Scripting with assets](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptingAssets.html)
  * Modify source assets from code


[](https://docs.unity3d.com/6000.0/Documentation/Manual/StreamingAssets.html)
Stream assets directly into a build
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)
Distribute assets as packages
# Modify source assets from code
You can modify assets from your runtime code. Depending on the asset type and method you use, the modifications can either be temporary or permanent. Temporary modifications reset on exiting Play mode, and permanent modifications persist on exiting Play mode.
## Temporary modification
Modifications to assets at application runtime are usually temporary. For example, you might want to modify the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) component of the material for a character to represent a temporary invincibility power-up. The shader modification in this case is not permanent and does not persist on exiting Play mode.
The following example demonstrates this by changing the `shader` property of the `material` component:
```
using UnityEngine;

public class ExampleScript : MonoBehaviour
{
    private Shader invincibleShader;

    void Start()
    {
        invincibleShader = Shader.Find("Specular");
    }

    public void StartInvincibility()
    {
        if (TryGetComponent<Renderer>(out Renderer renderer))
        {
            renderer.material.shader = invincibleShader;
        }
    }
}

```

On exiting Play mode, the state of the [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material) resets to whatever it was before entering Play mode. Accessing `renderer.material` automatically instantiates the material and returns the instance. This instance is simultaneously and automatically applied to the renderer, so any changes you make aren’t permanent.
**Note:** If you declare a public variable that holds a reference to the material and modify that instead of modifying the `renderer.material.shader` class member directly, you won’t get the benefits of automatic instantiation before the modifications are applied.
## Permanent modification
**Important** : The method presented here modifies actual source asset files used within Unity. You can’t undo these modifications. Use them with caution.
To avoid the material resetting on exiting Play mode, you can use [Renderer.sharedMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-sharedMaterial.html). The `sharedMaterial` property returns the actual asset used by the renderer.
The following example permanently changes the material to use the Specular shader and does not reset the material to the state it was in before Play mode:
```
using UnityEngine;

public class ExampleScript : MonoBehaviour
{
    private Shader invincibleShader;

    void Start()
    {
        invincibleShader = Shader.Find("Specular");
    }

    public void StartInvincibility()
    {
        if (TryGetComponent<Renderer>(out Renderer renderer))
        {
            renderer.sharedMaterial.shader = invincibleShader;
        }
    }
}

```

## Applicable classes and properties
The previously described programming pattern of using local or shared properties for temporary or permanent changes respectively applies for the following asset types:
Asset type | Property for temporary changes | Property for permanent changes  
---|---|---  
Material | [`Renderer.material`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-material.html) | [`Renderer.sharedMaterial`](https://docs.unity3d.com/6000.0/Documentation/Manual/Renderer-sharedMaterial)  
**Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) | [`MeshFilter.mesh`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter-mesh.html) | [`MeshFilter.sharedMesh`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/meshFilter-sharedMesh.html)  
**Physics Materials** A physics asset for adjusting the friction and bouncing effects of colliding objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsMaterial.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsMaterial) | [`Collider.material`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-material.html) | [`Collider.sharedMaterial`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider-sharedMaterial.html)  
**Note** : If you declare a public variable of any of these classes and make modifications to the asset using that variable instead of using the relevant class member, you won’t get the benefits of automatic instantiation before the modifications are applied.
## Assets that are not automatically instantiated
The following asset types are not automatically instantiated when modified:
  * [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)
  * [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html)


Any modifications made to these assets from code are always permanent, and can’t be undone. If, for example, you change a **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain)’s **heightmap** A greyscale Texture that stores height data for an object. Each pixel stores the height difference perpendicular to the face that pixel represents.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Heightmap) or the **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) of a texture file from code, you’ll need to account for instantiating and assigning values manually.
## Additional resources
  * [Loading resources at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingResourcesatRuntime.html)
  * [Streaming assets directly into a build](https://docs.unity3d.com/6000.0/Documentation/Manual/StreamingAssets.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StreamingAssets.html)
Stream assets directly into a build
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)
Distribute assets as packages
