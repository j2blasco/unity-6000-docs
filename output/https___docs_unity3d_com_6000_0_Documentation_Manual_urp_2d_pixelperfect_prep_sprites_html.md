* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect-prep-sprites.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-urp-landing.html)
  * [Precise pixel scaling and rotation via the Pixel Perfect Camera in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect.html)
  * Prepare your sprites for the 2D Pixel Perfect Camera in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect-intro.html)
Introduction to the Pixel Perfect Camera in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/pixel-cinemachine.html)
Make Cinemachine compatible with the 2D Pixel Perfect camera in URP
# Prepare your sprites for the 2D Pixel Perfect Camera in URP
Set up your **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) for compatibility with the **Pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) Perfect **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) component.
  1. After importing your asset into the project as sprites, set all sprites to the same **Pixels Per Unit** value.  
![Setting PPU value](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2D_Pix_image_1.png)
  2. In the sprites’ **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, open the **Filter Mode** dropdown and select **Point**.  
![Set Point mode](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2D_Pix_image_2.png)
  3. Open the ****Compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression)** dropdown and select **None**.  
![Set None compression](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2D_Pix_image_3.png)


Follow the steps below to set the pivot for a sprite:
  1. Open the **Sprite Editor** window for the selected sprite.
  2. If the sprite’s **Sprite Mode** is set to **Multiple** and there are multiple individual sprite elements in the imported texture, then you need to set a pivot point for each individual sprite element.
  3. In the Sprite panel at the lower left of the **Sprite Editor** window, open the **Pivot** dropdown and select **Custom**. Then open the **Pivot Unit Mode** and select **Pixels**. This allows you to set the pivot point’s coordinates in pixels, or drag the pivot point around in the **Sprite Editor** and have it automatically snap to pixel corners.  
![Setting the Sprite’s Pivot](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2D_Pix_image_4.png)
  4. Repeat step 3 for each sprite element as necessary.


## Set up snap settings
Follow the steps below to set the snap settings for your project to ensure that the movement of pixelated sprites are consistent with each other:
  1. To open the **Increment Snapping** settings, go to **Grid and Snap Overlay** in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view.  
![Snap Setting window](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2D_Pix_image_5.png)
  2. Set the **Move X/Y/Z** properties to 1 divided by the Pixel Perfect Camera’s **Asset Pixels Per Unit (PPU)** value. For example, if the Asset **PPU** is 100, you should set the **Move X/Y/Z** properties to 0.01 (1 / 100 = 0.01).  
![Grid Snap Setting window](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2D_Pix_image_6.png)
  3. Select the **Grid Snapping** icon to enable it (highlighted in blue).
  4. Unity does not apply Snap settings retroactively. If there are any pre-existing **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the scene, select each of them and select **All Axes** to apply the updated Snap settings.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect-intro.html)
Introduction to the Pixel Perfect Camera in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/pixel-cinemachine.html)
Make Cinemachine compatible with the 2D Pixel Perfect camera in URP
