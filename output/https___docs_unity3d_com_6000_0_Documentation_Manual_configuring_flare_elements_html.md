* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-flare-elements.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Lens flares](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lens-flares.html)
  * [Lens flares in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lens-flare-birp.html)
  * Configuring Flare elements


[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-lens-flare.html)
Create a lens flare
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Flare.html)
Flare asset reference
# Configuring Flare elements
Learn how Unity manages elements on a Flare asset, and compare texture layout options.
A Flare consists of multiple **Elements** , arranged along a line. The line is calculated by comparing the position of the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) containing the Lens Flare to the center of the screen. The line extends beyond the containing GameObject and the screen center. All Flare **Elements** are strung out on this line.
For performance reasons, all **Elements** of one Flare must share the same Texture. This Texture contains a collection of the different images that are available as Elements in a single Flare. The **Texture Layout** defines how the **Elements** are laid out in the **Flare Texture**. If you use many different Flare assets, using a shared single **Flare Texture** that contains all the **Elements** will give you best rendering performance.
Lens Flares are blocked by **Colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider). A Collider in-between the Flare GameObject and the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) will hide the Flare, even if the Collider does not have a **Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer). If the in-between Collider is marked as Trigger it will block the flare if and only if **Physics.queriesHitTriggers** is true.
To override the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) used for Flares, open the [Graphics](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html) window and set **Lens Flares** A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare) to the shader that you would like to use as the override.
## Understand texture layouts
These are the options you have for different Flare **Texture Layouts**. The numbers in the images correspond to the **Image Index** property for each **Element**.
### 1 Large 4 Small
Designed for large sun-style Flares where you need one of the **Elements** to have a higher fidelity than the others. This is designed to be used with Textures that are twice as high as they are wide.
![The large particle \(element 0\) is the top half of the texture. The 4 small particles are in a 2 x 2 layout in the bottom half of the texture. The element values increment from left to right in each row.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/FlaresLayout0.png) The large particle (element 0) is the top half of the texture. The 4 small particles are in a 2 x 2 layout in the bottom half of the texture. The element values increment from left to right in each row.
### 1 Large 2 Medium 8 Small
Designed for complex flares that require 1 high-definition, 2 medium and 8 small images. This is used in the standard assets “50mm Zoom Flare” where the two medium Elements are the rainbow-colored circles. This is designed to be used with textures that are twice as high as they are wide.
![The large particle \(element 0\) is the top half of the texture. In the bottom half, the 2 medium particles \(1 and 2\) are on the left side, with element 1 on top. The 8 small particles \(starting with element 3\) are in a 2 x 4 pattern on the right side. For the small particles, the element values increment from left to right in each row.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/FlaresLayout1.png) The large particle (element 0) is the top half of the texture. In the bottom half, the 2 medium particles (1 and 2) are on the left side, with element 1 on top. The 8 small particles (starting with element 3) are in a 2 x 4 pattern on the right side. For the small particles, the element values increment from left to right in each row.
### 1 Texture
A single image.
![A single particle texture.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/FlaresLayout2.png) A single particle texture.
### 2x2 grid
A simple 2x2 grid.
![A 2 x 2 grid of particles. The element values increment from left to right in each row.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/FlaresLayout3.png) A 2 x 2 grid of particles. The element values increment from left to right in each row.
### 3x3 grid
A simple 3x3 grid.
![A 3 x 3 grid of particles](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/FlaresLayout4.png) A 3 x 3 grid of particles
### 4x4 grid
A simple 4x4 grid.
![A 4 x 4 grid of particles.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/FlaresLayout5.png) A 4 x 4 grid of particles.
Flare
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/create-lens-flare.html)
Create a lens flare
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Flare.html)
Flare asset reference
