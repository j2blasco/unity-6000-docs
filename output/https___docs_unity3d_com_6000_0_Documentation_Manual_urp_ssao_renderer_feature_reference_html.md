* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/ssao-renderer-feature-reference.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * [Shadows in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Shadows-in-URP.html)
  * [Screen space ambient occlusion (SSAO) in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao-landing.html)
  * Configure screen space ambient occlusion in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/add-ssao-renderer-feature-to-renderer.html)
Add a Screen Space Ambient Occlusion Renderer Feature to a URP Renderer
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shadow-cascades-visualize.html)
Visualize shadow cascades
# Configure screen space ambient occlusion in URP
The properties of URP’s Screen Space **Ambient Occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion) (SSAO) renderer feature allow you to configure it to best suit the graphical and performance needs of a project.
## Properties
This section describes the properties of the SSAO Renderer Feature.
### Method
This property defines the type of noise the SSAO effect uses.
Available Options:
  * **Interleaved Gradient Noise** : Uses interleaved gradient noise to generate static SSAO.
  * **Blue Noise** : Uses a selection of blue noise textures to generate dynamic SSAO. This creates an animated effect as the texture changes with every frame, as a result the SSAO effect is more subtle when the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) is in motion.


**Performance impact** : Insignificant.
### Intensity
This property defines the intensity of the darkening effect.
**Performance impact** : Insignificant.
### Radius
When Unity calculates the Ambient Occlusion value, the SSAO effect takes samples of the normal texture within this radius from the current **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel).
**Performance impact** : High.
A lower **Radius** value improves performance, because the SSAO Renderer Feature samples pixels closer to the source pixel. This makes caching more efficient.
Calculating the Ambient Occlusion Pass on objects closer to the Camera takes longer than on objects further from the Camera. This is because the **Radius** property scales with the object.
### Falloff Distance
SSAO does not apply to objects farther than this distance from the Camera.
A lower value increases performance in **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) that contain many distant objects. The performance improvement is smaller in smaller scenes with fewer objects.
![Scene with only Ambient Occlusion texture demonstrating a varying fall-off distance.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/ssao/ssao-falloff-distance.gif) Scene with only Ambient Occlusion texture demonstrating a varying fall-off distance.
**Performance impact** : Depends on the application.
### Direct Lighting Strength
This property defines how visible the effect is in areas exposed to direct lighting.
These images show how the **Direct Lighting Strength** value changes the SSAO effect depending on whether they are in the shadow or not.
![Direct Lighting Strength: 0.2.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/ssao/ssao-direct-lighting-strength-weak.png) **Direct Lighting Strength** : 0.2. ![Direct Lighting Strength: 0.9.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/ssao/ssao-direct-lighting-strength-strong.png) **Direct Lighting Strength** : 0.9.
**A**. Shows the effect of **Direct Lighting Strength** on the SSAO effect in lit areas.
**B**. Shows the effect of **Direct Lighting Strength** on the SSAO effect in areas one or more shadows cover.
**Performance impact** : Insignificant.
## Quality
### Source
Select the source of the normal vector values. The SSAO Renderer Feature uses normal vectors for calculating how exposed each point on a surface is to ambient lighting.
Available options:
  * **Depth Normals** : SSAO uses the normal texture generated by the `DepthNormals` Pass. This option lets Unity make use of a more accurate normal texture.
  * **Depth** : SSAO does not use the `DepthNormals` Pass to generate the normal texture. SSAO reconstructs the normal vectors using the depth texture instead. Use this option only if you want to avoid using the `DepthNormals` Pass block in your custom **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader). Selecting this option enables the **Normal Quality** property.


**Performance impact** : Depends on the application.
When you switch between the options **Depth Normals** and **Depth** , there might be a variation in performance, which depends on the target platform and the application. In a wide range of applications the difference in performance is small. In most cases, **Depth Normals** produce a better visual look.
For more information on the Source property, refer to the [Implementation details](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao.html#implementation-details).
### Normal Quality
This property becomes active when you select the option Depth in the **Source** property.
Higher quality of the normal vectors produces smoother SSAO effect.
Available options:
  * **Low**
  * **Medium**
  * **High**


**Performance impact** : Medium.
In some scenarios, the **Depth** option produces results comparable with the **Depth Normals** option. But in certain cases, the **Depth Normals** option provides a significant increase in quality. The following images show an example of such case.
![Source: Depth. Normal Quality: Low.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/ssao/ssao-depth-q-low.png) **Source** : Depth. **Normal Quality** : Low. ![Source: Depth. Normal Quality: Medium.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/ssao/ssao-depth-q-medium.png) **Source** : Depth. **Normal Quality** : Medium. ![Source: Depth. Normal Quality: High.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/ssao/ssao-depth-q-high.png) **Source** : Depth. **Normal Quality** : High. ![Source: Depth Normals.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/ssao/ssao-depth-normals.png) **Source** : Depth Normals.
For more information, refer to the [Implementation details](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao.html#implementation-details).
### Downsample
Selecting this check box reduces the resolution of the Pass that calculates the Ambient Occlusion effect by a factor of two.
The reduction in resolution of the Ambient Occlusion Pass by a factor of two reduces the pixel count to process by a factor of four. This reduces the load on the GPU significantly, but makes the effect less detailed.
**Performance impact** : Very high.
### After Opaque
When you enable **After Opaque** , Unity calculates and applies the SSAO effect after the opaque render pass. This can increase performance when used with **Depth** as the **Source** for normal vector values as Unity does not perform the depth prepass to calculate SSAO and instead uses the existing depth values. However, this can cause over-darkening of the areas that receive baked occlusion and real-time occlusion.
**After Opaque** can also increase performance on mobile devices that use tile-based rendering.
**Performance impact** : Medium.
### Blur Quality
This property defines the quality of blur that Unity applies to the SSAO effect. Higher quality blur creates a smoother, higher fidelity effect but requires more processing power.
Available options:
  * **High** (Bilateral): Bilateral blur, takes three passes to process.
  * **Medium** (Gaussian): Gaussian blur, takes two passes to process.
  * **Low** (Kawase): Kawase blur, takes a single pass to process.


**Performance impact** : Very high.
### Samples
For each pixel, the SSAO Render Feature takes the selected number of samples within the specified radius to calculate the Ambient Occlusion value. A higher value makes the effect smoother and more detailed, but also reduces performance.
Available options:
  * **High** : 12 Samples
  * **Medium** : 8 Samples
  * **Low** : 4 Samples


**Performance impact** : High.
An increase in the **Sample Count** value from 4 to 8 doubles the computational load on the GPU.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/add-ssao-renderer-feature-to-renderer.html)
Add a Screen Space Ambient Occlusion Renderer Feature to a URP Renderer
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shadow-cascades-visualize.html)
Visualize shadow cascades
