* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-inspector-reference.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes.html)
  * Adaptive Probe Volume Inspector reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-troubleshoot-light-leaks.html)
Troubleshooting light leaks in Adaptive Probe Volumes in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-lighting-panel-reference.html)
Adaptive Probe Volumes panel reference
# Adaptive Probe Volume Inspector reference
Select an Adaptive Probe Volume and open the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) to view its properties.
## Mode
**Option** | **Description**  
---|---  
**Mode** | Sets the size of the Adaptive Probe Volume. The options are: 
  * **Global** : URP sizes this Adaptive Probe Volume to include all renderers in the scene or Baking Set that have **Contribute Global Illumination** enabled in their [Mesh Renderer component](https://docs.unity3d.com/Manual/class-MeshRenderer.html). URP recalculates the volume size every time you save or generate lighting.
  * **Scene** : URP sizes this Adaptive Probe Volume to include all renderers in the same scene as this Adaptive Probe Volume. URP recalculates the volume size every time you save or generate lighting.
  * **Local** : Set the size of this Adaptive Probe Volume manually.

  
**Size** | Set the size of this Adaptive Probe Volume. This setting only appears when you set **Mode** to **Local**.  
## Subdivision Override
**Property** | **Description**  
---|---  
**Override Probe Spacing** | Override the Probe Spacing set in the **Baking Set** for this Adaptive Probe Volume. This cannot exceed the **Min Probe Spacing** and **Max Probe Spacing** values in the [Adaptive Probe Volumes panel in the Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-lighting-panel-reference.html).  
## Geometry Settings
**Property** | **Description**  
---|---  
**Override Renderer Filters** | Enable filtering by Layer which **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) URP considers when it generates probe positions. Use this to exclude certain GameObjects from contributing to Adaptive Probe Volume lighting.  
****Layer Mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LayerMask)** | Filter by Layer which GameObjects URP considers when it generates probe positions.  
**Min Renderer Size** | The smallest [Renderer](https://docs.unity3d.com/ScriptReference/Renderer.html) size URP considers when it generates probe positions.  
**Fill Empty Spaces** | Enable URP filling the empty space between and around Renderers with bricks. Bricks in empty spaces always use the **Max Probe Spacing** value.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-troubleshoot-light-leaks.html)
Troubleshooting light leaks in Adaptive Probe Volumes in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-lighting-panel-reference.html)
Adaptive Probe Volumes panel reference
