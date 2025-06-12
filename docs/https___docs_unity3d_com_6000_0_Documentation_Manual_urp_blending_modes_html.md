* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/blending-modes.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
  * [Shader Material Inspector window reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp-reference.html)
  * Blending Modes in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp-reference.html)
Shader Material Inspector window reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lit-shader.html)
Lit Shader Material Inspector window reference for URP
# Blending Modes in URP
In a material in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP), the **Blending Mode** property determines how Unity calculates the color of each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) of a transparent Material when it blends the Material with the background.
In the context of Blending Modes, Source refers to the transparent Material where the Blending Mode is set and Destination refers to anything that Material overlaps with. 
## Alpha
![Alpha blending mode example](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/blend-modes/blend-mode-alpha.png)  
_Alpha blending mode._
**Alpha** uses the Material’s alpha value to change how transparent an object is. 0 is fully transparent. 255 is fully opaque, this is translated to a value of 1 when used with the blending equations. The Material is always rendered in the Transparent render pass regardless of its alpha value. This mode lets you use the Preserve Specular Lighting property.
Alpha equation:
OutputRGB = (SourceRGB * SourceAlpha) + DestinationRGB * (1 - SourceAlpha)
## Premultiply
![Premultiply blending mode example](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/blend-modes/blend-mode-premultiply.png)  
_Premultiply blending mode._
**Premultiply** first multiplies the RGB values of the transparent Material by its alpha value then applies a similar effect to the Material as Alpha. The equation for Premultiply also allows areas of the transparent Material with an alpha value of 0 to have an additive blend effect. This can help reduce artifacts that may appear at the edge of the overlap between opaque and transparent pixels.
Premultiply equation:
OutputRGB = SourceRGB + DestinationRGB * (1 - SourceAlpha)
## Additive
![Additive blending mode example](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/blend-modes/blend-mode-additive.png)  
_Additive blending mode._
**Additive** adds the color values of the Materials together to create the blend effect. The alpha value determines the strength of the source Material’s color before the blend is calculated. This mode lets you use the Preserve Specular Lighting property.
Additive equation:
OutputRGB = (SourceRGB * SourceAlpha) + DestinationRGB
## Multiply
![Multiply blending mode example](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/blend-modes/blend-mode-multiply.png)  
_Multiply blending mode._
**Multiply** multiplies the color of the Material with the color behind the surface. This creates a darker effect, like when you look through colored glass. This mode uses the Material’s alpha value to adjust how much the colors blend. An alpha value of 1 results in unadjusted multiplication of the colors while lower values blend the colors towards white.
Multiply equation:
OutputRGB = SourceRGB * DestinationRGB
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp-reference.html)
Shader Material Inspector window reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lit-shader.html)
Lit Shader Material Inspector window reference for URP
