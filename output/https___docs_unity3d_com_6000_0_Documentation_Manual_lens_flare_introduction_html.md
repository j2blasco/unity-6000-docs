* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/lens-flare-introduction.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Lens flares](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lens-flares.html)
  * Introduction to lens flare effects


[](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lens-flares.html)
Lens flares
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare.html)
Lens flares in URP
# Introduction to lens flare effects
Understand how Unity manages **lens flares** A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare), which simulate the effect of lights refracting inside a **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) lens. Use them to represent bright lights or to add a bit more atmosphere to your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
## Flares
A Flare asset allows you to create and configure the appearance of lens flares. 
Flares work by containing several Flare **Elements** on a single **Texture** An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture). Within the Flare, you pick and choose which **Elements** you want to include from any of the Textures.
## Displaying flares
A Lens Flare component displays a lens flare that is configured by a [Flare asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Flare.html).
You can display a Flare asset with a [Light component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html). If you do this, Unity automatically tracks the position and direction of the Light and uses those values to configure the appearance of the lens flare.
Use this component instead to configure the values of the lens flare yourself, which gives you more precise control.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lens-flares.html)
Lens flares
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare.html)
Lens flares in URP
