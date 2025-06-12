* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/2Dor3D.html

  * [Get started with Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/get-started-with-unity.html)
  * 2D or 3D projects


[](https://docs.unity3d.com/6000.0/Documentation/Manual/get-started-with-unity.html)
Get started with Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/QuickstartGuides.html)
Quickstart guides
# 2D or 3D projects
Unity is equally suited to creating both 2D and 3D games. When you create a new project in Unity, you have the choice to start in 2D or 3D mode. You may already know what you want to build, but there are a few subtle points that may affect which mode you choose.
The choice between starting in 2D or 3D mode determines some settings for the Unity Editor, such as whether images are imported as textures or **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite). You can swap between 2D or 3D mode at any time regardless of the mode you set when you created your project (see [2D and 3D Mode Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/2DAnd3DModeSettings.html)). Here are some guidelines which should help you choose.
### Full 3D
![Some 3D scenes from Unitys sample projects on the Asset Store](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/3dGames.jpg) Some 3D scenes from Unity’s sample projects on the Asset Store
3D games usually make use of three-dimensional geometry, with Materials and Textures rendered on the surface of **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to make them appear as solid environments, characters and objects that make up your game world. The Camera can move in and around the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) freely, with light and shadows cast around the world in a realistic way. 3D games usually render the Scene using perspective, so objects appear larger on screen as they get closer to the camera. For all games that fit this description, start in **3D** mode.
### Orthographic 3D
![Some 3D games using an Orthographic view. Images created using assets from Synty Studios and BITGEM](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/3dOrthographicGames.jpg) Some 3D games using an Orthographic view. Images created using assets from [Synty Studios](https://assetstore.unity.com/publishers/5217) and [BITGEM](https://assetstore.unity.com/publishers/1299)
Sometimes games use 3D geometry, but use an orthographic camera instead of perspective. This is a common technique used in games which give you a bird’s-eye view of the action, and is sometimes called “2.5D”. If you’re making a game like this, you should also use the Editor in **3D** mode, because even though there is no _perspective_ , you will still be working with 3D models and Assets. You’ll need to switch your [Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) and [Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html)An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) to **Orthographic** though.
### Full 2D
![Some examples of typical 2D game types](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2dGames.jpg) Some examples of typical 2D game types
Many 2D games use flat graphics, sometimes called sprites, which have no three-dimensional geometry at all. They are drawn to the screen as flat images, and the game’s camera has no perspective. For this type of game, you should start the editor in **2D** mode.
### 2D gameplay with 3D graphics
![A side scrolling game with 2D gameplay, but 3d graphics](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2dGame3dSceneSideScroll.jpg) A side scrolling game with 2D gameplay, but 3d graphics
Some 2D games use 3D geometry for the environment and characters, but restrict the _gameplay_ to two dimensions. For example, the camera may show a side-scrolling view, and the player can only move in two dimensions, but the game itself still uses 3D models for the obstacles and a 3D perspective for the camera. For these games, the 3D effect may serve a stylistic rather than functional purpose. This type of game is _also_ sometimes referred to as “2.5D”. Although the gameplay is 2D, you are mostly manipulating 3D models to build the game, so you should start the editor in **3D** mode.
### 2D gameplay and graphics with a perspective camera
![A 2D cardboard theatre style game, giving a parallax movement effect. Image created using an asset by One Point Six Studio, available on the Unity Asset Store.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2dParallaxScroller.jpg) A 2D “cardboard theatre” style game, giving a parallax movement effect. Image created using an asset by [One Point Six Studio](https://assetstore.unity.com/publishers/8138), available on the Unity Asset Store.
This is another popular style of 2D game, using 2D graphics but with a perspective camera to get a parallax scrolling effect. This is a “cardboard theater”-style scene, where all graphics are flat, but arranged at different distances from the camera. It’s most likely that **2D** mode will suit your development in this case. However, you should change your [Camera’s](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html) projection mode to **Perspective** and the [Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewNavigation.html) mode to **3D**.
## Additional resources
  * [XR](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/get-started-with-unity.html)
Get started with Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/QuickstartGuides.html)
Quickstart guides
