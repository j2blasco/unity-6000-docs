* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.html

# CubemapArray
class in UnityEngine
/
Inherits from:[Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CubemapArray.html "Go to CubemapArray Component in the Manual")
### Description
Class for handling Cubemap arrays.
Modern graphics APIs, such as D3D10.1 and later, OpenGL 4.0 and later, and Metal on macOS support cubemap arrays, which are arrays of cubemaps with same size and format. From the shader side, they are treated as a single resource, and sampling them needs an extra coordinate that indicates which array element to sample from.  
  
Typically cubemap arrays are useful for implementing efficient reflection probe, lighting and shadowing systems (all reflection/cookie/shadow cubemaps in a single array).  
  
Cubemap arrays do not have an import pipeline for them, and must be created from code, either at runtime or in editor scripts. Using [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html) is useful for fast copying of pixel data from regular [Cubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html) textures into elements of a cubemap array. From editor scripts, a common way of creating serialized cubemap array is to create it, fill with data (either via [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html) from regular cubemaps, or via [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.SetPixels.html) or [SetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.SetPixels32.html)) and save it as an asset via [AssetDatabase.CreateAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html).  
  
Note that not all platforms and GPUs support cubemap arrays. Use [SystemInfo.supportsCubemapArrayTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsCubemapArrayTextures.html) to check. Also, this class does not support CubemapArray creation with a Crunch compression [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html).
### Properties
Property | Description  
---|---  
[cubemapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray-cubemapCount.html) | Number of cubemaps in the array (Read Only).  
[format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray-format.html) | Texture format (Read Only).  
### Constructors
Constructor | Description  
---|---  
[CubemapArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray-ctor.html) | Create a new cubemap array.  
### Public Methods
Method | Description  
---|---  
[Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.Apply.html) | Copies changes you've made in a CPU texture to the GPU.  
[CopyPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.CopyPixels.html) | Copies pixel data from another texture on the CPU.  
[GetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.GetPixelData.html) | Gets the raw data from a texture.  
[GetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.GetPixels.html) | Gets the pixel color data for a mipmap level of a face of a slice as Color structs.  
[GetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.GetPixels32.html) | Gets the pixel color data for a mipmap level of a face of a slice as Color32 structs.  
[SetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.SetPixelData.html) | Sets the raw data of an entire mipmap level of a face directly in CPU memory.  
[SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.SetPixels.html) | Sets the pixel colors of an entire mipmap level of a face of a slice.  
[SetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.SetPixels32.html) | Sets the pixel colors of an entire mipmap level of a face of a slice.  
### Inherited Members
### Static Properties
Property | Description  
---|---  
[allowThreadedTextureCreation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-allowThreadedTextureCreation.html) | Allow Unity internals to perform Texture creation on any thread (rather than the dedicated render thread).  
[currentTextureMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-currentTextureMemory.html) | The amount of memory that all Textures in the scene use.  
[desiredTextureMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-desiredTextureMemory.html) | The total size of the Textures, in bytes, that Unity loads if there were no other constraints. Before Unity loads any Textures, it applies the memory budget which reduces the loaded Texture resolution if the Texture sizes exceed its value. The desiredTextureMemory value takes into account the mipmap levels that Unity has requested or that you have set manually.For example, if Unity does not load a Texture at full resolution because it is far away or its requested mipmap level is greater than 0, Unity reduces the desiredTextureMemory value to match the total memory needed.The desiredTextureMemory value can be greater than the Texture.targetTextureMemory value.   
[GenerateAllMips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.GenerateAllMips.html) | Can be used with Texture constructors that take a mip count to indicate that all mips should be generated. The value of this field is -1.  
[nonStreamingTextureCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-nonStreamingTextureCount.html) | The number of non-streaming Textures in the scene. This includes instances of Texture2D and CubeMap Textures. This does not include any other Texture types, or 2D and CubeMap Textures that Unity creates internally.  
[nonStreamingTextureMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-nonStreamingTextureMemory.html) | The amount of memory Unity allocates for non-streaming Textures in the scene. This only includes instances of Texture2D and CubeMap Textures. This does not include any other Texture types, or 2D and CubeMap Textures that Unity creates internally.  
[streamingMipmapUploadCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-streamingMipmapUploadCount.html) | How many times has a Texture been uploaded due to Texture mipmap streaming.  
[streamingRendererCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-streamingRendererCount.html) | Number of renderers registered with the Texture streaming system.  
[streamingTextureCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-streamingTextureCount.html) | Number of streaming Textures.  
[streamingTextureDiscardUnusedMips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-streamingTextureDiscardUnusedMips.html) | This property forces the streaming Texture system to discard all unused mipmaps instead of caching them until the Texture memory budget is exceeded. This is useful when you profile or write tests to keep a predictable set of Textures in memory.  
[streamingTextureForceLoadAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-streamingTextureForceLoadAll.html) | Force streaming Textures to load all mipmap levels.  
[streamingTextureLoadingCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-streamingTextureLoadingCount.html) | Number of streaming Textures with mipmaps currently loading.  
[streamingTexturePendingLoadCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-streamingTexturePendingLoadCount.html) | Number of streaming Textures with outstanding mipmaps to be loaded.  
[targetTextureMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-targetTextureMemory.html) | The total amount of Texture memory that Unity allocates to the Textures in the scene after it applies the memory budget and finishes loading Textures. `targetTextureMemory`also takes mipmap streaming settings into account. This value only includes instances of Texture2D and CubeMap Textures. This value does not include any other Texture types, or 2D and CubeMap Textures that Unity creates internally.  
[totalTextureMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-totalTextureMemory.html) | The total amount of Texture memory that Unity would use if it loads all Textures at mipmap level 0.This is a theoretical value that does not take into account any input from the streaming system or any other input, for example when you set the`Texture2D.requestedMipmapLevel` manually.To see a Texture memory value that takes inputs into account, use `desiredTextureMemory`.`totalTextureMemory` only includes instances of Texture2D and CubeMap Textures. This value does not include any other Texture types, or 2D and CubeMap Textures that Unity creates internally.  
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
[anisoLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-anisoLevel.html) | Defines the anisotropic filtering level of the Texture.  
[dimension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-dimension.html) | Dimensionality (type) of the Texture (Read Only).  
[filterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-filterMode.html) | Filtering mode of the Texture.  
[graphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-graphicsFormat.html) | Returns the GraphicsFormat format or color format of a Texture object.  
[graphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-graphicsTexture.html) |  GraphicsTexture that represents the texture resource uploaded to the graphics device (Read Only).  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-height.html) | Height of the Texture in pixels (Read Only).  
[imageContentsHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-imageContentsHash.html) | The hash value of the Texture.  
[isDataSRGB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isDataSRGB.html) | Returns true if the texture pixel data is in sRGB color space (Read Only).  
[isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) | Whether Unity stores an additional copy of this texture's pixel data in CPU-addressable memory.  
[mipMapBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipMapBias.html) | The mipmap bias of the Texture.  
[mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html) | How many mipmap levels are in this Texture (Read Only).  
[updateCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-updateCount.html) | This counter is incremented when the Texture is updated.  
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-width.html) | Width of the Texture in pixels (Read Only).  
[wrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-wrapMode.html) | Texture coordinate wrapping mode.  
[wrapModeU](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-wrapModeU.html) | Texture U coordinate wrapping mode.  
[wrapModeV](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-wrapModeV.html) | Texture V coordinate wrapping mode.  
[wrapModeW](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-wrapModeW.html) | Texture W coordinate wrapping mode for Texture3D.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
[GetNativeTexturePtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.GetNativeTexturePtr.html) | Retrieve a native (underlying graphics API) pointer to the Texture resource.  
[IncrementUpdateCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.IncrementUpdateCount.html) | Increment the update counter.  
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
[SetGlobalAnisotropicFilteringLimits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.SetGlobalAnisotropicFilteringLimits.html) | Sets Anisotropic limits.  
[SetStreamingTextureMaterialDebugProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.SetStreamingTextureMaterialDebugProperties.html) | This function sets mipmap streaming debug properties on all materials known by the mipmap streaming system.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
