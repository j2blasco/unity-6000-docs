* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-ambient-light.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Light sources](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-sources.html)
  * Add ambient light from the environment


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightExplorerExtension.html)
Customize the Light Explorer
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies.html)
Cookies
# Add ambient light from the environment
Ambient light, also known as diffuse environmental light, is light that is present all around the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and doesn’t come from any specific source object. It can be an important contributor to the overall look and brightness of a scene.
Ambient light can be useful in a number of cases, depending upon your chosen art style. An example would be bright, cartoon-style rendering where dark shadows may be undesirable or where lighting is perhaps hand-painted into textures. **Ambient light** Light that doesn’t come from any specific direction, and contributes equal light in all directions to the Scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientlight) can also be useful if you need to increase the overall brightness of a scene without adjusting individual lights.
## Add ambient light
After you [create a skybox material](https://docs.unity3d.com/6000.0/Documentation/Manual/skyboxes-using.html), Unity can use it to generate ambient lighting in your Scene. To make Unity do this:
  1. Open the Lighting window (menu: **Window > Rendering > Lighting**).
  2. Select the **Environment** tab.
  3. Assign your chosen **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) to the **Skybox Material** property.
  4. Click the **Source** drop-down and, from the list, click **Skybox**.


You can also specify when Unity updates the ambient lighting. To do this, change the **Ambient Mode**. The two values are:
  * **Realtime** : Unity constantly regenerates ambient lighting for your Scene. This is useful if you alter the skybox at run-time
  * **Baked** : Unity only generates ambient lighting for your Scene when you click the **Generate Lighting** button at the bottom of the Lighting window. This is useful if your skybox does not change during run-time because it saves computational resources.


## Additional resources
  * [Skyboxes](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)
  * [Visual environment in the High Definition Render Pipeline (HDRP)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Override-Visual-Environment.html)
  * [Changing lighting at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probe-volumes-change-lighting-at-runtime.html)
  * [Add ambient occlusion](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingBakedAmbientOcclusion.html)
  * [Screen space ambient occlusion in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightExplorerExtension.html)
Customize the Light Explorer
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies.html)
Cookies
