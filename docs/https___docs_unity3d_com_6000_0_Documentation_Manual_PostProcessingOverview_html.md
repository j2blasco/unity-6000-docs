* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * Introduction to post-processing


[](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
Post-processing and full-screen effects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-effect-availability-reference.html)
Post-processing effect availability reference
# Introduction to post-processing
Unity provides a number of ****post-processing**** effects and full-screen effects that can greatly improve the appearance of your application with little set-up time. You can use these effects to simulate physical **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) and film properties, or to create stylised visuals.
This page contains the following information:
  * [Render pipeline compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html#render-pipeline-compatibility)
  * [Effect availability and location](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html#effect-availability-and-location)


The images below demonstrate a **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) with and without post-processing.
![Scene with no post-processing](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PostProcessing-0.jpg) Scene with no post-processing ![Scene with post-processing](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PostProcessing-1.jpg) Scene with post-processing
## Render pipeline compatibility
Which post-processing effects are available and how you apply them depend on which [render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) you are using. A post-processing solution from one render pipeline is not compatible with other render pipelines.
This table contains information about which of Unity’s post-processing solutions are compatible with each of Unity’s render pipelines.
**Render pipeline** | **Post-processing support**  
---|---  
**[Universal Render Pipeline (URP)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-introduction.html)** | URP includes its own post-processing solution, which Unity installs when you create a Project using a URP Template. For information on using post-processing effects in URP, see the [URP post-processing documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/integration-with-post-processing.html).  
**[High Definition Render Pipeline (HDRP)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?preview=1)** | HDRP includes its own post-processing solution, which Unity installs when you create a Project using an HDRP Template. For information on using post-processing effects in HDRP, see the [HDRP post-processing documentation](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Post-Processing-Main.html).  
[**Built-in Render Pipeline**](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-RenderPipeline.html) | The Built-in Render Pipeline does not include a post-processing solution by default. To use post-processing effects with the Built-in Render Pipeline, download the [Post-Processing Version 2](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest) package. For information on using post-processing effects in the Built-in Render Pipeline, see the [Post-Processing Version 2](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest) documentation.  
**Note:** Post processing stack version 1 is now deprecated and should not be used.
## Effect availability and location
For information on the specific post-processing effects each render pipeline supports, refer to [Post-processing effect availability reference](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-effect-availability-reference.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
Post-processing and full-screen effects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-effect-availability-reference.html)
Post-processing effect availability reference
