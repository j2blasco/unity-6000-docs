* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Lens flares](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lens-flares.html)
  * [Lens flares in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare.html)
  * Add screen space lens flares in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-component.html)
Add lens flares in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)
Lens Flare (SRP) component reference for URP
# Add screen space lens flares in URP
![A scene with screen space lens flares turned on.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shared/lens-flare/screenspacelensflaresurp.png) A scene with screen space lens flares turned on.
The **Screen Space**Lens Flare** A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare)** override adds lens flares to your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
To calculate lens flares, the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) fetches bright areas of the current image, such as emissive lights and bright specular reflections. URP then draws the same areas back to the screen in different locations and using different effects such as stretch, blur, and chromatic aberration.
The **Screen Space Lens Flare** creates lens flares from the following:
  * Emissive surfaces.
  * Bright spots in your scene that appear depending on the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) view, for example a bright specular reflection on a shiny metal object, or a bright outside area viewed from a dark indoor area.
  * All onscreen lights.


You can use the [Lens Flare (SRP)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-component.html) component instead to create a flare for a light that has a specific position in the scene. You can also use both the **Lens Flare (SRP)** component and the **Screen Space Lens Flare** override in the same scene.
## How screen space lens flares work
The bright areas URP uses to calculate screen space lens flares are the same areas the [Bloom override](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-bloom.html) brightens.
URP uses the same buffer as the Bloom override to fetch the bright areas and render the lens flares. The settings in the Bloom override affect the appearance of screen space lens flares.
**Note** : If you have a [Bloom override](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-bloom.html) in the volume, set **Intensity** in the Bloom override to a value higher than 0 or lens flares won’t appear.
You can create the following types of lens flare:
  * Regular flares, which are a brightened distorted version of the bright areas of the screen.
  * Reversed flares, which are regular flares flipped upside-down and reversed.
  * Warped flares, which are regular flares transformed using polar coordinates, to mimic a circular camera lens.
  * Streaks, which are flares stretched in one direction, to mimic an anamorphic camera lens.


You can control which types of flares appear and how many there are. You can also control the chromatic aberration effect URP adds to the flares.
![The left image shows an emissive cube with bloom but no lens flares. The right image shows the same cube and a regular flare \(top-left\), a reversed flare \(bottom-right\), a warped flare \(top-right\) and streaks \(to the left and right of the cube\).](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shared/lens-flare/screenspacelensflares-types.png) The left image shows an emissive cube with bloom but no lens flares. The right image shows the same cube and a regular flare (top-left), a reversed flare (bottom-right), a warped flare (top-right) and streaks (to the left and right of the cube).
**Note** : Some lens flares only appear, or only appear at full intensity, if you enable High Dynamic Range (HDR) rendering on your camera. To enable **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR), refer to [the **Output** section of the Camera component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html#Output)
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-component.html)
Add lens flares in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)
Lens Flare (SRP) component reference for URP
