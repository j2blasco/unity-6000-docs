* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-Moving.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating indirect light with Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-landing.html)
  * Move Light Probes at runtime


[](https://docs.unity3d.com/6000.0/Documentation/Manual/light-probes-and-scene-loading.html)
Load Light Probes in multiple scenes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/light-probes-troubleshooting.html)
Troubleshooting Light Probes
# Move Light Probes at runtime
You might need to move **Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) at runtime. For example, if you create a world by [loading multiple scenes additively](https://docs.unity3d.com/6000.0/Documentation/Manual/setupmultiplescenes.html) and then move each **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) to a different position, you need to move the Light Probes with their related scene objects.
You can use the [LightProbes API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html) to move Light Probes at runtime. You can’t move Light Probes by updating the **Transform component** A Transform component determines the Position, Rotation, and Scale of each object in the scene. Every GameObject has a Transform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TransformComponent) of the **Light Probe Group** A component that enables you to add Light Probes to GameObjects in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbeGroup) object, because the Transform only affects baking.
When you move Light Probes using the API, only the positions change. The baked data stored in the Light Probes stays the same.
Follow these steps:
  1. Clone the Light Probes data that a loaded scene uses, using the [LightProbes.GetInstantiatedLightProbesForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetInstantiatedLightProbesForScene.html) API. The loaded scene (the `Scene` object) will use this cloned data from now on.
  2. Set new positions using the [GetPositionsSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetPositionsSelf.html) and [SetPositionsSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.SetPositionsSelf.html) APIs.
  3. Update the internal structure of the Light Probe data in the scene using the [LightProbes.Tetrahedralize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.Tetrahedralize.html) or [LightProbes.TetrahedralizeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.TetrahedralizeAsync.html) API, so objects use the correct light data.


If you baked the scene together with other scenes that contain Light Probes, the returned data contains Light Probes from all the baked scenes. Refer to [Light Probes and Scene loading](https://docs.unity3d.com/6000.0/Documentation/Manual/light-probes-and-scene-loading.html) for more information about using Light Probes in multiple scenes.
The `Tetrahedralize` APIs can take a long time. If you move multiple Light Probes, it’s best to tetrahedralize once at the end.
You can use the [LightProbes.GetSharedLightProbesForScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetSharedLightProbesForScene.html) API instead if you need to read the positions of the Light Probes in a scene, but not move them.
## Example
The following code moves the Light Probes in the current scene to a new position each frame.
Attach the script to any object in a scene. When you run the project, select any object that uses Light Probes so you can see the probes move. The Light Probe Group object doesn’t move.
```
using UnityEngine;
using UnityEngine.SceneManagement;

public class LoadSingleSceneAndMoveProbes : MonoBehaviour
{
    void Update()
    {
        // Get a copy of the Light Probes in the current scene
        LightProbes lightProbes = LightProbes.GetInstantiatedLightProbesForScene(SceneManager.GetActiveScene());

        // Get the Light Probe positions
        Vector3[] positions = lightProbes.GetPositionsSelf();

        // Update the positions
        for (int i = 0; i < positions.Length; i++)
        {
            positions[i].x = positions[i].x + 0.01f;
        }

        // Copy the new positions back to the Light Probes
        lightProbes.SetPositionsSelf(positions, true);

        // Tetrahedralize to update the data in the LightProbes object of the scene.
        LightProbes.Tetrahedralize();
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/light-probes-and-scene-loading.html)
Load Light Probes in multiple scenes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/light-probes-troubleshooting.html)
Troubleshooting Light Probes
