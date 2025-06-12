* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/reference-screen-space-lens-flare.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Lens flares](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lens-flares.html)
  * [Lens flares in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare.html)
  * Screen Space Lens Flare override reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html)
Lens Flare (SRP) Data Asset in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lens-flare-birp.html)
Lens flares in the Built-In Render Pipeline
# Screen Space Lens Flare override reference for URP
Refer to [Add screen space lens flares](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html) for more information.
## Properties
**Property** | **Description**  
---|---  
**Intensity** | Set the strength of all the types of **lens flares** A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare). If the value is 0, URP doesn’t calculate or render any lens flares. The default is 0.  
**Tint Color** | Set the color URP uses to tint all the types of lens flares. The default is white.  
**Bloom Mip Bias** | Set the mipmap level URP uses to sample the Bloom pyramid and create the lens flares. The higher the mipmap level, the smaller and more pixelated the sample source, and the blurrier the result. The range is 0 through 5. 0 is the full-resolution mipmap level. The default is 1. Refer to [Mipmaps introduction](https://docs.unity3d.com/2023.1/Documentation/Manual/texture-mipmaps-introduction.html) for more information. This property only appears if you open the **More** (⋮) menu and select **Advanced Properties**.  
### Flares
Use the **Flares** settings to control regular flares, reversed flares and warped flares.
**Property** | **Description**  
---|---  
**Regular Multiplier** | Set the strength of regular flares. If the value is 0, URP doesn’t calculate or render regular flares. The default is 1.  
**Reversed Multiplier** | Set the strength of reversed flares. If the value is 0, URP doesn’t calculate or render reversed flares. The default is 1.  
**Warped Multipler** | Set the strength of warped flares. If the value is 0, URP doesn’t calculate or render warped flares. The default is 1.  
**Scale** | Scale the width (**x**) and height (**y**) of warped flares. The defaults are 1. This property only appears if you open the **More** (⋮) menu and select **Advanced Properties**.  
**Samples** | Set the number of times URP repeats the regular, reversed and warped flares. The range is 1 through 3. The default is 1. Increasing **Samples** has a big impact on performance.  
**Sample Dimmer** | Set the strength of the lens flares URP adds if you set **Samples** to 2 or 3. The higher the value, the less intense the flares. This property only appears if you open the **More** (⋮) menu and select **Advanced Properties**.  
**Vignette Effect** | Set the strength of the regular, reversed and warped flares in a circular area in the center of the screen. Use **Vignette Effect** to avoid lens flare obscuring the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) too much. The default value is 1, which means URP doesn’t render flares at the center of the screen.  
**Starting Position** | Control how far the position of the regular, reversed and warped flares differ from the bright area they’re sampled from, in metres. If the value is 0, URP places the lens flares at the same position as the bright areas they’re sampled from. The range is 1 through 3. The default is 1.25.  
**Scale** | Set the size of regular, reversed and warped lens flares. The range is 1 through 4. The default is 1.5.  
### Streaks
Use the **Streaks** settings to control flares stretched in one direction.
**Property** | **Description**  
---|---  
**Multiplier** | Set the strength of streaks. If the value is 0, URP doesn’t calculate or render streaks. The default is 1.  
**Length** | Set the length of streaks. The range is 0 through 1. 1 is the approximate width of the screen. The default value is 0.5.  
**Orientation** | Set the angle of streaks, in degrees. The default value is 0, which creates horizontal streaks.  
**Threshold** | Control how localized the streak effect is. The higher the **Threshold** , the more localized the effect. The range is 0 through 1. The default value is 0.25.  
**Resolution** | Control the resolution detail of streaks. URP renders lower-resolution streaks faster. The options are **Half** , **Quarter** and **Eighth** full resolution. This property only appears if you open the **More** (⋮) menu and select **Advanced Properties**.  
![The effect of changing Threshold from 0 \(a larger flare effect\) to 1 \(a smaller flare effect\).](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shared/lens-flare/screenspacelensflares-threshold.gif)  

### Chromatic Aberration
Use the **Chromatic Aberration** settings to control chromatic aberration on all the lens flare types. Chromatic aberration splits light into its color components, which mimics the effect that a real-world **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) produces when its lens fails to join all colors to the same point.
The chromatic aberration effect is strongest at the edges of the screen, and decreases in strength towards the center of the screen.
**Property** | **Description**  
---|---  
**Intensity** | Set the strength of the chromatic aberration effect. If the value is 0, URP doesn’t split the colors.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html)
Lens Flare (SRP) Data Asset in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lens-flare-birp.html)
Lens flares in the Built-In Render Pipeline
