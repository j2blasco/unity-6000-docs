* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/create-light-2d.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-urp-landing.html)
  * [2D lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-index.html)
  * [Types of 2D lights](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/LightTypes.html)
  * Prepare your project for 2D lighting


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Lights-2D-intro.html)
Introduction to the 2D lighting system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DLightProperties.html)
Light 2D component reference for URP
# Prepare your project for 2D lighting
Follow the steps below to prepare your project for 2D lighting and 2D lighting effects.
The following is the general workflow to include 2D lighting in your project.
  1. Prepare your **Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) for lighting. For details, see [Prepare and upgrade sprites for 2D lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/PrepShader.html). 
  2. Set up **normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap) and mask Textures. 2D Lights can interact with normal map and mask Textures linked to Sprites to create advanced lighting effects, such as [normal mapping](https://en.wikipedia.org/wiki/Normal_mapping). See [Add normal map and mask textures to a sprite in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/SecondaryTextures.html). 
  3. Create a 2D Light **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject); see [Light 2D component reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DLightProperties.html). 
  4. Configure the 2D Renderer Data asset; see [Configuring the 2D Renderer Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DRendererData-overview.html). 
  5. To define the shape and properties that a Light uses to determine the shadows it casts, use the [Shadow Caster 2D component](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DShadows.html). 
  6. (Optional) if you want to apply 2D Light effects to a **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) art game, see [Precise pixel scaling and rotation via the Pixel Perfect Camera in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect.html).


## Create a Light 2D GameObject
Create a **2D Light** GameObject by going to **GameObject > Light** and selecting one of the four available types:
  * Sprite Light 2D
  * Spot Light 2D
  * Global Light 2D
  * Freeform Light 2D


## Additional resources
  * [Light 2D component reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DLightProperties.html)
  * [Configure a 2D light](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-properties-explained.html)
  * [Lighting in URP Learn tutorial](https://learn.unity.com/tutorial/editing-lighting-in-the-lightweight-render-pipeline)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Lights-2D-intro.html)
Introduction to the 2D lighting system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DLightProperties.html)
Light 2D component reference for URP
