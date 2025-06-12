* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html

# Texture2D
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
### Description
Class that represents textures in C# code.
Use this class to create textures, or to modify existing [texture assets](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html).  
  
The [ImageConversion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.html) class provides extension methods to this class that handle image encoding functionality. For details on those methods, see the [ImageConversion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.html) documentation.  
  
Do not assume that the texture will be created and available in [Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html). All texture uploads are synchronized on the Main thread at [Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Start.html). Perform texture operations in [Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Start.html).
### Static Properties
Property | Description  
---|---  
[blackTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-blackTexture.html) | Gets a small Texture with all black pixels.  
[grayTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-grayTexture.html) | Gets a small Texture with all gray pixels.  
[linearGrayTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-linearGrayTexture.html) | Gets a small Texture with all gray pixels.  
[normalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-normalTexture.html) | Gets a small Texture with pixels that represent surface normal vectors at a neutral position.  
[redTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-redTexture.html) | Gets a small Texture with all red pixels.  
[whiteTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-whiteTexture.html) | Gets a small Texture with all white pixels.  
### Properties
Property | Description  
---|---  
[activeMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-activeMipmapLimit.html) | The number of high resolution mipmap levels from the texture that Unity doesn't upload to the GPU. (Read Only)  
[alphaIsTransparency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-alphaIsTransparency.html) | Indicates whether this texture was imported with TextureImporter.alphaIsTransparency enabled. This setting is available only in the Editor scripts. Note that changing this setting will have no effect; it must be enabled in TextureImporter instead.  
[calculatedMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-calculatedMipmapLevel.html) | The mipmap level calculated by the streaming system, which takes into account the streaming Cameras and the location of the objects containing this Texture. This is unaffected by requestedMipmapLevel or minimumMipmapLevel.  
[desiredMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-desiredMipmapLevel.html) | The mipmap level that the streaming system would load before memory budgets are applied.  
[format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-format.html) | The format of the pixel data in the texture (Read Only).  
[ignoreMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-ignoreMipmapLimit.html) | This property causes a texture to ignore all texture mipmap limit settings.  
[loadedMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-loadedMipmapLevel.html) | The mipmap level that is currently loaded by the streaming system.  
[loadingMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-loadingMipmapLevel.html) | The mipmap level that the mipmap streaming system is in the process of loading.  
[minimumMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-minimumMipmapLevel.html) | Restricts the mipmap streaming system to a minimum mip level for this Texture.  
[mipmapLimitGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-mipmapLimitGroup.html) | The name of the texture mipmap limit group that this texture is associated with. (Read Only)  
[requestedMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-requestedMipmapLevel.html) | The mipmap level to load.  
[streamingMipmaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-streamingMipmaps.html) | Determines whether mipmap streaming is enabled for this Texture.  
[streamingMipmapsPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-streamingMipmapsPriority.html) | Sets the relative priority for this Texture when reducing memory size to fit within the memory budget.  
[vtOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-vtOnly.html) | Returns true if the VTOnly checkbox was checked when the texture was imported; otherwise returns false. For additional information, see TextureImporter.vtOnly.  
### Constructors
Constructor | Description  
---|---  
[Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-ctor.html) | Create a new empty texture.  
### Public Methods
Method | Description  
---|---  
[Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) | Copies changes you've made in a CPU texture to the GPU.  
[ClearMinimumMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.ClearMinimumMipmapLevel.html) | Resets the minimumMipmapLevel field.  
[ClearRequestedMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.ClearRequestedMipmapLevel.html) | Resets the requestedMipmapLevel field.  
[Compress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Compress.html) | Compress texture at runtime to DXT/BCn or ETC formats.  
[CopyPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.CopyPixels.html) | Copies pixel data from another texture on the CPU.  
[GetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixel.html) | Gets the pixel color at coordinates (x, y).  
[GetPixelBilinear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixelBilinear.html) | Gets the filtered pixel color at the normalized coordinates (u, v).  
[GetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixelData.html) | Gets the raw data from a texture.  
[GetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixels.html) | Gets the pixel color data for a mipmap level as Color structs.  
[GetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixels32.html) | Gets the pixel color data for a mipmap level as Color32 structs.  
[GetRawTextureData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetRawTextureData.html) | Gets the raw data from a texture, as an array that points to memory.  
[IsRequestedMipmapLevelLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.IsRequestedMipmapLevelLoaded.html) | Checks to see whether the mipmap level set by requestedMipmapLevel has finished loading.  
[LoadRawTextureData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.LoadRawTextureData.html) | Sets the raw data of an entire texture in CPU memory.  
[PackTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.PackTextures.html) | Packs multiple Textures into a texture atlas.  
[ReadPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.ReadPixels.html) | Reads pixels from the current render target and writes them to a texture.  
[Reinitialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Reinitialize.html) | Reinitializes a Texture2D, making it possible for you to replace width, height, textureformat, and graphicsformat data for that texture.  
[SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixel.html) | Sets the pixel color at coordinates (x,y).  
[SetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixelData.html) | Sets the raw data of an entire mipmap level directly in CPU memory.  
[SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html) | Sets the pixel colors of an entire mipmap level.  
[SetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels32.html) | Sets the pixel colors of an entire mipmap level.  
[UpdateExternalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.UpdateExternalTexture.html) | Updates Unity texture to use different native texture object.  
### Static Methods
Method | Description  
---|---  
[CreateExternalTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.CreateExternalTexture.html) | Creates a Unity Texture out of an externally created native texture object.  
[GenerateAtlas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GenerateAtlas.html) | Packs a set of rectangles into a square atlas, with optional padding between rectangles.  
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
