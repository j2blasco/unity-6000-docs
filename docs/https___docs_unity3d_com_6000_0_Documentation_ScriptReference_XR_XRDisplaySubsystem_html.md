* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html

# XRDisplaySubsystem
class in UnityEngine.XR
/
Inherits from:[IntegratedSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IntegratedSubsystem.html)
/
Implemented in:[UnityEngine.XRModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.XRModule.html)
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
An XRDisplaySubsystem controls rendering to a head tracked display.
### Properties
Property | Description  
---|---  
[contentProtectionEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-contentProtectionEnabled.html) | Sets or gets the state of content protection for the current active provider. For most providers, content protection allows you to use write only textures for rendering. This stops the ability for apps to read textures from the graphics card and view/record images that may be protected in some way.   
[disableLegacyRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-disableLegacyRenderer.html) | Disables the legacy renderer while this XRDisplaySubsystem is active.  
[displayOpaque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-displayOpaque.html) | Determines if the current attached device has an opaque display. Most VR devices are opaque in order to increase the immersive experience, AR devices are transparent to allow for interaction with an augmentation of the current environment.   
[foveatedRenderingFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-foveatedRenderingFlags.html) | Controls optional behavior of the foveated rendering system.  
[foveatedRenderingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-foveatedRenderingLevel.html) | Controls the intensity of the foveated rendering system.  
[hdrOutputSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-hdrOutputSettings.html) | The HDROutputSettings for the XR Display Subsystem.  
[occlusionMaskScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-occlusionMaskScale.html) | A scale applied to the standard occulsion mask.  
[reprojectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-reprojectionMode.html) | The kind of reprojection the app requests to stabilize its holographic rendering relative to the user's head motion.  
[scaleOfAllRenderTargets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-scaleOfAllRenderTargets.html) | Controls the size of the textures submitted to the display as a multiplier of the display's default resolution.  
[scaleOfAllViewports](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-scaleOfAllViewports.html) | Controls how much of the allocated display texture should be used for rendering.  
[supportedTextureLayouts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-supportedTextureLayouts.html) | Specifies all texture layouts supported by this display subsystem. This var is a bit field that could be combination of XRDisplaySubsystem.TextureLayout.  
[textureLayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-textureLayout.html) | Set DisplaySubsystem to use certain texture layout. Should query supported texture layout through XRDisplaySubsystem.supportedTextureLayouts first for the capabilities.  
[zFar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-zFar.html) | Set DisplaySubsystem to use zFar for rendering.  
[zNear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-zNear.html) | Set DisplaySubsystem to use zNear for rendering.  
### Public Methods
Method | Description  
---|---  
[AddGraphicsThreadMirrorViewBlit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.AddGraphicsThreadMirrorViewBlit.html) | This function records the display subsystem's native blit event to the target command buffer. This function is typically called by a scriptable rendering pipeline.  
[BeginRecordingIfLateLatched](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.BeginRecordingIfLateLatched.html) | This function enables late latching recording of constant buffer memory locations which are later patched with the latest pose data.  
[EndRecordingIfLateLatched](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.EndRecordingIfLateLatched.html) | This function disables late latching recording of constant buffer locations.  
[GetCullingParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.GetCullingParameters.html) | Gets culling parameters for a specific culling pass index.  
[GetMirrorViewBlitDesc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.GetMirrorViewBlitDesc.html) | Get a mirror view blit operation descriptor from the current display subsystem.  
[GetPreferredMirrorBlitMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.GetPreferredMirrorBlitMode.html) | Returns the XR display's preferred mirror blit mode.  
[GetRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.GetRenderPass.html) | Gets an XRRenderPass of a specific index.  
[GetRenderPassCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.GetRenderPassCount.html) | The number of XRRenderPass entries for this XR Display.  
[GetRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.GetRenderTexture.html) | Given the UnityXRRenderTextureID returned by IUnityXRDisplayInterface::CreateTexture, return the managed UnityEngine.RenderTexture instance.  
[GetRenderTextureForRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.GetRenderTextureForRenderPass.html) | Given a render pass, return the RenderTexture instance backing that render pass. If the render pass is invalid, or if the render texture does not exist, return null.  
[GetSharedDepthTextureForRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.GetSharedDepthTextureForRenderPass.html) | Given a render pass, return the shared depth buffer RenderTexture instance backing that render pass. If the render pass is invalid, or if the render texture does not exist, return null.  
[MarkTransformLateLatched](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.MarkTransformLateLatched.html) | This marks a given GameObject's transform to be late latched in the next frame. Once marked for late latching, the GameObject transform and its descendants will be updated with the latest VR pose updates before rendering is submitted to the GPU.  
[SetFocusPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.SetFocusPlane.html) | Sets a point in 3D space that acts as the focal point of the Scene for this frame. This helps to improve the visual fidelity of content around this point. You must set this value every frame. Note that specifying body-locked content in focus improves the fidelity of body-locked content at the expense of content not locked to the body. This is especially apparent when the user moves.   
[SetMSAALevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.SetMSAALevel.html) | Set MSAA level for the DisplaySubsystem's render texture.  
[SetPreferredMirrorBlitMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.SetPreferredMirrorBlitMode.html) | Override the XR display's preferred mirror blit mode from the script.  
[TryGetAppGPUTimeLastFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.TryGetAppGPUTimeLastFrame.html) | Retrieves the time the GPU has spent on executing commands from the application's last frame, as reported by the XR Plugin. Measured in seconds.  
[TryGetCompositorGPUTimeLastFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.TryGetCompositorGPUTimeLastFrame.html) | Retrieves the amount of time that the GPU spent executing the compositor renderer during the last frame, as reported by the XR Plugin. Measured in seconds.  
[TryGetDisplayRefreshRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.TryGetDisplayRefreshRate.html) | Retrieves the refresh rate of the display as reported by the XR Plugin.  
[TryGetDroppedFrameCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.TryGetDroppedFrameCount.html) | Retrieves the number of dropped frames reported by the XR Plugin.  
[TryGetFramePresentCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.TryGetFramePresentCount.html) | Retrieves the number of times the current frame has been drawn to the device as reported by the XR Plugin.  
[TryGetMotionToPhoton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.TryGetMotionToPhoton.html) | Retrieves the motion-to-photon value as reported by the XR Plugin.  
### Events
Event | Description  
---|---  
[displayFocusChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-displayFocusChanged.html) | Event sent when XR display focus changes.  
### Inherited Members
### Properties
Property | Description  
---|---  
[running](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IntegratedSubsystem-running.html) | Whether or not the subsystem is running.  
### Public Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IntegratedSubsystem.Destroy.html) | Destroys this instance of a subsystem.  
[Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IntegratedSubsystem.Start.html) | Starts an instance of a subsystem.  
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IntegratedSubsystem.Stop.html) | Stops an instance of a subsystem.  
* * *
