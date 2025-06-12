* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html

# Camera
class in UnityEngine
/
Inherits from:[Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
### Description
A Camera is a device through which the player views the world.
A screen space point is defined in pixels. The bottom-left of the screen is (0,0); the right-top is ([pixelWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-pixelWidth.html),[pixelHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-pixelHeight.html)). The z position is in world units from the Camera.  
  
A viewport space point is normalized and relative to the Camera. The bottom-left of the Camera is (0,0); the top-right is (1,1). The z position is in world units from the Camera.  
  
A world space point is defined in global coordinates (for example, [Transform.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html)).  
  
Additional resources: [camera component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html).
### Static Properties
Property | Description  
---|---  
[allCameras](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-allCameras.html) | Returns all enabled cameras in the Scene.  
[allCamerasCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-allCamerasCount.html) | The number of cameras in the current Scene.  
[current](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-current.html) | The camera we are currently rendering with, for low-level render control only (Read Only).  
[kMaxAperture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-kMaxAperture.html) | The maximum allowed aperture.  
[kMaxBladeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-kMaxBladeCount.html) | The maximum blade count for the aperture diaphragm.  
[kMinAperture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-kMinAperture.html) | The minimum allowed aperture.  
[kMinBladeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-kMinBladeCount.html) | The minimum blade count for the aperture diaphragm.  
[main](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html) | The first enabled Camera component that is tagged "MainCamera" (Read Only).  
[onPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPostRender.html) | Delegate that you can use to execute custom code after a Camera renders the scene.  
[onPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPreCull.html) | Delegate that you can use to execute custom code before a Camera culls the scene.  
[onPreRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPreRender.html) | Delegate that you can use to execute custom code before a Camera renders the scene.  
### Properties
Property | Description  
---|---  
[activeTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-activeTexture.html) | Gets the temporary RenderTexture target for this Camera.  
[actualRenderingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-actualRenderingPath.html) | The rendering path that is currently being used (Read Only).  
[allowDynamicResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-allowDynamicResolution.html) | Dynamic Resolution Scaling.  
[allowHDR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-allowHDR.html) | High dynamic range rendering.  
[allowMSAA](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-allowMSAA.html) | MSAA rendering.  
[anamorphism](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-anamorphism.html) | The camera anamorphism. To use this property, enable UsePhysicalProperties.  
[aperture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-aperture.html) | The camera aperture. To use this property, enable UsePhysicalProperties.  
[areVRStereoViewMatricesWithinSingleCullTolerance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-areVRStereoViewMatricesWithinSingleCullTolerance.html) | Determines whether the stereo view matrices are suitable to allow for a single pass cull.  
[aspect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-aspect.html) | The aspect ratio (width divided by height).  
[backgroundColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-backgroundColor.html) | The color with which the screen will be cleared.  
[barrelClipping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-barrelClipping.html) | The camera barrel clipping. To use this property, enable UsePhysicalProperties.  
[bladeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-bladeCount.html) | The blade count in the lens of the camera. To use this property, enable UsePhysicalProperties.  
[cameraToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-cameraToWorldMatrix.html) | Matrix that transforms from camera space to world space (Read Only).  
[cameraType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-cameraType.html) | Identifies what kind of camera this is, using the CameraType enum.  
[clearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-clearFlags.html) | How the camera clears the background.  
[clearStencilAfterLightingPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-clearStencilAfterLightingPass.html) | Should the camera clear the stencil buffer after the deferred light pass?  
[commandBufferCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-commandBufferCount.html) | Number of command buffers set up on this camera (Read Only).  
[cullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-cullingMask.html) | This is used to render parts of the Scene selectively.  
[cullingMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-cullingMatrix.html) | Sets a custom matrix for the camera to use for all culling queries.  
[curvature](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-curvature.html) | The curvature of the blades. To use this property, enable UsePhysicalProperties.  
[depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-depth.html) | Camera's depth in the camera rendering order.  
[depthTextureMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-depthTextureMode.html) | How and if camera generates a depth texture.  
[eventMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-eventMask.html) | Mask to select which layers can trigger events on the camera.  
[farClipPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-farClipPlane.html) | The distance of the far clipping plane from the Camera, in world units.  
[fieldOfView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-fieldOfView.html) | The vertical field of view of the Camera, in degrees.  
[focalLength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-focalLength.html) | The camera focal length, expressed in millimeters. To use this property, enable UsePhysicalProperties.  
[focusDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-focusDistance.html) | The focus distance of the lens. To use this property, enable UsePhysicalProperties.  
[forceIntoRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-forceIntoRenderTexture.html) | Should camera rendering be forced into a RenderTexture.  
[gateFit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-gateFit.html) | There are two gates for a camera, the sensor gate and the resolution gate. The physical camera sensor gate is defined by the sensorSize property, the resolution gate is defined by the render target area.  
[iso](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-iso.html) | The sensor sensitivity of the camera. To use this property, enable UsePhysicalProperties.  
[layerCullDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullDistances.html) | Per-layer culling distances.  
[layerCullSpherical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-layerCullSpherical.html) | How to perform per-layer culling for a Camera.  
[lensShift](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-lensShift.html) | The lens offset of the camera. The lens shift is relative to the sensor size. For example, a lens shift of 0.5 offsets the sensor by half its horizontal size.  
[nearClipPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-nearClipPlane.html) | The distance of the near clipping plane from the the Camera, in world units.  
[nonJitteredProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-nonJitteredProjectionMatrix.html) | Get or set the raw projection matrix with no camera offset (no jittering).  
[opaqueSortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-opaqueSortMode.html) | Opaque object sorting mode.  
[orthographic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-orthographic.html) | Is the camera orthographic (true) or perspective (false)?  
[orthographicSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-orthographicSize.html) | Camera's half-size when in orthographic mode.  
[overrideSceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-overrideSceneCullingMask.html) | Sets the culling mask used to determine which objects from which Scenes to draw. See EditorSceneManager.SetSceneCullingMask.  
[pixelHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-pixelHeight.html) | How tall is the camera in pixels (not accounting for dynamic resolution scaling) (Read Only).  
[pixelRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-pixelRect.html) | Where on the screen is the camera rendered in pixel coordinates.  
[pixelWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-pixelWidth.html) | How wide is the camera in pixels (not accounting for dynamic resolution scaling) (Read Only).  
[previousViewProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-previousViewProjectionMatrix.html) | Get the view projection matrix used on the last frame.  
[projectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-projectionMatrix.html) | Set a custom projection matrix.  
[rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-rect.html) | Where on the screen is the camera rendered in normalized coordinates.  
[renderCloudsInSceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-renderCloudsInSceneView.html) | If false, clouds are not rendered in the scene view of this camera.  
[renderingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-renderingPath.html) | The rendering path that should be used, if possible.  
[scaledPixelHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-scaledPixelHeight.html) | How tall is the camera in pixels (accounting for dynamic resolution scaling) (Read Only).  
[scaledPixelWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-scaledPixelWidth.html) | How wide is the camera in pixels (accounting for dynamic resolution scaling) (Read Only).  
[scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-scene.html) | If not null, the camera will only render the contents of the specified Scene.  
[sensorSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-sensorSize.html) | The size of the camera sensor, expressed in millimeters.  
[shutterSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-shutterSpeed.html) | The exposure time of the camera, in seconts. To use this property, enable UsePhysicalProperties.  
[stereoActiveEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-stereoActiveEye.html) | Returns the eye that is currently rendering. If called when stereo is not enabled it will return Camera.MonoOrStereoscopicEye.Mono. If called during a camera rendering callback such as OnRenderImage it will return the currently rendering eye. If called outside of a rendering callback and stereo is enabled, it will return the default eye which is Camera.MonoOrStereoscopicEye.Left.  
[stereoConvergence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-stereoConvergence.html) | Distance to a point where virtual eyes converge.  
[stereoEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-stereoEnabled.html) | Stereoscopic rendering.  
[stereoSeparation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-stereoSeparation.html) | The distance between the virtual eyes. Use this to query or set the current eye separation. Note that most VR devices provide this value, in which case setting the value will have no effect.  
[stereoTargetEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-stereoTargetEye.html) | Defines which eye of a VR display the Camera renders into.  
[targetDisplay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-targetDisplay.html) | Set the target display for this Camera.  
[targetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-targetTexture.html) | Destination render texture.  
[transparencySortAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-transparencySortAxis.html) | An axis that describes the direction along which the distances of objects are measured for the purpose of sorting.  
[transparencySortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-transparencySortMode.html) | Transparent object sorting mode.  
[useJitteredProjectionMatrixForTransparentRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-useJitteredProjectionMatrixForTransparentRendering.html) | Should the jittered matrix be used for transparency rendering?  
[useOcclusionCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-useOcclusionCulling.html) | Whether or not the Camera will use occlusion culling during rendering.  
[usePhysicalProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-usePhysicalProperties.html) | Enable usePhysicalProperties to use physical camera properties to compute the field of view and the frustum.  
[velocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-velocity.html) | Get the world-space speed of the camera (Read Only).  
[worldToCameraMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-worldToCameraMatrix.html) | Matrix that transforms from world to camera space.  
### Public Methods
Method | Description  
---|---  
[AddCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.AddCommandBuffer.html) | Add a command buffer to be executed at a specified place.  
[AddCommandBufferAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.AddCommandBufferAsync.html) | Adds a command buffer to the GPU's async compute queues and executes that command buffer when graphics processing reaches a given point.  
[CalculateFrustumCorners](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CalculateFrustumCorners.html) | Given viewport coordinates, calculates the view space vectors pointing to the four frustum corners at the specified camera depth.  
[CalculateObliqueMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CalculateObliqueMatrix.html) | Calculates and returns oblique near-plane projection matrix.  
[CopyFrom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CopyFrom.html) | Makes this camera's settings match other camera.  
[CopyStereoDeviceProjectionMatrixToNonJittered](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CopyStereoDeviceProjectionMatrixToNonJittered.html) | Sets the non-jittered projection matrix, sourced from the VR SDK.  
[GetCommandBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetCommandBuffers.html) | Get command buffers to be executed at a specified place. This API is only available with the Built-in renderer.  
[GetGateFittedFieldOfView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetGateFittedFieldOfView.html) |  Retrieves the effective vertical field of view of the camera, including GateFit. Fitting the sensor gate and the resolution gate has an impact on the final field of view. If the sensor gate aspect ratio is the same as the resolution gate aspect ratio or if the camera is not in physical mode, then this method returns the same value as the fieldofview property.   
[GetGateFittedLensShift](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetGateFittedLensShift.html) |  Retrieves the effective lens offset of the camera, including GateFit. Fitting the sensor gate and the resolution gate has an impact on the final obliqueness of the projection. If the sensor gate aspect ratio is the same as the resolution gate aspect ratio, then this method returns the same value as the lenshift property. If the camera is not in physical mode, then this methods returns Vector2.zero.   
[GetStereoNonJitteredProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetStereoNonJitteredProjectionMatrix.html) | Gets the non-jittered projection matrix of a specific left or right stereoscopic eye.  
[GetStereoProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetStereoProjectionMatrix.html) | Gets the projection matrix of a specific left or right stereoscopic eye.  
[GetStereoViewMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetStereoViewMatrix.html) | Gets the left or right view matrix of a specific stereoscopic eye.  
[RemoveAllCommandBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RemoveAllCommandBuffers.html) | Remove all command buffers set on this camera.  
[RemoveCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RemoveCommandBuffer.html) | Remove command buffer from execution at a specified place.  
[RemoveCommandBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RemoveCommandBuffers.html) | Remove command buffers from execution at a specified place.  
[Render](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.Render.html) | Render the camera manually.  
[RenderToCubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RenderToCubemap.html) | Render into a static cubemap from this camera.  
[RenderWithShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RenderWithShader.html) | Render the camera with shader replacement.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.Reset.html) | Revert all camera parameters to default.  
[ResetAspect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetAspect.html) | Revert the aspect ratio to the screen's aspect ratio.  
[ResetCullingMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetCullingMatrix.html) | Make culling queries reflect the camera's built in parameters.  
[ResetProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetProjectionMatrix.html) | Make the projection reflect normal camera's parameters.  
[ResetReplacementShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetReplacementShader.html) | Remove shader replacement from camera.  
[ResetStereoProjectionMatrices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetStereoProjectionMatrices.html) | Reset the camera to using the Unity computed projection matrices for all stereoscopic eyes.  
[ResetStereoViewMatrices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetStereoViewMatrices.html) | Reset the camera to using the Unity computed view matrices for all stereoscopic eyes.  
[ResetTransparencySortSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetTransparencySortSettings.html) | Resets this Camera's transparency sort settings to the default. Default transparency settings are taken from GraphicsSettings instead of directly from this Camera.  
[ResetWorldToCameraMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetWorldToCameraMatrix.html) | Make the rendering position reflect the camera's position in the Scene.  
[ScreenPointToRay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ScreenPointToRay.html) | Returns a ray going from camera through a screen point.  
[ScreenToViewportPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ScreenToViewportPoint.html) | Transforms position from screen space into viewport space.  
[ScreenToWorldPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ScreenToWorldPoint.html) | Transforms a point from screen space into world space, where world space is defined as the coordinate system at the very top of your game's hierarchy.  
[SetReplacementShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetReplacementShader.html) | Make the camera render with shader replacement.  
[SetStereoProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetStereoProjectionMatrix.html) | Sets a custom projection matrix for a specific stereoscopic eye.  
[SetStereoViewMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetStereoViewMatrix.html) | Sets a custom view matrix for a specific stereoscopic eye.  
[SetTargetBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetTargetBuffers.html) | Sets the Camera to render to the chosen buffers of one or more RenderTextures.  
[SubmitRenderRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SubmitRenderRequest.html) | Submit a renderRequest.  
[TryGetCullingParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.TryGetCullingParameters.html) | Get culling parameters for a camera.  
[ViewportPointToRay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ViewportPointToRay.html) | Returns a ray going from camera through a viewport point.  
[ViewportToScreenPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ViewportToScreenPoint.html) | Transforms position from viewport space into screen space.  
[ViewportToWorldPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ViewportToWorldPoint.html) | Transforms position from viewport space into world space.  
[WorldToScreenPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.WorldToScreenPoint.html) | Transforms position from world space into screen space.  
[WorldToViewportPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.WorldToViewportPoint.html) | Transforms position from world space into viewport space.  
### Static Methods
Method | Description  
---|---  
[CalculateProjectionMatrixFromPhysicalProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CalculateProjectionMatrixFromPhysicalProperties.html) |  Calculates the projection matrix from focal length, sensor size, lens shift, near plane distance, far plane distance, and Gate fit parameters. To calculate the projection matrix without taking Gate fit into account, use Camera.GateFitMode.None . Additional resources: GateFitParameters   
[FieldOfViewToFocalLength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.FieldOfViewToFocalLength.html) | Converts field of view to focal length. Use either sensor height and vertical field of view or sensor width and horizontal field of view.  
[FocalLengthToFieldOfView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.FocalLengthToFieldOfView.html) | Converts focal length to field of view.  
[GetAllCameras](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetAllCameras.html) | Fills an array of Camera with the current cameras in the Scene, without allocating a new array.  
[HorizontalToVerticalFieldOfView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.HorizontalToVerticalFieldOfView.html) | Converts the horizontal field of view (FOV) to the vertical FOV, based on the value of the aspect ratio parameter.  
[VerticalToHorizontalFieldOfView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.VerticalToHorizontalFieldOfView.html) | Converts the vertical field of view (FOV) to the horizontal FOV, based on the value of the aspect ratio parameter.  
### Messages
Message | Description  
---|---  
[OnPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnPostRender.html) |  Event function that Unity calls after a Camera renders the scene.  
[OnPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnPreCull.html) |  Event function that Unity calls before a Camera culls the scene.  
[OnPreRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnPreRender.html) |  Event function that Unity calls before a Camera renders the scene.  
[OnRenderImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnRenderImage.html) |  Event function that Unity calls after a Camera has finished rendering, that allows you to modify the Camera's final image.  
[OnRenderObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnRenderObject.html) | OnRenderObject is called after camera has rendered the Scene.  
[OnWillRenderObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnWillRenderObject.html) | OnWillRenderObject is called for each camera if the object is visible.  
### Delegates
Delegate | Description  
---|---  
[CameraCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CameraCallback.html) | Delegate type for camera callbacks.  
### Inherited Members
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) | Enabled Behaviours are Updated, disabled Behaviours are not.  
[isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) | Reports whether a GameObject and its associated Behaviour is active and enabled.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[BroadcastMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.BroadcastMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object or any of its children.  
[CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.CompareTag.html) | Checks the GameObject's tag against the defined tag.  
[GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) | Gets a reference to a component of type T on the same GameObject as the component specified.  
[GetComponentInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInChildren.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any child of the GameObject.  
[GetComponentIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentIndex.html) | Gets the index of the component on its parent GameObject.  
[GetComponentInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInParent.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any parent of the GameObject.  
[GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponents.html) | Gets references to all components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInChildren.html) | Gets references to all components of type T on the same GameObject as the component specified, and any child of the GameObject.  
[GetComponentsInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInParent.html) | Gets references to all components of type T on the same GameObject as the component specified, and any parent of the GameObject.  
[SendMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object.  
[SendMessageUpwards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessageUpwards.html) | Calls the method named methodName on every MonoBehaviour in this game object and on every ancestor of the behaviour.  
[TryGetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.TryGetComponent.html) | Gets the component of the specified type, if it exists.  
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
