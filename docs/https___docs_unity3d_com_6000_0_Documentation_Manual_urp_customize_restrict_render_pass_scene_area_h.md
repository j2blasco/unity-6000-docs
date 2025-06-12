* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/restrict-render-pass-scene-area.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Adding a Scriptable Render Pass to the frame rendering loop in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/inject-a-render-pass.html)
  * Restrict a render pass to a scene area in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/inject-render-pass-via-script.html)
Inject a render pass via scripting in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/custom-pass-injection-points.html)
Injection points reference for URP
# Restrict a render pass to a scene area in URP
To restrict a render pass to a specific area of a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), add a [volume](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/volumes-landing-page.html) to the scene, then add code to your render pass and your **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) to check if the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) is inside the volume.
Follow these steps:
  1. Update your shader code to enable or disable your custom rendering effect based on a Boolean value.
For example, add the following code to your shader:
```
Pass
{
    ...

    // Add a variable to enable or disable your custom rendering effect
    float _Enabled;

    ...

    float4 Frag(Varyings input) : SV_Target0
    {
        ...

        // Return the color with the effect if the variable is 1, or the original color if the variable is 0
        if (_Enabled == 1){
            return colorWithEffect;
        } else {
            return originalColor;
        }
    }
}

```

  2. Create a script that implements the `VolumeComponent` class. This creates a volume override component that you can add to a volume.
```
using UnityEngine;
using UnityEngine.Rendering;

public class MyVolumeOverride : VolumeComponent
{
}

```

  3. In the **Hierarchy** window, select the **Add** (**+**) button, then select **GameObject** > **Volume** > **Box Volume**.
  4. In the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window for the new box volume, under **Volume** , select **New** to create a new volume profile.
  5. Select **Add override** , then select your volume override component, for example **My Volume Override**.
  6. Add a property to the volume override script. Unity adds the property in the **Inspector** window of the volume override.
For example:
```
public class MyVolumeOverride : VolumeComponent
{
    // Add an 'Effect Enabled' checkbox to the Volume Override, with a default value of true.
    public BoolParameter effectEnabled = new BoolParameter(true);
}

```

  7. In your custom pass, use the `GetComponent` API to get the volume override component and check the value of the property.
For example:
```
class myCustomPass : ScriptableRenderPass
{

    ...

    public void Setup(Material material)
    {
        // Get the volume override component
        MyVolumeOverride myOverride = VolumeManager.instance.stack.GetComponent<MyVolumeOverride>();

        // Get the value of the 'Effect Enabled' property
        bool effectStatus = myOverride.effectEnabled.overrideState ? myOverride.effectEnabled.value : false;
    }
}

```

  8. Pass the value of the property to the variable you added to the shader code.
For example:
```
class myCustomPass : ScriptableRenderPass
{

    ...

    public void Setup(Material material)
    {
        MyVolumeOverride myOverride = VolumeManager.instance.stack.GetComponent<MyVolumeOverride>();
        bool effectStatus = myOverride.effectEnabled.overrideState ? myOverride.effectEnabled.value : false;

        // Pass the value to the shader
        material.SetFloat("_Enabled", effectStatus ? 1 : 0);
    }
}

```



Your custom rendering effect is now enabled when the camera is inside the volume, and disabled when the camera is outside the volume.
## Additional resources
  * [Write a Scriptable Render Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/write-a-scriptable-render-pass.html)
  * [Volumes in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/volumes-landing-page.html)
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
  * [Create a custom post-processing effect with Volume support in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/custom-post-processing-with-volume.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/inject-render-pass-via-script.html)
Inject a render pass via scripting in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/custom-pass-injection-points.html)
Injection points reference for URP
