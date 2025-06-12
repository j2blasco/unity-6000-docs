* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/generate-physics-shape.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Sprite editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html)
  * [Custom physics shape](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/custom-physics-shape-landing.html)
  * Generate the physics shape


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/open-custom-physics-shape-editor.html)
Open the Custom Physics Shape editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/manually-edit-physics-shape.html)
Manually edit the physics shape
# Generate the physics shape
To have Unity automatically generate a physics shape that follows the shape of the original **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) texture, and that also takes into account transparent areas in the texture;
  1. Click the **Generate** button.
However, you can adjust how tightly the generated physics shape follows the Sprite texture by adjusting the **Outline Tolerance** slider.
  2. Adjust the **Outline Tolerance** slider to refine the outline of the physics shape that Unity generates.
Increasing the value increases how closely the outline follows the shape of the Sprite texture. Leaving the slider at 0 generates a physics shape that more loosely follows the Sprite texture.
  3. After adjusting the Outline Tolerance value, to have Unity automatically generate the physics shape based on the slider settings, click **Generate**.
If you adjust the slider value after generating an outline, to regenerate the outline based on the updated slider value, click **Generate** again.

![The generated outline and control points.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2D-CustomPS-generatedoutline.png) The generated outline and control points.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/open-custom-physics-shape-editor.html)
Open the Custom Physics Shape editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/manually-edit-physics-shape.html)
Manually edit the physics shape
