* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Lens flares](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lens-flares.html)
  * [Lens flares in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare.html)
  * Lens Flare (SRP) Data Asset in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)
Lens Flare (SRP) component reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/reference-screen-space-lens-flare.html)
Screen Space Lens Flare override reference for URP
# Lens Flare (SRP) Data Asset in URP
Unity’s [Scriptable Render Pipeline (SRP)](https://docs.unity3d.com/Manual/ScriptableRenderPipeline.html) includes the **Lens Flare Data** asset. You can use this asset to control the appearance of [Lens Flares](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-component.html)A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare) in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). This is the SRP equivalent of the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline)’s [Flare](https://docs.unity3d.com/Manual/class-Flare.html) asset, which is incompatible with SRPs.
For examples of how to use Lens Flares, refer to the [Lens Flare samples in URP Package Samples](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-sample-urp-package-samples.html#lens-flares).
To create a Lens Flare Data asset, select **Assets** > **Create** > **Lens Flare (SRP)**. To use this asset, assign it to the **Lens Flare Data** property of a [Lens Flare (SRP) component](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-component.html).
## Properties
The Lens Flare Element asset has the following properties:
  * [Type](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Type)
  * [Image](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Image)
  * [Circle](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Circle)
  * [Polygon](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Polygon)
  * [Ring](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Ring)
  * [Lens Flare Data SRP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#LensFlareDataSRP)
  * [Common](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Common)
  * [Cutoff](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Cutoff)
  * [Transform](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Transform)
  * [AxisTransform](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#AxisTransform)
  * [Distortion](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Distortion)
  * [Multiple Elements](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Multiple-Elements)
    * [Uniform](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#uniform)
    * [Curve](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Curve)
    * [Random](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Random)


### Type
**Property** | **Description**  
---|---  
**Type** | Select the type of Lens Flare Element this asset creates:
  * [Image](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Image)
  * [Circle](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Circle)
  * [Polygon](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Polygon)

  
#### Image
**Property** | **Description**  
---|---  
**Flare Texture** | The Texture this lens flare element uses.  
**Preserve**Aspect Ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AspectRatio)** | Fixes the width and height (aspect ratio) of the **Flare Texture**. You can use [Distortion](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Distortion) to change this property.  
#### Circle
**Property** | **Description**  
---|---  
**Gradient** | Controls the offset of the circular flare’s gradient. This value ranges from 0 to 1.  
**Falloff** | Controls the falloff of the circular flare’s gradient. This value ranges from 0 to 1, where 0 has no falloff between the tones and 1 creates a falloff that is spread evenly across the circle.  
**Inverse** | Enable this property to reverse the direction of the gradient.  
#### Polygon
**Property** | **Description**  
---|---  
**Gradient** | Controls the offset of the polygon flare’s gradient. This value ranges from 0 to 1.  
**Falloff** | Controls the falloff of the polygon flare’s gradient. This value ranges from 0 to 1, where 0 has no falloff between the tones and 1 creates a falloff that is spread evenly across the polygon.  
**Side Count** | Determines how many sides the polygon flare has.  
**Roundness** | Defines how smooth the edges of the polygon flare are. This value ranges from 0 to 1, where 0 is a sharp polygon and 1 is a circle.  
**Inverse** | Enable this property to reverse the direction of the gradient  
#### Ring
**Property** | **Description**  
---|---  
**Gradient** | Controls the offset of the circular flare’s gradient. This value ranges from 0 to 1.  
**Falloff** | Controls the falloff of the circular flare’s gradient. This value ranges from 0 to 1, where 0 has no falloff between the tones and 1 creates a falloff that is spread evenly across the circle.  
**Inverse** | Enable this property to reverse the direction of the gradient.  
**Amplitude** | Amplitude of the sampling of the noise.  
**Repeat** | Frequency of the sampling for the noise.  
**Speed** | Scale the speed of the animation.  
**Ring Thickness** | Ring Thickness.  
#### Lens Flare Data Driven SRP
**Property** | **Description**  
---|---  
**Asset** | Lens Flare Data SRP asset as an element.  
Unity support an Lens Flare Data SRP recursive, but with a hard cutoff after 16 recursions call. For instance asset A constains asset B which constains asset A (infinite recursion). That will trigger a warning and execution 16 recursions: ~~~~~~ “LensFlareSRPAsset contains too deep recursive asset (> 16). Be careful to not have recursive aggregation, A contains B, B contains A, … which will produce an infinite loop.” ~~~~~~
## Color
**Property** | **Description**  
---|---  
**Color Type** | Select the color type of Lens Flare Element this asset creates:
  * [Constant](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#ColorConstant)
  * [Radial](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#ColorRadial)
  * [Angular](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#ColorAngular)

  
**Tint** | Changes the tint of the lens flare. If this asset is attached to the light, this property is based on the light tint.  
**Modulate By Light Color** | Allows light color to affect this Lens Flare Element. This only applies when the asset is used in a [SRP Lens Flare Override Component](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-component.html) that is attached to a point, spot, or area light.  
**Intensity** | Controls the intensity of this element.  
**Blend Mode** | Select the blend mode of the Lens Flare Element this asset creates:
  * Additive
  * Screen
  * Premultiplied
  * Lerp

  
### Constant Color
**Property** | **Description**  
---|---  
**Tint** | Changes the tint of the lens flare. If this asset is attached to the light, this property is based on the light tint.  
### Constant Color
**Property** | **Description**  
---|---  
**Tint Radial** | Specifies the radial gradient tint of the element. If the element type is set to Image, the Flare Texture is multiplied by this color.  
### Constant Color
**Property** | **Description**  
---|---  
**Tint Angular** | Specifies the angular gradient tint of the element. If the element type is set to Image, the Flare Texture is multiplied by this color.  
## Common
### Cutoff
**Property** | **Description**  
---|---  
**Cutoff Speed** | Sets the speed at which the radius occludes the element.  
  
A value of zero (with a large radius) does not occlude anything. The higher this value, the faster the element is occluded on the side of the screen.  
  
The effect of this value is more noticeable with multiple elements.  
**Cutoff Radius** | Sets the normalized radius of the lens shape used to occlude the lens flare element. A radius of one is equivalent to the scale of the element.  
### Transform
**Property** | **Description**  
---|---  
**Position Offset** | Defines the offset of the lens flare’s position in screen space, relative to its source.  
**Auto Rotate** | Enable this property to automatically rotate the Lens Flare Texture relative to its angle on the screen. Unity uses the **Auto Rotate** angle to override the **Rotation** parameter.  
  
To ensure the Lens Flare can rotate, assign a value greater than 0 to the [**Starting Position**](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#AxisTransform) property.  
**Rotation** | Rotates the lens flare. This value operates in degrees of rotation.  
**Size** | Use this to adjust the scale of this lens flare element.  
  
This property is not available when the [Type](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Type) is set to [Image](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Image) and **Preserve Aspect Ratio** is enabled.  
**Scale** | The size of this lens flare element in world space.  
### Axis Transform
**Property** | **Description**  
---|---  
**Starting Position** | Defines the starting position of the lens flare relative to its source. This value operates in screen space.  
**Angular Offset** | Controls the angular offset of the lens flare, relative to its current position. This value operates in degrees of rotation.  
**Translation Scale** | Limits the size of the lens flare offset. For example, values of (1, 0) create a horizontal lens flare, and (0, 1) create a vertical lens flare.  
  
You can also use this property to control how quickly the lens flare appears to move. For example, values of (0.5, 0.5) make the lens flare element appear to move at half the speed.  
### Distortion
**Property** | **Description**  
---|---  
**Enable** | Set this property to True to enable distortion.  
**Radial Edge Size** | Controls the size of the **distortion effect** An audio effect that modifies the sound by squashing and clipping the waveform to produce a rough, harsh result. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioDistortionFilter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DistortionEffect) from the edge of the screen.  
**Radial Edge Curve** | Blends the distortion effect along a curve from the center of the screen to the edges of the screen.  
**Relative To Center** | Set this value to True to make distortion relative to the center of the screen. Otherwise, distortion is relative to the screen position of the lens flare.  
### Multiple Elements
**Property** | **Description**  
---|---  
**Enable** | Enable this to allow multiple lens flare elements in your scene.  
**Count** | Determines the number of identical lens flare elements Unity generates.  
A value of **1** appears the same as a single lens flare element.  
**Distribution** | Select the method that Unity uses to generate multiple lens flare elements:
  * [Uniform](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#uniform)
  * [Curve](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Curve)
  * [Random](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-asset.html#Random)

  
**Length Spread** | Controls how spread out multiple lens flare elements appear.  
**Relative To Center** | If true the distortion is relative to center of the screen otherwise relative to lensFlare source screen position.  
#### Uniform
**Property** | **Description**  
---|---  
**Colors** | The range of colors that this asset applies to the lens flares.  
**Rotation** | The angle of rotation (in degrees) applied to each element incrementally.  
#### Curve
**Property** | **Description**  
---|---  
**Colors** | The range of colors that this asset applies to the lens flares. You can use the **Position Spacing** curve to determine how this range affects each lens flare.  
**Position Variation** | Adjust this curve to change the placement of the lens flare elements in the **Lens Spread**.  
**Rotation** | The uniform angle of rotation (in degrees) applied to each element distributed along the curve. This value ranges from –180° to 180°.  
**Scale** | Adjust this curve to control the size range of the lens flare elements.  
#### Random
**Property** | **Description**  
---|---  
**Seed** | The base value that this asset uses to generate randomness.  
**Intensity Variation** | Controls the variation of brightness across the lens flare elements. A high value can make some elements might invisible.  
**Colors** | The range of colors that this asset applies to the lens flares. This property is based on the **Seed** value.  
**Position Variation** | Controls the position of the lens flares. The **X** value is spread along the same axis as **Length Spread**. A value of 0 means there is no change in the lens flare position. The **Y** value is spread along the vertical screen space axis based on the **Seed** value.  
**Rotation Variation** | Controls the rotation variation of the lens flares, based on the **Seed** value. The **Rotation** and **Auto Rotate** parameters inherit from this property.  
**Scale Variation** | Controls the scale of the lens flares based on the **Seed** value.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)
Lens Flare (SRP) component reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/reference-screen-space-lens-flare.html)
Screen Space Lens Flare override reference for URP
