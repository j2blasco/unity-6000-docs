* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.html

# BillboardAsset
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardAsset.html "Go to BillboardAsset Component in the Manual")
### Description
BillboardAsset describes how a billboard is rendered.
Billboards are a level-of-detail (LOD) method of drawing complicated 3D objects in a simpler manner if they are further away. Because the object is further away, there is often less requirement to draw the object at full detail due to its size on-screen and low likelihood of being a focal point in the Camera view. Instead, the object can be pre-rendered to a texture, and this texture used on a very simple Camera-facing Mesh of flat geometry (often simply a quadrilateral) known as a billboard. At great distances an object does not significantly change its orientation relative to the camera, so a billboard looks much like the object it represents from frame to frame, without having to be redrawn from the model. The BillboardAsset class allows the creation of billboards that are rendered from several directions, allowing a BillboardAsset to efficiently represent an object at low level of detail from any approximately-horizontal viewpoint.  
  
A BillboardAsset is usually created by importing SpeedTree assets. You can also create your own once you know how the billboard is described.  
  
SpeedTree billboard geometry is usually more complex than a plain quadrilateral. By using more vertices to cut out the empty part of the billboard image, rendering performance can potentially be improved due to the graphics system not having to draw as many redundant transparent pixels. You have access to the geometry data via BillboardAsset.vertices and BillboardAsset.indices.  
  
All vertices are considered in UV-space, because the geometry is due to be textured by the billboard images. UV vertices are easily expanded to 3D-space vertices by knowing the billboard's width, height, bottom, and what direction the billboard is currently facing. Assuming we have a billboard located at (0,0,0) looking at negative Z axis, the 3D-space coordinates are calculated as:  
  
_X_ = (_u_ - 0.5) * _width_  
_Y_ = _v_ * _height_ + _bottom_  
_Z_ = 0  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/Billboard_Geometry.png)  
_UV-space vertices are expanded to 3D-space vertices, with a SpeedTree billboard at (0, 0, 0) in 3D space._  
  
In order to display something similar to the real 3D mesh being billboarded, SpeedTree billboards select an appropriate image from several pre-rendered images according to the current view direction.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/Billboard_Images.png)  
_The eight SpeedTree billboard images are baked. The images are created by capturing the rendered image of the 3D tree at different view angles, evenly distributed around the Y-axis. The first image always starts at positive X axis direction (or 0° if you imagine a unit circle from above)._  
  
All images should be atlased together in one single texture. Each image is represented as a [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) of {_left u_ , _top v_ , _width in u_ , _height in v_} in the atlas. You have access to all the images via BillboardAsset.imageTexCoords. SpeedTree Modeler always exports a normal texture alongside the diffuse texture for even better approximation of the lighting, and it shares the same atlas layout with the diffuse texture.  
  
Once the BillboardAsset is constructed, use [BillboardRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardRenderer.html) to render it.
### Properties
Property | Description  
---|---  
[bottom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset-bottom.html) | Height of the billboard that is below ground.  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset-height.html) | Height of the billboard.  
[imageCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset-imageCount.html) | Number of pre-rendered images that can be switched when the billboard is viewed from different angles.  
[indexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset-indexCount.html) | Number of indices in the billboard mesh.  
[material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset-material.html) | The material used for rendering.  
[vertexCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset-vertexCount.html) | Number of vertices in the billboard mesh.  
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset-width.html) | Width of the billboard.  
### Constructors
Constructor | Description  
---|---  
[BillboardAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset-ctor.html) | Constructs a new BillboardAsset.  
### Public Methods
Method | Description  
---|---  
[GetImageTexCoords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.GetImageTexCoords.html) | Get the array of billboard image texture coordinate data.  
[GetIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.GetIndices.html) | Get the indices of the billboard mesh.  
[GetVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.GetVertices.html) | Get the vertices of the billboard mesh.  
[SetImageTexCoords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.SetImageTexCoords.html) | Set the array of billboard image texture coordinate data.  
[SetIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.SetIndices.html) | Set the indices of the billboard mesh.  
[SetVertices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.SetVertices.html) | Set the vertices of the billboard mesh.  
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
