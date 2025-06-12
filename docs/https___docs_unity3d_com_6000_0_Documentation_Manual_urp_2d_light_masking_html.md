* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-masking.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-urp-landing.html)
  * [2D lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-index.html)
  * [Blend Modes in 2D lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-blending.html)
  * Masking


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-blend-modes.html)
Blend Modes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/SecondaryTextures.html)
Add normal map and mask textures to a sprite in URP
# Masking
This property determines how Unity blends the lighting with the colors of the **sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) and other **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that the light affects. The following are some examples of how a mask affects the sprite its covering with different **Blend Modes**.
![Original rock color](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/image_45.png) | ![Rock Mask](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/image_46.png)  
---|---  
Rock sprite with its original color. | Rock with a mask  
![Additive Light Blending](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/image_47.png) | ![Masked Additive Light Blending](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/image_48.png)  
Additive Light Blending | Additive Light Blending with a mask  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-blend-modes.html)
Blend Modes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/SecondaryTextures.html)
Add normal map and mask textures to a sprite in URP
