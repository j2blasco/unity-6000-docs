* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-adding-a-device.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [Device Simulator](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator.html)
  * Adding a device


[](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-simulated-classes.html)
Simulated classes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-plugins.html)
Extending the device simulator
# Adding a device
To add a new device to the Device Simulator, you create a device definition and a device overlay.
A device definition is a text file with the `.device` extension in your Unity project. It contains JSON that describes the properties of a device.
A device overlay is an image that contains the border of the device screen, together with notches, punchouts, and any other additions to the screen rectangle. You can optionally use it with a device definition to visualize how hardware elements obstruct the device screen, and to determine when touch inputs fail as a result.
## Creating a device definition
A device definition is a JSON file that represents the device. It has both required properties and some optional properties. If a device definition file contains any errors, the errors appear in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) when you select the file.
### Schema
**Property** | **Required** | **Description**  
---|---|---  
**friendlyName** | Yes | The name to display in the UI for this device.  
**version** | Yes | Indicates the version of the device definition file. Currently, the version is `1`.  
**screens** | Yes | A list of objects that each describe a screen to simulate the device for. This must contain at least one screen. For information about the schema of each screen object, see [screen](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-adding-a-device.html#screen).  
**systemInfo** | Yes | An object that describes the capabilities of the device. The values in this object map to [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html). For information about the schema of the systemInfo object, see [systemInfo](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-adding-a-device.html#systeminfo).  
#### screen
**Property** | **Required** | **Description**  
---|---|---  
**width** | Yes | The width, in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel), of the screen.  
**height** | Yes | The height, in pixels, of the screen.  
**navigationBarHeight** | No | The height, in pixels, of the on-screen Android navigation bar that appears on some devices when not in fullscreen.  
**dpi** | Yes | The dpi of the screen.  
**orientations** | No | A list of objects that each describe an orientation the screen can simulate. If you don’t set a value for this property, the screen supports all orientations. For information about the schema of each orientation object, see [orientation](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-adding-a-device.html#orientation).  
**presentation** | No | An object that describes the device overlay. For information about the schema of this object, see [presentation](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-adding-a-device.html#presentation).  
#### orientation
**Properties** | **Required** | **Description**  
---|---|---  
**orientation** | Yes | The screen orientation. The value of this property is a number that maps to the [ScreenOrientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.html) enum.  
**safeArea** | No | A [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) that determines the safe area of the screen. If you don’t set a value for this property, the simulator assumes the entire screen is safe.  
**cutouts** | No | A list of [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)s that specify areas of the screen that aren’t functional for displaying content.  
#### presentation
**Property** | **Required** | **Description**  
---|---|---  
**overlayPath** | No | A relative path from the device definition file to an image to use as the device overlay.  
**borderSize** | No | The distance, in pixels, from the overlay to where the screen begins.  
#### systeminfo
The properties in this object describe the capabilities and system information of the device. Since they describe the system information, many of them map to properties in [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo.html).
**Property** | **Required** | **Description**  
---|---|---  
**deviceModel** | No | See [Device.SystemInfo.deviceModel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-deviceModel.html).  
**deviceType** | No | See [Device.SystemInfo.deviceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-deviceType.html).  
**operatingSystem** | Yes | See [Device.SystemInfo.operatingSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-operatingSystem.html).  
**operatingSystemFamily** | No | See [Device.SystemInfo.operatingSystemFamily](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-operatingSystemFamily.html).  
**processorCount** | No | See [Device.SystemInfo.processorCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-processorCount.html).  
**processorFrequency** | No | See [Device.SystemInfo.processorFrequency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-processorFrequency.html).  
**processorType** | No | See [Device.SystemInfo.processorType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-processorType.html).  
**supportsAccelerometer** | No | See [Device.SystemInfo.supportsAccelerometer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsAccelerometer.html).  
**supportsAudio** | No | See [Device.SystemInfo.supportsAudio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsAudio.html).  
**supportsGyroscope** | No | See [Device.SystemInfo.supportsGyroscope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsGyroscope.html).  
**supportsLocationService** | No | See [Device.SystemInfo.supportsLocationService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsLocationService.html).  
**supportsVibration** | No | See [Device.SystemInfo.supportsVibration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsVibration.html).  
**systemMemorySize** | No | See [Device.SystemInfo.systemMemorySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-systemMemorySize.html).  
**unsupportedIdentifier** | No | See [Device.SystemInfo.unsupportedIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-unsupportedIdentifier.html).  
**graphicsDependentData** | No | A list of objects that each describe graphics APIs that the device supports. For information about the schema of each object, see [graphicsDependentData](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-adding-a-device.html#graphicsdependentdata).  
#### graphicsDependentData
The properties in the object describe a graphics API that the device supports.
**Property** | **Required** | **Description**  
---|---|---  
**graphicsDeviceType** | Yes | See [Device.SystemInfo.graphicsDeviceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-graphicsDeviceType.html).  
**graphicsMemorySize** | No | See [Device.SystemInfo.graphicsMemorySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-graphicsMemorySize.html).  
**graphicsDeviceName** | No | See [Device.SystemInfo.graphicsDeviceName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-graphicsDeviceName.html).  
**graphicsDeviceVendor** | No | See [Device.SystemInfo.graphicsDeviceVendor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-graphicsDeviceVendor.html).  
**graphicsDeviceID** | No | See [Device.SystemInfo.graphicsDeviceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-graphicsDeviceID.html).  
**graphicsDeviceVendorID** | No | See [Device.SystemInfo.graphicsDeviceVendorID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-graphicsDeviceVendorID.html).  
**graphicsUVStartsAtTop** | No | See [Device.SystemInfo.graphicsUVStartsAtTop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-graphicsUVStartsAtTop.html).  
**graphicsDeviceVersion** | No | See [Device.SystemInfo.graphicsDeviceVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-graphicsDeviceVersion.html).  
**graphicsShaderLevel** | No | See [Device.SystemInfo.graphicsShaderLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-graphicsShaderLevel.html).  
**graphicsMultiThreaded** | No | See [Device.SystemInfo.graphicsMultiThreaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-graphicsMultiThreaded.html).  
**renderingThreadingMode** | No | See [Device.SystemInfo.renderingThreadingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-renderingThreadingMode.html).  
**hasHiddenSurfaceRemovalOnGPU** | No | See [Device.SystemInfo.hasHiddenSurfaceRemovalOnGPU](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-hasHiddenSurfaceRemovalOnGPU.html).  
**hasDynamicUniformArrayIndexingInFragmentShaders** | No | See [Device.SystemInfo.hasDynamicUniformArrayIndexingInFragmentShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-hasDynamicUniformArrayIndexingInFragmentShaders.html).  
**supportsShadows** | No | See [Device.SystemInfo.supportsShadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsShadows.html).  
**supportsRawShadowDepthSampling** | No | See [Device.SystemInfo.supportsRawShadowDepthSampling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsRawShadowDepthSampling.html).  
**supportsMotionVectors** | No | See [Device.SystemInfo.supportsMotionVectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsMotionVectors.html).  
**supports3DTextures** | No | See [Device.SystemInfo.supports3DTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supports3DTextures.html).  
**supports2DArrayTextures** | No | See [Device.SystemInfo.supports2DArrayTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supports2DArrayTextures.html).  
**supports3DRenderTextures** | No | See [Device.SystemInfo.supports3DRenderTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supports3DRenderTextures.html).  
**supportsCubemapArrayTextures** | No | See [Device.SystemInfo.supportsCubemapArrayTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsCubemapArrayTextures.html).  
**copyTextureSupport** | No | See [Device.SystemInfo.copyTextureSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-copyTextureSupport.html).  
**supportsComputeShaders** | No | See [Device.SystemInfo.supportsComputeShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsComputeShaders.html).  
**supportsGeometryShaders** | No | See [Device.SystemInfo.supportsGeometryShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsGeometryShaders.html).  
**supportsTessellationShaders** | No | See [Device.SystemInfo.supportsTessellationShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsTessellationShaders.html).  
**supportsInstancing** | No | See [Device.SystemInfo.supportsInstancing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsInstancing.html).  
**supportsHardwareQuadTopology** | No | See [Device.SystemInfo.supportsHardwareQuadTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsHardwareQuadTopology.html).  
**supports32bitsIndexBuffer** | No | See [Device.SystemInfo.supports32bitsIndexBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supports32bitsIndexBuffer.html).  
**supportsSparseTextures** | No | See [Device.SystemInfo.supportsSparseTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsSparseTextures.html).  
**supportedRenderTargetCount** | No | See [Device.SystemInfo.supportedRenderTargetCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportedRenderTargetCount.html).  
**supportsSeparatedRenderTargetsBlend** | No | See [Device.SystemInfo.supportsSeparatedRenderTargetsBlend](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsSeparatedRenderTargetsBlend.html).  
**supportedRandomWriteTargetCount** | No | See [Device.SystemInfo.supportedRandomWriteTargetCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportedRandomWriteTargetCount.html).  
**supportsMultisampledTextures** | No | See [Device.SystemInfo.supportsMultisampledTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsMultisampledTextures.html).  
**supportsMultisampleAutoResolve** | No | See [Device.SystemInfo.supportsMultisampleAutoResolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsMultisampleAutoResolve.html).  
**supportsTextureWrapMirrorOnce** | No | See [Device.SystemInfo.supportsTextureWrapMirrorOnce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsTextureWrapMirrorOnce.html).  
**usesReversedZBuffer** | No | See [Device.SystemInfo.usesReversedZBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-usesReversedZBuffer.html).  
**npotSupport** | No | See [Device.SystemInfo.npotSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-npotSupport.html).  
**maxTextureSize** | No | See [Device.SystemInfo.maxTextureSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-maxTextureSize.html).  
**maxCubemapSize** | No | See [Device.SystemInfo.maxCubemapSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-maxCubemapSize.html).  
**maxComputeBufferInputsVertex** | No | See [Device.SystemInfo.maxComputeBufferInputsVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-maxComputeBufferInputsVertex.html).  
**maxComputeBufferInputsFragment** | No | See [Device.SystemInfo.maxComputeBufferInputsFragment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-maxComputeBufferInputsFragment.html).  
**maxComputeBufferInputsGeometry** | No | See [Device.SystemInfo.maxComputeBufferInputsGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-maxComputeBufferInputsGeometry.html).  
**maxComputeBufferInputsDomain** | No | See [Device.SystemInfo.maxComputeBufferInputsDomain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-maxComputeBufferInputsDomain.html).  
**maxComputeBufferInputsHull** | No | See [Device.SystemInfo.maxComputeBufferInputsHull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-maxComputeBufferInputsHull.html).  
**maxComputeBufferInputsCompute** | No | See [Device.SystemInfo.maxComputeBufferInputsCompute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-maxComputeBufferInputsCompute.html).  
**maxComputeWorkGroupSize** | No | See [Device.SystemInfo.maxComputeWorkGroupSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-maxComputeWorkGroupSize.html).  
**maxComputeWorkGroupSizeX** | No | See [Device.SystemInfo.maxComputeWorkGroupSizeX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-maxComputeWorkGroupSizeX.html).  
**maxComputeWorkGroupSizeY** | No | See [Device.SystemInfo.maxComputeWorkGroupSizeY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-maxComputeWorkGroupSizeY.html).  
**maxComputeWorkGroupSizeZ** | No | See [Device.SystemInfo.maxComputeWorkGroupSizeZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-maxComputeWorkGroupSizeZ.html).  
**supportsAsyncCompute** | No | See [Device.SystemInfo.supportsAsyncCompute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsAsyncCompute.html).  
**supportsGraphicsFence** | No | See [Device.SystemInfo.supportsGraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsGraphicsFence.html).  
**supportsAsyncGPUReadback** | No | See [Device.SystemInfo.supportsAsyncGPUReadback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsAsyncGPUReadback.html).  
**supportsParallelPSOCreation** | No | See [Device.SystemInfo.supportsParallelPSOCreation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsParallelPSOCreation.html).  
**supportsRayTracing** | No | See [Device.SystemInfo.supportsRayTracing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsRayTracing.html).  
**supportsRayTracingShaders** | No | See [Device.SystemInfo.supportsRayTracingShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsRayTracingShaders.html).  
**supportsInlineRayTracing** | No | See [Device.SystemInfo.supportsInlineRayTracing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsInlineRayTracing.html).  
**supportsSetConstantBuffer** | No | See [Device.SystemInfo.supportsSetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsSetConstantBuffer.html).  
**hasMipMaxLevel** | No | See [Device.SystemInfo.hasMipMaxLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-hasMipMaxLevel.html).  
**supportsMipStreaming** | No | See [Device.SystemInfo.supportsMipStreaming](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-supportsMipStreaming.html).  
**usesLoadStoreActions** | No | See [Device.SystemInfo.usesLoadStoreActions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo-usesLoadStoreActions.html).  
#### Minimal device definition
The following device definition contains every required property and no optional properties. This is the minimum device definition you can have.
**Note** : This device definition doesn’t provide orientation data, so the simulator assumes the device supports all orientations and that the safe area covers the entire screen.
```
{
    "friendlyName": "Minimal Device",
    "version": 1,
    "screens": [
        {
            "width": 1080,
            "height": 1920,
            "dpi": 450.0
        }
    ],
    "systemInfo": {
        "operatingSystem": "Android"
    }
}

```

#### Complete device definition
The following device definition contains every required and optional property.
```
{
    "friendlyName": "Apple iPhone XR",
    "version": 1,
    "screens": [
        {
            "width": 828,
            "height": 1792,
            "navigationBarHeight": 0,
            "dpi": 326.0,
            "orientations": [
                {
                    "orientation": 1,
                    "safeArea": {
                        "serializedVersion": "2",
                        "x": 0.0,
                        "y": 68.0,
                        "width": 828.0,
                        "height": 1636.0
                    },
                    "cutouts": [
                        {
                            "serializedVersion": "2",
                            "x": 184.0,
                            "y": 1726.0,
                            "width": 460.0,
                            "height": 66.0
                        }
                    ]
                },
                {
                    "orientation": 3,
                    "safeArea": {
                        "serializedVersion": "2",
                        "x": 88.0,
                        "y": 42.0,
                        "width": 1616.0,
                        "height": 786.0
                    },
                    "cutouts": [
                        {
                            "serializedVersion": "2",
                            "x": 0.0,
                            "y": 184.0,
                            "width": 66.0,
                            "height": 460.0
                        }
                    ]
                },
                {
                    "orientation": 4,
                    "safeArea": {
                        "serializedVersion": "2",
                        "x": 88.0,
                        "y": 42.0,
                        "width": 1616.0,
                        "height": 786.0
                    },
                    "cutouts": [
                        {
                            "serializedVersion": "2",
                            "x": 1726.0,
                            "y": 184.0,
                            "width": 66.0,
                            "height": 460.0
                        }
                    ]
                }
            ],
            "presentation": {
                "overlayPath": "Apple iPhone 11_Overlay.png",
                "borderSize": {
                    "x": 51.0,
                    "y": 51.0,
                    "z": 51.0,
                    "w": 51.0
                }
            }
        }
    ],
    "systemInfo": {
        "deviceModel": "iPhone11,8",
        "deviceType": 1,
        "operatingSystem": "iOS 12.0",
        "operatingSystemFamily": 0,
        "processorCount": 6,
        "processorFrequency": 0,
        "processorType": "arm64e",
        "supportsAccelerometer": true,
        "supportsAudio": true,
        "supportsGyroscope": true,
        "supportsLocationService": true,
        "supportsVibration": true,
        "systemMemorySize": 2813,
        "unsupportedIdentifier": "n/a",
        "graphicsDependentData": [
            {
                "graphicsDeviceType": 16,
                "graphicsMemorySize": 1024,
                "graphicsDeviceName": "Apple A12 GPU",
                "graphicsDeviceVendor": "Apple",
                "graphicsDeviceID": 0,
                "graphicsDeviceVendorID": 0,
                "graphicsUVStartsAtTop": true,
                "graphicsDeviceVersion": "Metal",
                "graphicsShaderLevel": 50,
                "graphicsMultiThreaded": true,
                "renderingThreadingMode": 0,
                "hasHiddenSurfaceRemovalOnGPU": true,
                "hasDynamicUniformArrayIndexingInFragmentShaders": true,
                "supportsShadows": true,
                "supportsRawShadowDepthSampling": true,
                "supportsMotionVectors": true,
                "supports3DTextures": true,
                "supports2DArrayTextures": true,
                "supports3DRenderTextures": true,
                "supportsCubemapArrayTextures": true,
                "copyTextureSupport": 31,
                "supportsComputeShaders": true,
                "supportsGeometryShaders": false,
                "supportsTessellationShaders": true,
                "supportsInstancing": true,
                "supportsHardwareQuadTopology": false,
                "supports32bitsIndexBuffer": true,
                "supportsSparseTextures": false,
                "supportedRenderTargetCount": 8,
                "supportsSeparatedRenderTargetsBlend": true,
                "supportedRandomWriteTargetCount": 8,
                "supportsMultisampledTextures": 1,
                "supportsMultisampleAutoResolve": false,
                "supportsTextureWrapMirrorOnce": 0,
                "usesReversedZBuffer": true,
                "npotSupport": 2,
                "maxTextureSize": 16384,
                "maxCubemapSize": 16384,
                "maxComputeBufferInputsVertex": 8,
                "maxComputeBufferInputsFragment": 8,
                "maxComputeBufferInputsGeometry": 0,
                "maxComputeBufferInputsDomain": 8,
                "maxComputeBufferInputsHull": 8,
                "maxComputeBufferInputsCompute": 8,
                "maxComputeWorkGroupSize": 1024,
                "maxComputeWorkGroupSizeX": 1024,
                "maxComputeWorkGroupSizeY": 1024,
                "maxComputeWorkGroupSizeZ": 1024,
                "supportsAsyncCompute": false,
                "supportsGraphicsFence": true,
                "supportsAsyncGPUReadback": true,
                "supportsParallelPSOCreation": true,
                "supportsRayTracing": false,
                "supportsRayTracingShaders": false,
                "supportsInlineRayTracing": false,
                "supportsSetConstantBuffer": true,
                "hasMipMaxLevel": true,
                "supportsMipStreaming": true,
                "usesLoadStoreActions": true,
                "supportedTextureFormats": [1, 2, 3, 4, 5],
                "supportedRenderTextureFormats": [1, 2, 3, 4, 5],
                "ldrGraphicsFormat": 59,
                "hdrGraphicsFormat": 74
            }
        ]
    }
}

```

## Creating a device overlay
A device overlay is an image that contains the border of the device screen and other features such as notches, punchouts, and any other additions to the screen rectangle. You can optionally use it with a device definition to visualize how hardware elements obstruct the device screen, and to determine when touch inputs fail as a result.
The Device Simulator interprets transparent pixels as areas of the screen you can tap, and opaque pixels of any other color as areas that the hardware obstructs. The texture itself can be any shape.
The following examples show device overlays for two iPhone models.
**Note** : To mimic what you see when you use a device overlay, these examples display Unity’s default **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) in the area of the screen where you can tab. In a real device overlay, these pixels should be transparent.
Apple iPhone 8 Overlay | Apple iPhone XS Overlay  
---|---  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/device-simulator-overlay-iphone8.png) | ![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/device-simulator-overlay-iphonexs.png)  
### Using a device overlay
After you create a device overlay texture, to use it with a device definition you must first import the device overlay texture file into your project.
**Note** : When the Device Simulator loads a device overlay texture, it attempts to enable **Read/Write** for it. If this isn’t possible, the Device Simulator displays the texture but can’t use the texture to mask input. This means that if you click on notches and other areas of the screen that the device overlay should mask, the Device Simulator detects input. To ensure this doesn’t happen, when you import the device overlay texture, enable **Read/Write** in the Texture Import Settings window.
When the device overlay texture is in your project, open the device definition file and, in the object that defines a screen the device supports, add the [presentation](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-adding-a-device.html#presentation) property. Here, set the path to the image file (`overlayPath`) and the size of the borders (`borderSize`). For an example of how to do this, see the following device definition file:
```
{
    "friendlyName": "Minimal Device with Overlay",
    "version": 1,
    "screens": [
        {
            "width": 1080,
            "height": 1920,
            "dpi": 450.0,
            "presentation": {
                "overlayPath": "Overlays/MinimalDeviceOverlay.png",
                "borderSize": {
                    "x": 51.0,
                    "y": 51.0,
                    "z": 51.0,
                    "w": 130.0
                }
            }
        }
    ],
    "systemInfo": {
        "operatingSystem": "Android"
    }
}

```

**Note** : The path to the device overlay texture file can be relative to the device definition file, or relative to the directory that contains the **Assets** or **Packages** directory in your Unity project. For example, if the device definition file is in the **Assets/Devices** directory and the device overlay file is in the **Assets/Devices/Overlays** directory, the following file paths are both valid:
  * Relative to the device definition file: **Overlays/MinimalDeviceOverlay.png**
  * Relative to the directory that contains the **Assets** directory: **Assets/Devices/Overlays/MinimalDeviceOverlay.png**


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-simulated-classes.html)
Simulated classes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/device-simulator-plugins.html)
Extending the device simulator
