* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/custom-physics-shape-editor-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Sprite editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html)
  * [Custom physics shape](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/custom-physics-shape-landing.html)
  * Custom physics shape editor reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/update-shape-collider-2d-meshes.html)
Update the shape of the collider 2D meshes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/secondary-texture/secondary-texture-landing.html)
Sprite editor secondary textures
# Custom physics shape editor reference
Property | Function  
---|---  
**Snap** | Snap control points to the nearest **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel).  
**Outline Tolerance** | Use this slider to control how tightly and accurately the generated outline follows the outline of the **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) texture. At the minimum value (0), the Sprite Editor generates a basic outline around the Sprite. At the maximum value (1), the Sprite Editor generates an outline that follows the outline of the Sprite as closely as possible.  
**Generate** | When you click this button, Unity automatically creates a physics shape outline based on the **Outline Tolerance** value you set.  
**Copy** | After you have generated or set up a custom physics shape, click this **Copy** button to duplicate the custom physics shape. Leaving the Custom Physics Shape module or closing the Sprite Editor removes the copied physics shape from memory.  
**Paste** | Use this button to paste a copied physics shape to the currently selected Sprite. If you have not used the **Copy** function to copy a physics shape, this button is not available. To **Paste** a copied custom physics shape to another Sprite, in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow) select the Sprite while the Custom Physics Shape editor window is open. Then click the **Paste** button to paste the copied physics shape to the new Sprite. When you paste the physics shape, if a point in the physics shape is larger than the Sprite’s frame, Unity clamps the point to be inside the Sprite’s frame.  
**Paste All** | Use this button to paste a copied physics shape to all sprites in the Sprite Editor window, regardless of selection. If you have not used the **Copy** function to copy a physics shape, this button is not available. Use this function to apply the same physics shape to multiple sprites in the same Texture (such as when a Texture has its [Sprite Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-sprite.html) set to ‘Multiple’). When you paste the physics shape, if a point in the physics shape exceeds the Sprite’s frame, Unity clamps the point to be inside that Sprite’s frame.  
**Revert** | Undoes any unsaved recent changes made in the editor window. To save changes, click **Apply** first.  
**Apply** | Select this button to save all changes made in the editor window.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/update-shape-collider-2d-meshes.html)
Update the shape of the collider 2D meshes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/secondary-texture/secondary-texture-landing.html)
Sprite editor secondary textures
