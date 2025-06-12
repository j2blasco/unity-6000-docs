* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html

# SystemInfo
class in UnityEngine
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
Access system and hardware information.
Use this class to figure out capabilities of the underlying platform and hardware. For example, you can check which [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) formats are supported ([SupportsRenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsRenderTextureFormat.html)), how many CPU threads are available ([processorCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorCount.html)), and so on.
### Static Properties
Property | Description  
---|---  
[batteryLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-batteryLevel.html) | The current battery level (Read Only).  
[batteryStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-batteryStatus.html) | Returns the current status of the device's battery (Read Only).  
[computeSubGroupSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-computeSubGroupSize.html) | Size of the compute thread group that supports efficient memory sharing on the GPU (Read Only).  
[constantBufferOffsetAlignment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-constantBufferOffsetAlignment.html) | Minimum buffer offset (in bytes) when binding a constant buffer using Shader.SetConstantBuffer or Material.SetConstantBuffer.  
[copyTextureSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-copyTextureSupport.html) | Support for various Graphics.CopyTexture cases (Read Only).  
[deviceModel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceModel.html) | The model of the device (Read Only).  
[deviceName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceName.html) | The user defined name of the device (Read Only).  
[deviceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceType.html) | Returns the kind of device the application is running on (Read Only).  
[deviceUniqueIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-deviceUniqueIdentifier.html) | A unique device identifier. It's guaranteed to be unique for every device (Read Only).  
[foveatedRenderingCaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-foveatedRenderingCaps.html) | The foveated rendering technique supported on this platform.  
[graphicsDeviceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceID.html) | The identifier code of the graphics device (Read Only).  
[graphicsDeviceName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceName.html) | The name of the graphics device (Read Only).  
[graphicsDeviceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceType.html) | The graphics API type used by the graphics device (Read Only).  
[graphicsDeviceVendor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceVendor.html) | The vendor of the graphics device (Read Only).  
[graphicsDeviceVendorID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceVendorID.html) | The identifier code of the graphics device vendor (Read Only).  
[graphicsDeviceVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceVersion.html) | The graphics API type and driver version used by the graphics device (Read Only).  
[graphicsMemorySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsMemorySize.html) | Amount of video memory present (Read Only).  
[graphicsMultiThreaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsMultiThreaded.html) | Is graphics device using multi-threaded rendering (Read Only)?  
[graphicsShaderLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsShaderLevel.html) | Graphics device shader capability level (Read Only).  
[graphicsUVStartsAtTop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsUVStartsAtTop.html) | Returns true if the texture UV coordinate convention for this platform has Y starting at the top of the image.  
[hasDynamicUniformArrayIndexingInFragmentShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-hasDynamicUniformArrayIndexingInFragmentShaders.html) | Returns true when the GPU has native support for indexing uniform arrays in fragment shaders without restrictions.  
[hasHiddenSurfaceRemovalOnGPU](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-hasHiddenSurfaceRemovalOnGPU.html) | True if the GPU supports hidden surface removal.  
[hasMipMaxLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-hasMipMaxLevel.html) | Returns true if the GPU supports partial mipmap chains (Read Only).  
[hdrDisplaySupportFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-hdrDisplaySupportFlags.html) | Returns a bitwise combination of HDRDisplaySupportFlags describing the support for HDR displays on the system.  
[maxAnisotropyLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxAnisotropyLevel.html) | Returns the maximum anisotropic level for anisotropic filtering that is supported on the device.   
[maxComputeBufferInputsCompute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeBufferInputsCompute.html) | Determines how many compute buffers Unity supports simultaneously in a compute shader for reading. (Read Only)  
[maxComputeBufferInputsDomain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeBufferInputsDomain.html) | Determines how many compute buffers Unity supports simultaneously in a domain shader for reading. (Read Only)  
[maxComputeBufferInputsFragment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeBufferInputsFragment.html) | Determines how many compute buffers Unity supports simultaneously in a fragment shader for reading. (Read Only)  
[maxComputeBufferInputsGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeBufferInputsGeometry.html) | Determines how many compute buffers Unity supports simultaneously in a geometry shader for reading. (Read Only)  
[maxComputeBufferInputsHull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeBufferInputsHull.html) | Determines how many compute buffers Unity supports simultaneously in a hull shader for reading. (Read Only)  
[maxComputeBufferInputsVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeBufferInputsVertex.html) | Determines how many compute buffers Unity supports simultaneously in a vertex shader for reading. (Read Only)  
[maxComputeWorkGroupSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeWorkGroupSize.html) | The largest total number of invocations in a single local work group that can be dispatched to a compute shader (Read Only).  
[maxComputeWorkGroupSizeX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeWorkGroupSizeX.html) | The maximum number of work groups that a compute shader can use in X dimension (Read Only).  
[maxComputeWorkGroupSizeY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeWorkGroupSizeY.html) | The maximum number of work groups that a compute shader can use in Y dimension (Read Only).  
[maxComputeWorkGroupSizeZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxComputeWorkGroupSizeZ.html) | The maximum number of work groups that a compute shader can use in Z dimension (Read Only).  
[maxConstantBufferSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxConstantBufferSize.html) | The maximum size of a constant buffer binding (Read Only).  
[maxCubemapSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxCubemapSize.html) | Maximum cubemap texture size in pixels (Read Only).  
[maxGraphicsBufferSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxGraphicsBufferSize.html) | The maximum size of a graphics buffer (GraphicsBuffer, ComputeBuffer, vertex/index buffer, etc.) in bytes (Read Only).  
[maxTexture3DSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxTexture3DSize.html) | Maximum 3D texture size in pixels (Read Only).  
[maxTextureArraySlices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxTextureArraySlices.html) | Maximum number of slices in a Texture array (Read Only).  
[maxTextureSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxTextureSize.html) | Maximum texture size in pixels (Read Only).  
[npotSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-npotSupport.html) | What NPOT (non-power of two size) texture support does the GPU provide? (Read Only)  
[operatingSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-operatingSystem.html) | Operating system name with version (Read Only).  
[operatingSystemFamily](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-operatingSystemFamily.html) | Returns the operating system family the game is running on (Read Only).  
[processorCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorCount.html) | Number of processors present (Read Only).  
[processorFrequency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorFrequency.html) | The processor frequency of the device in MHz (Read Only).  
[processorManufacturer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorManufacturer.html) | Specifies the manufacturer name of the processor in the user's device (Read Only).  
[processorModel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorModel.html) | Specifies the model name of the processor in the user's device (Read Only).  
[processorType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-processorType.html) | Processor name (Read Only).  
[renderingThreadingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-renderingThreadingMode.html) | Application's actual rendering threading mode (Read Only).  
[supportedRandomWriteTargetCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportedRandomWriteTargetCount.html) | The maximum number of random write targets (UAV) that Unity supports simultaneously. (Read Only)  
[supportedRenderTargetCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportedRenderTargetCount.html) | How many simultaneous render targets (MRTs) are supported? (Read Only)  
[supports2DArrayTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supports2DArrayTextures.html) | Are 2D Array textures supported? (Read Only)  
[supports32bitsIndexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supports32bitsIndexBuffer.html) | Are 32-bit index buffers supported? (Read Only)  
[supports3DRenderTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supports3DRenderTextures.html) | Are 3D (volume) RenderTextures supported? (Read Only)  
[supports3DTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supports3DTextures.html) | Are 3D (volume) textures supported? (Read Only)  
[supportsAccelerometer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsAccelerometer.html) | Is an accelerometer available on the device?  
[supportsAnisotropicFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsAnisotropicFilter.html) | Returns true when anisotropic filtering is supported on the device.  
[supportsAsyncCompute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsAsyncCompute.html) | Returns true when the platform supports asynchronous compute queues and false if otherwise.  
[supportsAsyncGPUReadback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsAsyncGPUReadback.html) | Returns true if asynchronous readback of GPU data is available for this device and false otherwise.  
[supportsAudio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsAudio.html) | Is there an Audio device available for playback? (Read Only)  
[supportsCompressed3DTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsCompressed3DTextures.html) | Are compressed formats for 3D (volume) textures supported? (Read Only).  
[supportsComputeShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsComputeShaders.html) | Are compute shaders supported? (Read Only)  
[supportsConservativeRaster](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsConservativeRaster.html) | Is conservative rasterization supported? (Read Only)  
[supportsCubemapArrayTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsCubemapArrayTextures.html) | Are Cubemap Array textures supported? (Read Only)  
[supportsDepthFetchInRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsDepthFetchInRenderPass.html) | Indicates whether RenderPass can use its depth attachment as input. (Read Only)  
[supportsGeometryShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsGeometryShaders.html) | Are geometry shaders supported? (Read Only)  
[supportsGpuRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsGpuRecorder.html) | Specifies whether the current platform supports the GPU Recorder or not. (Read Only).  
[supportsGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsGraphicsFence.html) |  true if the platform supports GraphicsFences, otherwise false.  
[supportsGyroscope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsGyroscope.html) | Is a gyroscope available on the device?  
[supportsHardwareQuadTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsHardwareQuadTopology.html) | Does the hardware support quad topology? (Read Only)  
[supportsIndirectArgumentsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsIndirectArgumentsBuffer.html) | Returns true if the graphics system supports GPU draw calls with indirect argument buffers. (Read Only)  
[supportsIndirectDispatchRays](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsIndirectDispatchRays.html) | Returns true if the graphics system supports indirect ray tracing dispatch. (Read Only)  
[supportsInlineRayTracing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsInlineRayTracing.html) | Is inline ray tracing (ray query) supported? (Read Only)  
[supportsInstancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsInstancing.html) | Is GPU draw call instancing supported? (Read Only)  
[supportsLocationService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsLocationService.html) | Is the device capable of reporting its location?  
[supportsMipStreaming](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMipStreaming.html) | Is streaming of texture mip maps supported? (Read Only)  
[supportsMotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMotionVectors.html) | Whether motion vectors are supported on this platform.  
[supportsMultisampleAutoResolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMultisampleAutoResolve.html) | Returns true if multisampled textures are resolved automatically  
[supportsMultisampled2DArrayTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMultisampled2DArrayTextures.html) | Boolean that indicates whether multisampled texture arrays are supported (true if supported, false if not supported).  
[supportsMultisampledBackBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMultisampledBackBuffer.html) | A boolean property that indicates whether multi-sampled back buffer is supported (true if supported, false if not supported).  
[supportsMultisampledTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMultisampledTextures.html) | Returns a value of 1 or higher if multisampled textures are supported. (Read Only)  
[supportsMultisampleResolveDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMultisampleResolveDepth.html) | Returns true if the platform supports multisample resolve of depth textures.  
[supportsMultisampleResolveStencil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMultisampleResolveStencil.html) | Returns true if the platform supports multisample resolve of stencil textures. Otherwise, returns false.  
[supportsMultiview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsMultiview.html) | Boolean that indicates whether Multiview is supported (true if supported, false if not supported). (Read Only)  
[supportsParallelPSOCreation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsParallelPSOCreation.html) | Returns true if parallel PSO creation is available for this device and false otherwise.  
[supportsRawShadowDepthSampling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsRawShadowDepthSampling.html) | Is sampling raw depth from shadowmaps supported? (Read Only)  
[supportsRayTracing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsRayTracing.html) | Checks if any ray tracing features are supported by the current system configuration. (Read Only)  
[supportsRayTracingShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsRayTracingShaders.html) | Checks if ray tracing shaders are supported by the current system configuration. (Read Only)  
[supportsRenderTargetArrayIndexFromVertexShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsRenderTargetArrayIndexFromVertexShader.html) | Boolean that indicates if SV_RenderTargetArrayIndex can be used in a vertex shader (true if it can be used, false if not).  
[supportsSeparatedRenderTargetsBlend](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsSeparatedRenderTargetsBlend.html) | Returns true when the platform supports different blend modes when rendering to multiple render targets, or false otherwise.  
[supportsSetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsSetConstantBuffer.html) | Does the current renderer support binding constant buffers directly? (Read Only)  
[supportsShadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsShadows.html) | Are built-in shadows supported? (Read Only)  
[supportsSparseTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsSparseTextures.html) | Are sparse textures supported? (Read Only)  
[supportsStoreAndResolveAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsStoreAndResolveAction.html) | This property is true if the graphics API of the target build platform takes RenderBufferStoreAction.StoreAndResolve into account, false if otherwise.  
[supportsTessellationShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsTessellationShaders.html) | Are tessellation shaders supported? (Read Only)  
[supportsTextureWrapMirrorOnce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsTextureWrapMirrorOnce.html) | Returns a value of 1 or higher if the 'Mirror Once' texture wrap mode is supported. (Read Only)  
[supportsVibration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsVibration.html) | Is the device capable of providing the user haptic feedback by vibration?  
[systemMemorySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-systemMemorySize.html) | Amount of system memory present (Read Only).  
[unsupportedIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-unsupportedIdentifier.html) | Value returned by SystemInfo string properties which are not supported on the current platform.  
[usesLoadStoreActions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-usesLoadStoreActions.html) | True if the Graphics API takes RenderBufferLoadAction and RenderBufferStoreAction into account, false if otherwise.  
[usesReversedZBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-usesReversedZBuffer.html) | This property is true if the current platform uses a reversed depth buffer (where values range from 1 at the near plane and 0 at far plane), and false if the depth buffer is normal (0 is near, 1 is far). (Read Only)  
### Static Methods
Method | Description  
---|---  
[GetCompatibleFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.GetCompatibleFormat.html) | Returns a format supported by the platform for the specified usage.  
[GetGraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.GetGraphicsFormat.html) | Returns the platform-specific GraphicsFormat that is associated with the DefaultFormat.  
[GetRenderTextureSupportedMSAASampleCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.GetRenderTextureSupportedMSAASampleCount.html) | Checks if the target platform supports the MSAA samples count in the RenderTextureDescriptor argument.  
[IsFormatSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.IsFormatSupported.html) | Verifies that the specified graphics format is supported for the specified usage.  
[SupportsBlendingOnRenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsBlendingOnRenderTextureFormat.html) | Is blending supported on render texture format?  
[SupportsRandomWriteOnRenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsRandomWriteOnRenderTextureFormat.html) | Tests if a RenderTextureFormat can be used with RenderTexture.enableRandomWrite.  
[SupportsRenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsRenderTextureFormat.html) | Is render texture format supported?  
[SupportsTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsTextureFormat.html) | Is texture format supported on this device?  
[SupportsVertexAttributeFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsVertexAttributeFormat.html) | Indicates whether the given combination of a vertex attribute format and dimension is supported on this device.  
* * *
