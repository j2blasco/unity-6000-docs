* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmaps-reference.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * [Baking lightmaps before runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baking-before-runtime.html)
  * Lightmapping settings in the Lighting Settings Asset reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUProgressiveLightmapper.html)
Optimize baking
[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-landing.html)
Creating lightmaps at runtime with Enlighten Realtime Global Illumination
# Lightmapping settings in the Lighting Settings Asset reference
For all other lighting settings, see [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html).
**Property** | **Description**  
---|---  
**Lightmapper** | Use this to specify which internal lighting calculation software to use to calculate lightmaps in the Scene. The options are:  
  

  * [Progressive CPU](https://docs.unity3d.com/6000.0/Documentation/Manual/progressive-lightmapper.html)
  * [Progressive GPU](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUProgressiveLightmapper.html)

  
The default value is **Progressive CPU**.  
**Importance Sampling** | Enable this to use multiple importance sampling for sampling the environment. This generally leads to faster convergence when generating **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap), but can lead to noisier results in certain low frequency environments. This is disabled by default.  
**Direct Samples** | The number of samples (paths) shot from each texel. This setting controls the number of samples that the Progressive Lightmapper uses for direct lighting calculations. Move the slider to improve the quality of direct lighting in lightmaps and Light Probes, at the cost of longer bake times. You can only set the slider to powers of 2. The default maximum value is 1024, but you can change the maximum by typing a new value into the field next to the slider, up to a limit of 230  
**Indirect Samples** | The number of samples (paths) shot from each texel. This setting controls the number of samples that the Progressive Lightmapper uses for indirect lighting calculations. For some Scenes, especially outdoor Scenes, 128 samples should be enough. For indoor Scenes with emissive geometry, increase the value until you see the amount of noise is acceptable. Move the slider to improve the quality of indirect lighting in lightmaps, at the cost of longer bake times. You can only set the slider to powers of 2. The default maximum value is 8192, but you can change the maximum by typing a new value into the field next to the slider, up to a limit of 230  
**Environment Samples** | The Environment Samples property determines the total number of environment rays that Unity fires toward the skybox to gather light directly. Unity fires these rays from the lightmap texel or light probe position depending on the context. The default value is 256. Higher values might yield smoother results, but at the cost of increased bake times. You can only set the slider to powers of 2, with a minimum of 1 and a maximum of 2048.  
  
In Scenes with HDR skyboxes, more samples are often needed to reduce noise in the final lightmap or probe. Scenes with skyboxes that include bright singularities (such as the sun) or high-frequency details with significant contrast (such as backlit clouds) also benefit from a higher number of samples.  
**Light Probe Sample Multiplier** | Controls how many samples are used for Light Probes as a multiplier of the sample values above. Higher values improve the quality of Light Probes, but they will take longer to bake. To enable this feature, go to **Project Settings > Editor** and disable **Use legacy Light Probe sample counts.** The default value is 4.  
**Bounces** | Use this value to specify the number of indirect bounces to do when tracing paths. For most **Scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), two bounces are enough. For some indoor Scenes, more bounces might be necessary.  
**Max Bounces** | The maximum number of bounces you want the Progressive Lightmapper to include in indirect lighting calculations.   
  
Default value: 2. Range: 0 - 100.  
  
Values of up to 10 are suitable for most Scenes. Values higher than 10 might lead to significantly longer bake times.  
  
Each bounce increases the computational resources needed to bake your scene. Use higher bounce values for indoor Scenes, and lower bounce values for outdoor Scenes and those with many bright surfaces.  
  
  
**Filtering** | Configure the way the Progressive Lightmapper applies post-processing to lightmaps to limit noise. For lightmap post-processing, the lightmap is split into **Direct** , **Indirect** and **Ambient Occlusion** targets that Unity applies post-processing to individually, before it composites them together into a single lightmap.  
  
- **Direct** : Any light that arrives directly from a Light to a sensor (usually the Camera).  
- **Indirect** : Any light that arrives indirectly from a Light to a sensor. This most commonly applies to light that reflects off other GameObjects.  
- **Ambient Occlusion** : Any ambient light that the lighting system calculates.  
  
