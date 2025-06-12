* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.html

# CustomRenderTexture
class in UnityEngine
/
Inherits from:[RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture.html "Go to CustomRenderTexture Component in the Manual")
### Description
Custom Render Textures are an extension to Render Textures that allow you to render directly to the Texture using a Shader.
Custom Render Textures are an extension to Render Textures that allow you to update a texture with a Shader, and then use it in a regular Material. This is useful for implementing all kinds of complex simulations, for instance: water caustics, ripple simulations for rain effects, or splatting liquids against a wall. Also provided is a scripting and Shader framework to help with more complicated configurations like partial or multi-pass updates, and varying update frequency.
### Properties
Property | Description  
---|---  
[cubemapFaceMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-cubemapFaceMask.html) | The bit field that you can use to enable or disable update on each of the cubemap faces. The bit order from least to most significant bit is as follows: +X, -X, +Y, -Y, +Z, -Z.  
[doubleBuffered](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-doubleBuffered.html) | When this parameter is set to true, Unity double-buffers the Custom Render Texture so that you can access it during its own update.  
[initializationColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-initializationColor.html) | The color that Unity uses to initialize a Custom Render Texture. Unity ignores this parameter if an initializationMaterial is set.  
[initializationMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-initializationMaterial.html) | The Material that Unity uses to initialize a Custom Render Texture. Initialization texture and color are ignored if you have set this parameter.  
[initializationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-initializationMode.html) | Determine how Unity initializes a texture.  
[initializationSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-initializationSource.html) | Determine if Unity initializes the Custom Render Texture with a Texture and a Color or a Material.  
[initializationTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-initializationTexture.html) | The Texture that Unity uses to initialize a Custom Render Texture, multiplied by the initialization color. Unity ignores this parameter if an initializationMaterial is set.  
[material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-material.html) | The Material that Unity uses to initialize the content of a Custom Render Texture.  
[shaderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-shaderPass.html) | The Shader Pass Unity uses to update the Custom Render Texture.  
[updateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-updateMode.html) | Determine how Unity updates the Custom Render Texture.  
[updatePeriod](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-updatePeriod.html) | The period in seconds that Unity updates real-time Custom Render Textures. A value of 0.0 means Unity updates real-time Custom Render Textures every frame.  
[updateZoneSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-updateZoneSpace.html) | The space in which Unity expresses update zones. You can set this to Normalized or Pixel space.  
[wrapUpdateZones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-wrapUpdateZones.html) | When this parameter is set to true, Unity wraps Update zones around the border of the Custom Render Texture. Otherwise, Unity clamps Update zones at the border of the Custom Render Texture.  
### Constructors
Constructor | Description  
---|---  
[CustomRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture-ctor.html) | Create a new Custom Render Texture.  
### Public Methods
Method | Description  
---|---  
[ClearUpdateZones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.ClearUpdateZones.html) | Clear all Update Zones.  
[EnsureDoubleBufferConsistency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.EnsureDoubleBufferConsistency.html) | Updates the internal Render Texture that a Custom Render Texture uses for double buffering, so that it matches the size and format of the Custom Render Texture.  
[GetDoubleBufferRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.GetDoubleBufferRenderTexture.html) | Gets the Render Texture that this Custom Render Texture uses for double buffering.  
[GetUpdateZones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.GetUpdateZones.html) | Returns the list of Update Zones.  
[Initialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.Initialize.html) | Initializes the Custom Render Texture at the start of the next frame. Unity calls /Initialise()/ before /CustomRenderTexture.Update/.  
[SetUpdateZones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.SetUpdateZones.html) | Setup the list of Update Zones for the Custom Render Texture.  
[Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.Update.html) | Triggers an update of the Custom Render Texture.  
### Inherited Members
### Static Properties
Property | Description  
---|---  
[active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html) | Currently active render texture.  
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
[antiAliasing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-antiAliasing.html) | The antialiasing level for the RenderTexture.  
[autoGenerateMips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-autoGenerateMips.html) | Mipmap levels are generated automatically when this flag is set.  
[bindTextureMS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-bindTextureMS.html) | If true and antiAliasing is greater than 1, the render texture will not be resolved by default. Use this if the render texture needs to be bound as a multisampled texture in a shader.  
[colorBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-colorBuffer.html) | Color buffer of the render texture (Read Only).  
[depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depth.html) | The precision of the render texture's depth buffer in bits (0, 16, 24 and 32 are supported).  
[depthBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depthBuffer.html) | Depth/stencil buffer of the render texture (Read Only).  
[depthStencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depthStencilFormat.html) | The format of the depth/stencil buffer.  
[descriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-descriptor.html) | This struct contains all the information required to create a RenderTexture. It can be copied, cached, and reused to easily create RenderTextures that all share the same properties.  
[dimension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-dimension.html) | Dimensionality (type) of the render texture.  
[enableRandomWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-enableRandomWrite.html) | Enable random access write into this render texture on Shader Model 5.0 level shaders.  
[graphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-graphicsFormat.html) | The color format of the render texture. You can set the color format to None to achieve depth-only rendering.  
[height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-height.html) | The height of the render texture in pixels.  
[memorylessMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-memorylessMode.html) | The render texture memoryless mode property.  
[sRGB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-sRGB.html) | Does this render texture use sRGB read/write conversions? (Read Only).  
[stencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-stencilFormat.html) | The format of the stencil data that you can encapsulate within a RenderTexture.Specifying this property creates a stencil element for the RenderTexture and sets its format. This allows for stencil data to be bound as a Texture to all shader types for the platforms that support it. This property does not specify the format of the stencil buffer, which is constrained by the depth buffer format specified in RenderTexture.depth.Currently, most platforms only support R8_UInt (DirectX11, DirectX12).  
[useDynamicScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-useDynamicScale.html) | When this flag is set to true, render texture is set to be used by the Dynamic Resolution system.  
[useDynamicScaleExplicit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-useDynamicScaleExplicit.html) | When this flag is set to true, render texture is set to be used by the Dynamic Resolution system. Scale is applied with an explicit call to ApplyDynamicScale  
[useMipMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-useMipMap.html) | Render texture has mipmaps when this flag is set.  
[volumeDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-volumeDepth.html) | Volume extent of a 3D render texture or number of slices of array texture.  
[vrUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-vrUsage.html) | If this RenderTexture is a VR eye texture used in stereoscopic rendering, this property decides what special rendering occurs, if any.  
[width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-width.html) | The width of the render texture in pixels.  
[anisoLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-anisoLevel.html) | Defines the anisotropic filtering level of the Texture.  
[filterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-filterMode.html) | Filtering mode of the Texture.  
[graphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-graphicsTexture.html) |  GraphicsTexture that represents the texture resource uploaded to the graphics device (Read Only).  
[imageContentsHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-imageContentsHash.html) | The hash value of the Texture.  
[isDataSRGB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isDataSRGB.html) | Returns true if the texture pixel data is in sRGB color space (Read Only).  
[isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) | Whether Unity stores an additional copy of this texture's pixel data in CPU-addressable memory.  
[mipMapBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipMapBias.html) | The mipmap bias of the Texture.  
[mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html) | How many mipmap levels are in this Texture (Read Only).  
[updateCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-updateCount.html) | This counter is incremented when the Texture is updated.  
[wrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-wrapMode.html) | Texture coordinate wrapping mode.  
[wrapModeU](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-wrapModeU.html) | Texture U coordinate wrapping mode.  
[wrapModeV](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-wrapModeV.html) | Texture V coordinate wrapping mode.  
[wrapModeW](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-wrapModeW.html) | Texture W coordinate wrapping mode for Texture3D.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
[ApplyDynamicScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.ApplyDynamicScale.html) | Applies the Dynamic Resolution system scale.  
[ConvertToEquirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.ConvertToEquirect.html) | Converts the render texture to equirectangular format (both stereoscopic or monoscopic equirect). The left eye will occupy the top half and the right eye will occupy the bottom. The monoscopic version will occupy the whole texture. Texture dimension must be of type TextureDimension.Cube.  
[Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.Create.html) | Actually creates the RenderTexture.  
[DiscardContents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.DiscardContents.html) | Hint the GPU driver that the contents of the RenderTexture will not be used.  
[GenerateMips](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.GenerateMips.html) | Generate mipmap levels of a render texture.  
[GetNativeDepthBufferPtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.GetNativeDepthBufferPtr.html) | Retrieve a native (underlying graphics API) pointer to the depth buffer resource.  
[IsCreated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.IsCreated.html) | Is the render texture actually created?  
[Release](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.Release.html) | Releases the RenderTexture.  
[ResolveAntiAliasedSurface](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.ResolveAntiAliasedSurface.html) | Force an antialiased render texture to be resolved.  
[SetGlobalShaderProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.SetGlobalShaderProperty.html) | Assigns this RenderTexture as a global shader property named propertyName.  
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
[GetTemporary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.GetTemporary.html) | Allocate a temporary render texture.  
[ReleaseTemporary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.ReleaseTemporary.html) | Release a temporary texture allocated with GetTemporary.  
[SupportsStencil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.SupportsStencil.html) | Does a RenderTexture have stencil buffer?  
[SetGlobalAnisotropicFilteringLimits](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.SetGlobalAnisotropicFilteringLimits.html) | Sets Anisotropic limits.  
[SetStreamingTextureMaterialDebugProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.SetStreamingTextureMaterialDebugProperties.html) | This function sets mipmap streaming debug properties on all materials known by the mipmap streaming system.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
