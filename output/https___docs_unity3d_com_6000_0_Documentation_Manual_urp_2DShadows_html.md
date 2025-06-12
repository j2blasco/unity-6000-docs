* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DShadows.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-urp-landing.html)
  * [2D lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-index.html)
  * Create shadows with Shadow Caster 2D in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/HDREmulationScale.html)
HDR emulation scale
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/ShaderGraph.html)
Create a 2D sprite lit Shader Graph in URP
# Create shadows with Shadow Caster 2D in URP
Learn how the **Shadow Caster 2D** component defines the shape and properties that a Light uses to determine its cast shadows. 
Add the **Shadow Caster 2D** component to a GameObject by going to menu: **Component > Rendering > 2D > Shadow Caster 2D**.
**Property** | **Function**  
---|---  
**Use Renderer Silhouette** | Enable this and **Self Shadows** to include the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) Renderer’s silhouette as part of the shadow. Enable this and disable Self Shadows to exclude the Renderer’s silhouette from the shadow. This option is only available when a valid Renderer is present.  
**Casts Shadows** | Enable this to have the Renderer cast shadows.  
**Self Shadows** | Enable this to have the Renderer cast shadows on itself.  
![Left: Use Renderer Silhouette disabled, Self Shadow disabled. Right: Use Renderer Silhouette enabled, Self Shadow disabled.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/RendSilhou_SS_false-disabled-enabled.png) Left: **Use Renderer Silhouette** disabled, **Self Shadow** disabled. Right: **Use Renderer Silhouette** enabled, **Self Shadow** disabled. ![Left: Use Renderer Silhouette disabled, Self Shadows enabled. Right: Use Renderer Silhouette enabled, Self Shadows enabled.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/RendSilhou_SS_true-disabled-enabled.png) Left: **Use Renderer Silhouette** disabled, **Self Shadows** enabled. Right: **Use Renderer Silhouette** enabled, **Self Shadows** enabled.
## Composite Shadow Caster 2D
The **Composite Shadow Caster 2D** merges the shape of multiple **Shadow Caster 2Ds** together as a single **Shadow Caster 2D**. Add the **Composite Shadow Caster 2D** component to a GameObject by going to menu: **Component > Rendering > 2D > Composite Shadow Caster 2D**, then parent GameObjects with the **Shadow Caster 2D** component to it. The Composite component merges all Shadow Caster 2Ds within this hierarchy, including any Shadow Caster 2Ds on the parent as well.
![Left: Without Composite Shadow Caster 2D. Right: With Composite Shadow Caster 2D](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/composite_shadow-without-with.png) Left: Without **Composite Shadow Caster 2D**. Right: With **Composite Shadow Caster 2D**
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/HDREmulationScale.html)
HDR emulation scale
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/ShaderGraph.html)
Create a 2D sprite lit Shader Graph in URP
