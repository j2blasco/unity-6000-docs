* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-reference.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Textures reference](https://docs.unity3d.com/6000.0/Documentation/Manual/textures-reference.html)
  * 3D texture preview reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cubemap.html)
Cubemap texture Import Settings window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cursor.html)
Cursor texture Import Settings window reference
# 3D texture preview reference
There are three different 3D texture preview modes available:
  * [**Volume**](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-reference.html#volume)
  * [**Slice**](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-reference.html#slice)
  * [**SDF**](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D-reference.html#sdf)


Refer to [Texture Import Settings window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html) for information about other settings in the **Texture Import Settings** window.
## Volume
In **Volume** preview mode, Unity displays the 3D texture as a translucent cube. Select and drag the cube to rotate the preview.
![ ](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/3DTexture-volumetric.png) **Control** | **Description**  
---|---  
**Ramp** | Enable and disable color ramp so that Unity displays grayscale as color. If the image contains a lot of subtle details, enable **Ramp** to make the details easier to check.  
**Quality** | Set the sample per texture **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) count. Higher values result in a higher quality render.  
**Alpha** | Set the opacity of the preview. A value of 1 is fully opaque and a value of 0 is fully transparent. Adjust to view the inner pixels.  
## Slice
In **Slice** preview mode, Unity displays a 2D slice of each of the three axes of the 3D texture. Use the **X** , **Y** and **Z** sliders to select the slices to preview.
![ ](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/3DTexture-slice.png) **Control** | **Description**  
---|---  
**Ramp** | Enable and disable color ramp so that Unity displays grayscale as color. If the image contains a lot of subtle details, enable **Ramp** to make the details easier to check.  
**X** | Set the slice to view from the x-axis, in texture pixels.  
**Y** | Set the slice to view from the y-axis, in texture pixels.  
**Z** | Set the slice to view from the z-axis, in texture pixels.  
## SDF
In **SDF** preview mode, Unity displays the 3D texture as a signed distance field (SDF) in 3D space. This preview mode supports only non-directional signed distance fields. 
![ ](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/3DTexture-SDF.png) **Control** | **Description**  
---|---  
**Scale** | Set the value by which to multiply the ray step size. The ray step size is the distance between 2 neighboring pixels. Increase this value if Unity cuts off distant parts of the preview. Decrease this value if the 3D texture isn’t visible.  
**Offset** | The intensity that Unity uses to render the surface pixels. When this value is positive, Unity expands the rendered surface. When this value is negative, Unity renders empty space as a surface, and a surface as empty space.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cubemap.html)
Cubemap texture Import Settings window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cursor.html)
Cursor texture Import Settings window reference