The options are:
  * **None** : Select this to use no filter or denoising for the lightmap.
  * **Auto** : Select this to use a platform-dependent preset for post-processing the lightmap. If your development machine fulfills the requirements to run OptiX (the [NVIDIA OptiX AI-Accelerated Denoiser](https://developer.nvidia.com/optix-denoiser)), the Progressive Lightmapper uses the denoiser with a Gaussian filter that has a 1-texel radius for all targets. If your development machine cannot run OptiX, the Progressive Lightmapper falls back to **OpenImageDenoise**.
  * **Advanced** : Select **Advanced** to manually configure options for each type of lightmap target. The targets types are **Direct** , **Indirect** and **Ambient Occlusion**. For more information, refer to [Advanced Filtering settings](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmaps-reference.html#AdvancedFilteringSettings).

  
**Lightmap Resolution** | Specifies the number of texels per unit to use for lightmaps. Increasing this value improves lightmap quality, but also increases bake times. Note that doubling this value causes the number of texels to quadruple because it determines both the height and width of the lightmap. See the **Occupied texels** count in the statistics area of the Lighting window.  
**Lightmap Padding** | Determines the separation (in texel units) between separate shapes in the baked lightmap. The default is 2.  
**Max Lightmap Size** | Specifies the size (in pixels) of the full lightmap texture, which incorporates a separate region for each included **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). The default value is 1024.  
**Lightmap compression** | The level of compression the Editor uses for lightmaps.   
- None: Does not compress lightmaps.   
- Low Quality: This may use less memory and storage than Normal Quality, but can also introduce visual artifacts.   
- Normal Quality: This is a good trade-off between memory usage and visual quality.   
- High Quality: Requires more memory and storage than Normal Quality, but provides better visual results.  
****Ambient Occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion)** | Controls the relative brightness of surfaces in [baked ambient occlusion](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingBakedAmbientOcclusion.html). This only applies to the indirect lighting calculated by the **lightmapper** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmapper) you are using to bake your lighting. Enabled by default. If Ambient Occlusion is enabled, it exposes three settings: Max Distance, Indirect Contribution, and Direct Contribution. For all three settings, higher values indicate a greater contrast between occluded and fully lit areas.  
**Max Distance** | Specifies how far the lighting system casts rays in order to determine whether or not to apply occlusion to an object. A higher value produces longer rays and contributes more shadows to the lightmap, while a lower value produces shorter rays that contribute shadows only when objects are very close to one another. A value of 0 casts an infinitely long ray that has no maximum distance. The default value is 1.  
**Indirect Contribution** | Scales the brightness of indirect **ambient light** Light that doesn’t come from any specific direction, and contributes equal light in all directions to the Scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientlight) bounced and emitted from objects in the final lightmap. This is a value between 0 and 10. The default value is 1. Values less than 1 reduce the intensity, while values greater than 1 increase it.  
**Direct Contribution** | Scales the brightness of direct light. This is a value between 0 and 10. The default value is 0. The higher this value is, the greater the contrast the Editor applies to the direct lighting.  
**Directional Mode** | Enables the lightmap to store information about the characteristics of the dominant incoming light at each point on an object’s surface. See [Directional Lightmapping](https://docs.unity3d.com/6000.0/Documentation/Manual/LightmappingDirectional.html) for more information. The default mode is **Directional**.  
**Directional** | In **Directional** mode, Unity generates a second lightmap to store the dominant direction of incoming light. This makes it possible for diffuse normal mapped materials to work with the **global illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) system. **Shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) sample both lightmap textures during rendering. As a result, directional mode requires about twice as much video memory as non-directional mode for the additional lightmap data. Generating the additional directionality texture has an impact on baking performance. Directional lightmaps cannot be decoded on SM2.0 hardware or when using GLES2.0.  
**Non-directional** |  **Non-directional** mode lightmaps only include a single texture. As a result, they require less video memory and less storage than directional lightmaps, and are faster to decode in shaders. These optimizations reduce visual quality.  
**Indirect Intensity** | Determines the brightness of indirect light stored in real-time and baked lightmaps. This is a value between 0 and 5. A value above 1 increases the intensity of indirect light while a value of less than 1 reduces indirect light intensity. The default value is 1.  
**Albedo Boost** | Specifies the amount of light Unity bounces between surfaces. This value is between 1 and 10. Increasing this value pulls the albedo value towards white for indirect light computation. The default value of 1 is physically accurate.  
**Lightmap Parameters** | A Lightmap Parameters **Asset stores** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore) values for settings relevant to Baked Global Illumination. The Editor provides several default Lightmap Parameters Assets to choose from, but you can also create your own lightmap parameters file using the **Create New** option. See [Lightmap Parameters](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightmapParameters.html) for more information. The default value is **Default-Medium**. The options are Default-Medium, Default-HighResolution, Default-LowResolution, and Default-VeryLowResolution.  
## Advanced Filtering settings
Set **Filtering** to **Advanced** to manually configure options for each type of lightmap target. The target types are:
  * **Direct** : Any light that arrives directly from a Light to a sensor (usually the Camera).
  * **Indirect** : Any light that arrives indirectly from a Light to a sensor. This most commonly applies to light that reflects off other GameObjects.
  * **Ambient Occlusion** : Any ambient light that the lighting system calculates.

