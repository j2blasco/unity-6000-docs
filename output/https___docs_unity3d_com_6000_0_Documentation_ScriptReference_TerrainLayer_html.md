* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer.html

# TerrainLayer
class in UnityEngine
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
/
Implemented in:[UnityEngine.TerrainModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.TerrainModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TerrainLayer.html "Go to TerrainLayer Component in the Manual")
### Description
Description of a terrain layer.
### Properties
Property | Description  
---|---  
[diffuseRemapMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-diffuseRemapMax.html) | A Vector4 value specifying the maximum RGBA value that the diffuse texture maps to when the value of the channel is 1.  
[diffuseRemapMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-diffuseRemapMin.html) | A Vector4 value specifying the minimum RGBA value that the diffuse texture maps to when the value of the channel is 0.  
[diffuseTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-diffuseTexture.html) | The diffuse texture used by the terrain layer.  
[maskMapRemapMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-maskMapRemapMax.html) | A Vector4 value specifying the maximum RGBA value that the mask map texture maps to when the value of the channel is 1.  
[maskMapRemapMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-maskMapRemapMin.html) | A Vector4 value specifying the minimum RGBA value that the mask map texture maps to when the value of the channel is 0.  
[maskMapTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-maskMapTexture.html) | The mask map texture used by the terrain layer.  
[metallic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-metallic.html) | Metallic factor used by the terrain layer.  
[normalMapTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-normalMapTexture.html) | Normal map texture used by the terrain layer.  
[normalScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-normalScale.html) | A float value that scales the normal vector. The minimum value is 0, the maximum value is 1.  
[smoothness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-smoothness.html) | Smoothness of the specular reflection.  
[smoothnessSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-smoothnessSource.html) | Choose the source for smoothness value.  
[specular](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-specular.html) | Specular color.  
[tileOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-tileOffset.html) | UV tiling offset.  
[tileSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayer-tileSize.html) | UV Tiling size.  
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
