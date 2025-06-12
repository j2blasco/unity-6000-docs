* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/volume-component-reference.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-in-urp.html)
  * [Volumes in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/volumes-landing-page.html)
  * Volume component reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/VolumeOverrides.html)
Configure Volume Overrides in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/EffectList.html)
Post-processing Volume Overrides reference for URP
# Volume component reference for URP
Volumes components contain properties that control how they affect **Cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) and how they interact with other Volumes.
Property | Description  
---|---  
**Mode** | Use the drop-down to select the method that URP uses to calculate whether this Volume can affect a Camera:  
• **Global** : Makes the Volume have no boundaries and allow it to affect every Camera in the scene.  
• **Local** : Allows you to specify boundaries for the Volume so that the Volume only affects Cameras inside the boundaries. Add a Collider to the Volume’s GameObject and use that to set the boundaries.  
**Blend Distance** | The furthest distance from the Volume’s Collider that URP starts blending from. A value of 0 means URP applies this Volume’s overrides immediately upon entry.  
This property only appears when you select **Local** from the **Mode** drop-down.  
**Weight** | The amount of influence the Volume has on the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). URP applies this multiplier to the value it calculates using the Camera position and Blend Distance.  
**Priority** | URP uses this value to determine which Volume it uses if more than one Volume overrides the same property. URP uses the Volume with the highest value.  
**Volume Profile** | A Volume Profile Asset that contains the Volume Components that store the properties URP uses to handle this Volume. The **Profile** field stores a [Volume Profile](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volume-Profile.html), which is an Asset that contains the properties that URP uses to render the scene. You can edit this Volume Profile, or assign a different Volume Profile to the **Profile** field. You can also create a Volume Profile by selecting the **New** button.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/VolumeOverrides.html)
Configure Volume Overrides in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/EffectList.html)
Post-processing Volume Overrides reference for URP
