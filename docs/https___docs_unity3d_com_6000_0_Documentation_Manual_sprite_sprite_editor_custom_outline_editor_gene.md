* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-outline-editor/generate-outline.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Sprite editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html)
  * [Custom outline](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-landing.html)
  * Generate the outline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-landing.html)
Custom outline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-outline-editor/edit-custom-outline.html)
Edit the custom outline
# Generate the outline
To have Unity automatically generate an outline that follows the shape of the original **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) texture, and that also takes into account transparent areas in the texture, click the **Generate** button. However, you can adjust how tightly the generated outline follows the Sprite texture by adjusting the **Outline Tolerance** slider.
Adjust the **Outline Tolerance** slider to refine the outline of the **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) that Unity generates. Increasing the value increases how closely the outline follows the shape of the Sprite texture. Leaving the slider at 0 generates a Mesh that more loosely follows the Sprite texture.
![Left: An automatically generated Mesh outline with a low Outline Tolerance. Right: An automatically generated Mesh outline with a high Outline Tolerance.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/2DCustomOutline_7.png) _Left_ : An automatically generated Mesh outline with a low **Outline Tolerance**. _Right_ : An automatically generated Mesh outline with a high **Outline Tolerance**.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-landing.html)
Custom outline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-outline-editor/edit-custom-outline.html)
Edit the custom outline
