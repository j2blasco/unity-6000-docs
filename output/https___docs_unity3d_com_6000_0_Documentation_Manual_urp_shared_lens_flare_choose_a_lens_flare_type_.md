* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/choose-a-lens-flare-type.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Lens flares](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lens-flares.html)
  * [Lens flares in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare.html)
  * Choose a lens flare type in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare.html)
Lens flares in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-component.html)
Add lens flares in URP
# Choose a lens flare type in URP
You can add the following types of lens flares:
  * [Lens flares](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-component.html)A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare) - use a **Lens Flare (SRP)** component to create lens flares for lights that have specific locations in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), for example the sun or bright bulbs.
  * [Screen space lens flares](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html) - use a **Screen Space Lens Flare** override to create lens flares for emissive surfaces, bright spots, and onscreen lights.


You can use both types in the same scene.
Use the following table to help you choose a lens flare type:
Feature | Lens Flare (SRP) component | Screen Space Lens Flare override  
---|---|---  
Typical uses | Lens flares from the sun and specific lights, custom flare shapes, and cinematics | Lens flares on vehicles and water, first-person games, and science-fiction environments  
Supported platforms | All platforms | All platforms  
CPU and GPU use | CPU and GPU | GPU  
Types of light | All Light objects, except Area Lights | All bright spots and visible lights  
Placement | Attach to individual lights. Place lens flares manually | Generate inside a volume. Place all lens flares automatically with a single setting  
Lens flares from offscreen lights | Yes | No  
Light streaks | No, unless you create them manually | Yes  
Configure flares | Configure per lens flare or per element | Configure for all lens flares together  
Configure flare elements | Configure many settings for each element, per lens flare | Configure several settings for elements, for all lens flares together  
Configure attenuation | Yes | No  
Affected by the environment | Yes | Yes  
Preserve **aspect ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AspectRatio) | Yes | No  
Chromatic aberration | No | Yes  
Blend modes | Additive, Lerp, Premultiplied and Screen | Additive only  
Occlusion | Screen space occlusion, and geometric occlusion for offscreen lights. Configurable. Occlusion might not always work at the edge of the screen. | Screen space occlusion, generated from the color buffer. Not configurable  
Examples in [package samples](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-samples.html) | Yes | No  
## Additional resources
  * [Lens Flare (SRP) reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)
  * [Lens Flare (SRP) Data Asset reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html)
  * [Screen Space Lens Flare override reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare.html)
Lens flares in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-component.html)
Add lens flares in URP
