* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-rendertexture.html

  * [Video and cutscenes](https://docs.unity3d.com/6000.0/Documentation/Manual/Video.html)
  * [Video Player](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer.html)
  * Set up your Render Texture to display video


[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-instructions.html)
Create a Video Player component
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-MigratingFromMovieTexture.html)
Migrating from MovieTexture to VideoPlayer
# Set up your Render Texture to display video
Use a **Render Texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) to display your video content on the surface of multiple **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that share the Render Texture or to apply **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects to the video.
To display your video content on a Render Texture: 
  1. [Prepare your Render Texture for video](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-rendertexture.html#prepare).
  2. [Set a Render Texture as your Video Player’s target](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-rendertexture.html#target).


## Prepare your Render Texture for video
To optimize your Render Texture for use with video content:
  1. Click on your Render Texture to open the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window.
  2. Make sure the resolution of the Render Texture matches the resolution of your video content.
  3. Set **Anti-aliasing** to **None**.
  4. Set **Color Format** to **R8G8B8A8_UNORM**. If you notice excessive banding with your Render Texture, particularly in dark areas where the color transitions look unnatural, set **Color Format** to **R16G16B16A16_UNORM**.
  5. Set **Depth Stencil Format** to **None**.
  6. Disable **Mipmap**.
  7. Set **Wrap Mode** to **Clamp**.
  8. Set **Filter Mode** to **Point**.
  9. Disable anisotropic filtering via script: `renderTexture.anisoLevel = 0;`


When done, your Render Texture is ready for your video content. 
## Set a Render Texture as your Video Player’s target
To have your video play on your Render Texture, you need to set up your Video Player component to target your Render Texture: 
  1. Click on the GameObject that contains the Video Player component. The Inspector window opens.
  2. Set **Render Mode** to **Render Texture**.
  3. Assign your Render Texture to **Target Texture**.


Your Video Player component now targets your optimized Render Texture. 
## Additional resources
  * [VideoPlayer API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)
  * [Video Player](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer.html)
  * [Video Player component targets](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-intro.html)
  * [Video Player component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoPlayer.html)
  * [Create a Video Player component](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-instructions.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-instructions.html)
Create a Video Player component
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-MigratingFromMovieTexture.html)
Migrating from MovieTexture to VideoPlayer
