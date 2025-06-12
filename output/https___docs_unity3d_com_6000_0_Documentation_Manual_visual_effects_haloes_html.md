* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-haloes.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * Light halos


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)
Lens Flare component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-configure-halo.html)
Create and configure a halo light effect
# Light halos
Strategies for creating glowing halos around light sources, to give the impression of small dust particles in the air, and add atmosphere to your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). 
![A Light with a separate Halo Component](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/HaloWindow.jpg) A Light with a separate Halo **Component** **Topic** | **Description**  
---|---  
[Create and configure a halo light effect](https://docs.unity3d.com/6000.0/Documentation/Manual/create-configure-halo.html) | Create and customize a halo around a light source.  
[Halo component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Halo.html) | Explore the properties for the Halo component to customize the appearance of a halo.  
## Render pipeline information
How you work with light halos depends on the **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) you use.
**Feature name** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Built-in Render Pipeline**  
---|---|---|---  
**Halos** | Yes  
  
Use a [Lens Flare (SRP) Data Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html) and a [Lens Flare (SRP) component](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-component.html). | Yes  
  
Use a [Lens Flare (SRP) Data Asset](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/shared/lens-flare/lens-flare-asset.html) and a [Lens Flare (SRP) component](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/shared/lens-flare/lens-flare-component.html), or a [Screen Space Lens Flare override](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/shared/lens-flare/Override-Screen-Space-Lens-Flare.html). | Yes  
  
Use a [Halo component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Halo.html).  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)
Lens Flare component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-configure-halo.html)
Create and configure a halo light effect