**Setting** | **Description**  
---|---  
**Denoiser** | Select a denoiser to use for the lightmap target. The options are:  
  
- **Optix** : The NVIDIA Optix denoiser is an AI accelerated denoiser that reduces noise in baked lightmaps. It requires an NVIDIA GeForce, Quadro, or Tesla GPU with Maxwell or newer generation architecture, using driver version R495.89 or above. Optix is only supported on Windows.  
- **OpenImageDenoise** : Intel’s Open Image Denoise is an AI-accelerated denoiser that reduces noise in baked lightmaps.  
- **None** : Do not use a denoiser.  
**Filter** | Select a filter to use for the lightmap target:  
  
- **Gaussian:** Select this to use a Gaussian filter for the lightmap target. The Gaussian filter applies a bilateral Gaussian filter on the lightmap. This blurs the lightmap and reduces the visible noise.  
- **A-Trous:** Select this to use an A-Trous filter for the lightmap target. The A-Trous filter minimizes the amount of blur while it removes visible noise in the lightmap.  
- **None** : Select this to disable all filtering for the lightmap target.  
**Radius** | This option is only available when **Filter** is set to **Gaussian**. Use the **Radius** value to set the radius of the Gaussian filter kernel in texels. A higher **Radius** increases the blur strength and reduces the perceptible noise, but might cause detail to be lost in the lighting.  
**Sigma** | This option is only available when **Filter** is set to **A-Trous**. Use the **Sigma** value to adjust how much to preserve detail or blur the lighting. A higher **Sigma** increases the blur strength and reduces the perceptible noise, but might cause detail to be lost in the lighting.  
## Statistics
The panel below the **Generate Lighting** button shows statistics about the lightmapping, including:
  * The number of lightmaps that Unity has created
  * **Memory Usage:** The amount of memory required for the current lightmapping.
  * **Occupied Texels** : The number of texels that are occupied in lightmap UV space.
  * **Converged** : All calculations for these lightmaps are complete.
  * **Not Converged** : Baking is still in progress for these lightmaps.
  * **Bake Performance** : The number of rays per second. If this is low (that is, less than 2) you should adjust your settings or your hardware to process more light rays at a time.


## ETA
The progress bar that appears while Unity is baking the lightmap provides an “estimated time of arrival” (displayed as **ETA**). This is the estimated time in seconds for the current bake to complete. This allows for much more predictable baking times and allows you to quickly learn how much time baking takes with your current lighting settings.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUProgressiveLightmapper.html)
Optimize baking
[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-landing.html)
Creating lightmaps at runtime with Enlighten Realtime Global Illumination
