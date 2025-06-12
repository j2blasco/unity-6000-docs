* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html

# Sprite
class in UnityEngine
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Represents a Sprite object for use in 2D gameplay.
_Sprites_ are 2D graphic objects used for characters, props, projectiles and other elements of 2D gameplay. The graphics are obtained from bitmap images - [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html). The Sprite class primarily identifies the section of the image that should be used for a specific Sprite. This information can then be used by a SpriteRenderer component on a GameObject to actually display the graphic.  
  
Additional resources: [SpriteRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) class.
### Properties
Property | Description  
---|---  
[associatedAlphaSplitTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-associatedAlphaSplitTexture.html) | Returns the Texture that contains the alpha channel from the source Texture. Unity generates this Texture under the hood for Sprites that have alpha in the source, and need to be compressed using techniques like ETC1.Returns NULL if there is no associated alpha Texture for the source Sprite. This is the case if the Sprite has not been setup to use ETC1 compression.   
[border](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-border.html) | Returns the border sizes of the Sprite.   
[bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-bounds.html) |  Bounds of the Sprite, specified by its center and extents in world space units.  
[packed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-packed.html) | Returns true if this Sprite is packed in an atlas.  
[packingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-packingMode.html) | If Sprite is packed (see Sprite.packed), returns its SpritePackingMode.  
[packingRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-packingRotation.html) | If Sprite is packed (see Sprite.packed), returns its SpritePackingRotation.  
[pivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-pivot.html) | Location of the Sprite's pivot point in the Rect on the original Texture, specified in pixels.  
[pixelsPerUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-pixelsPerUnit.html) | The number of pixels in the Sprite that correspond to one unit in world space. (Read Only)   
[rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-rect.html) | Location of the Sprite on the original Texture, specified in pixels.  
[spriteAtlasTextureScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-spriteAtlasTextureScale.html) | The Variant scale of Texture used by the Sprite. This is useful to check when a Variant SpriteAtlas is being used by Sprites.   
[texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-texture.html) | Get the reference to the used Texture. If packed this will point to the atlas, if not packed will point to the source Sprite.   
[textureRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-textureRect.html) | Get the rectangle this Sprite uses on its Texture. Raises an exception if this Sprite is tightly packed in an atlas.   
[textureRectOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-textureRectOffset.html) | Gets the offset of the rectangle this Sprite uses on its Texture to the original Sprite bounds. If Sprite mesh type is FullRect, offset is zero.   
[triangles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-triangles.html) | Returns a copy of the array containing Sprite mesh triangles.   
[uv](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-uv.html) | The base Texture coordinates of the Sprite mesh.   
[vertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite-vertices.html) | Returns a copy of the array containing Sprite mesh vertex positions.   
### Public Methods
Method | Description  
---|---  
[AddScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.AddScriptableObject.html) | Adds a ScriptableObject reference to the sprite.   
[GetPhysicsShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.GetPhysicsShape.html) | Gets a physics shape from the Sprite by its index.  
[GetPhysicsShapeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.GetPhysicsShapeCount.html) | The number of physics shapes for the Sprite.  
[GetPhysicsShapePointCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.GetPhysicsShapePointCount.html) | Retrieves the number of points in the selected physics shape for the sprite.   
[GetScriptableObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.GetScriptableObjects.html) | Retrieves an array of ScriptableObject referenced by the sprite.   
[GetScriptableObjectsCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.GetScriptableObjectsCount.html) | Gets the number of ScriptableObject that the sprite references.   
[GetSecondaryTextureCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.GetSecondaryTextureCount.html) | Gets the number of Secondary Textures that the Sprite is using.  
[GetSecondaryTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.GetSecondaryTextures.html) | Retrieves an array of SecondarySpriteTexture used by the Sprite.  
[OverrideGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.OverrideGeometry.html) | Sets up new Sprite geometry.  
[OverridePhysicsShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.OverridePhysicsShape.html) | Sets up a new Sprite physics shape.  
[RemoveScriptableObjectAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.RemoveScriptableObjectAt.html) | Removes the ScriptableObject reference from the sprite.   
[SetScriptableObjectAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.SetScriptableObjectAt.html) | Replace the ScriptableObject reference from the sprite.  
### Static Methods
Method | Description  
---|---  
[Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.Create.html) | Create a new Sprite object.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
