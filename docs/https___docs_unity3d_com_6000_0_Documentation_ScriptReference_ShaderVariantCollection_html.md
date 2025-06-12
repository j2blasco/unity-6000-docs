* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.html

# ShaderVariantCollection
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
ShaderVariantCollection records which shader variants are actually used in each shader.
This is used for shader preloading ("warmup"), so that a game can make sure "actually required" shader variants are loaded at startup (or level load time), to avoid shader compilation related hiccups later on in the game.  
  
In Unity, many shaders internally have multiple "variants", to account for different light modes, lightmaps, shadows and so on. These variants are identified by a shader pass type, and a set of shader keywords. See [ShaderVariant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.ShaderVariant.html).  
  
Typical use of ShaderVariantCollection is to record the shader variants used during a play session from the editor (under Graphics Settings), save them out as an asset, and add to the list of preloaded shaders (again in Graphics Settings). Additionally, you could call [WarmUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.WarmUp.html) on a ShaderVariantCollection object manually.  
  
ShaderVariantCollection generally replaces the old [Shader.WarmupAllShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.WarmupAllShaders.html) function.
### Properties
Property | Description  
---|---  
[isWarmedUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection-isWarmedUp.html) | Is this ShaderVariantCollection already warmed up? (Read Only)  
[shaderCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection-shaderCount.html) | Number of shaders in this collection (Read Only).  
[variantCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection-variantCount.html) | Number of total variants in this collection (Read Only).  
[warmedUpVariantCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection-warmedUpVariantCount.html) | Number of total variants in this collection that are already warmed up (Read Only).  
### Constructors
Constructor | Description  
---|---  
[ShaderVariantCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection-ctor.html) | Create a new empty shader variant collection.  
### Public Methods
Method | Description  
---|---  
[Add](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.Add.html) | Adds a new shader variant to the collection.  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.Clear.html) | Remove all shader variants from the collection.  
[Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.Contains.html) | Checks if a shader variant is in the collection.  
[Remove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.Remove.html) | Removes shader variant from the collection.  
[WarmUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.WarmUp.html) | Prewarms all shader variants in this shader variant collection.  
[WarmUpProgressively](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.WarmUpProgressively.html) | Prewarms the given number of shader variants in this shader variant collection.  
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
