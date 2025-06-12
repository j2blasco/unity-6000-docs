* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/LightBlendStyles.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-urp-landing.html)
  * [2D lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-index.html)
  * Light Blend Styles component reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DRendererData-overview.html)
2D Renderer asset component reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect.html)
Precise pixel scaling and rotation via the Pixel Perfect Camera in URP
# Light Blend Styles component reference for URP
Find the **Light Blend Styles** settings in the [2D Renderer Data asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DRendererData-overview.html) to customize the way that the light interacts with **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). 
The asset can contain a total of four different **Light Blend Styles** , each with a different combination of Blend Style settings by default. All lights in the scene must pick from one of these available **Light Blend Styles**. When you create a light, it’s automatically assigned the first Blend Style listed in the asset.
![](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/image_38.png) **Property** | **Description**  
---|---  
**Name** | The name that appears when choosing a Blend Style for a Light 2D.  
**Mask Texture Channel** | Select the channel(s) that the mask texture affects in this **Blend Style**. These channels comprise the red green blue alpha (RGBA) color model.  
| **R** | The red color channel.  
| **G** | The green color channel.  
| **B** | The blue color channel.  
| **A** | The alpha channel.  
**Blend Mode** | A **Blend Mode** controls the way a sprite is lit by light. Select how a Light 2D is blended when using this Blend Style. Refer to [these examples](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-blending.html) of the different **Blend Modes**.  
| **Additive** | Select to set the **Blend Mode** to Additive.  
| **Multiply** | Select to set the **Blend Mode** to Multiply.  
| **Subtractive** | Select to set the **Blend Mode** to Subtractive.  
## Additional resources
  * [Types of 2D lights](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/LightTypes.html)
  * [Light 2D component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DLightProperties.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DRendererData-overview.html)
2D Renderer asset component reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect.html)
Precise pixel scaling and rotation via the Pixel Perfect Camera in URP
