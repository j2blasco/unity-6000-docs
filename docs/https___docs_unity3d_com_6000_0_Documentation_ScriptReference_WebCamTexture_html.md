* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html

# WebCamTexture
class in UnityEngine
/
Inherits from:[Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)
/
Implemented in:[UnityEngine.AudioModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AudioModule.html)
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
WebCam Textures are textures onto which the live video input is rendered.
On Android, iOS, and WebGL platforms, `WebCamTexture` requires the camera permission. On Android, you can request it at runtime using the [Permission](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.html) API. For more information, refer to [Request runtime permissions](https://docs.unity3d.com/6000.0/Documentation/Manual/android-RequestingPermissions.html) documentation.  
  
On iOS and WebGL, you can request camera permission at runtime using [Application.RequestUserAuthorization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestUserAuthorization.html).  
  
**Note** : On Android and iOS platforms, Unity doesn't support multiple WebCamTextures simultaneously.  
  
The following code example demonstrates how to request the user for camera permission on iOS, Android, and WebGL platforms.
```
using UnityEngine;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections;
using UnityEngine;
#if UNITY_ANDROID
using UnityEngine.Android;
#endif  
  
public class WebCam[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.WebCam.html) : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
#if UNITY_IOS || UNITY_WEBGL
    private bool CheckPermissionAndRaiseCallbackIfGranted(UserAuthorization[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.html) authenticationType, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) authenticationGrantedAction)
    {
        if (Application.HasUserAuthorization[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.HasUserAuthorization.html)(authenticationType))
        {
            if (authenticationGrantedAction != null)
                authenticationGrantedAction();  
  
            return true;
        }
        return false;
    }  
  
    private IEnumerator AskForPermissionIfRequired(UserAuthorization[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.html) authenticationType, Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) authenticationGrantedAction)
    {
        if (!CheckPermissionAndRaiseCallbackIfGranted(authenticationType, authenticationGrantedAction))
        {
            yield return Application.RequestUserAuthorization[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestUserAuthorization.html)(authenticationType);
            if (!CheckPermissionAndRaiseCallbackIfGranted(authenticationType, authenticationGrantedAction))
                Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)($"Permission[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.html) {authenticationType} Denied");
        }
    }
#elif UNITY_ANDROID
    private void PermissionCallbacksPermissionGranted(string permissionName)
    {
        StartCoroutine(DelayedCameraInitialization());
    }  
  
    private IEnumerator DelayedCameraInitialization()
    {
        yield return null;
        InitializeCamera();
    }  
  
    private void PermissionCallbacksPermissionDenied(string permissionName)
    {
        Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)($"Permission[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.html) {permissionName} Denied");
    }  
  
    private void AskCameraPermission()
    {
        var callbacks = new PermissionCallbacks[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.PermissionCallbacks.html)();
        callbacks.PermissionDenied += PermissionCallbacksPermissionDenied;
        callbacks.PermissionGranted += PermissionCallbacksPermissionGranted;
        Permission.RequestUserPermission[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.RequestUserPermission.html)(Permission.Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.Camera.html), callbacks);
    }
#endif  
  
    void Start()
    {
#if UNITY_IOS || UNITY_WEBGL
        StartCoroutine(AskForPermissionIfRequired(UserAuthorization.WebCam[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.WebCam.html), () => { InitializeCamera(); }));
        return;
#elif UNITY_ANDROID
        if (!Permission.HasUserAuthorizedPermission[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.HasUserAuthorizedPermission.html)(Permission.Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.Permission.Camera.html)))
        {
            AskCameraPermission();
            return;
        }
#endif
        InitializeCamera();
    }  
  
    private void InitializeCamera()
    {
        WebCamTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html) webcamTexture = new WebCamTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html)();
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) renderer = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
        renderer.material.mainTexture = webcamTexture;
        webcamTexture.Play();
    }
}

```

### Static Properties
Property | Description  
---|---  
[devices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-devices.html) | Return a list of available devices.  
### Properties
Property | Description  
---|---  
[autoFocusPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-autoFocusPoint.html) | This property allows you to set/get the auto focus point of the camera. This works only on Android and iOS devices.  
[deviceName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-deviceName.html) | Set this to specify the name of the device to use.  
[didUpdateThisFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-didUpdateThisFrame.html) | Did the video buffer update this frame?  
[isDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-isDepth.html) | This property is true if the texture is based on depth data.  
[isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-isPlaying.html) | Returns if the camera is currently playing.  
[requestedFPS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-requestedFPS.html) | Set the requested frame rate of the camera device (in frames per second).  
[requestedHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-requestedHeight.html) | Set the requested height of the camera device.  
[requestedWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-requestedWidth.html) | Set the requested width of the camera device.  
[videoRotationAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-videoRotationAngle.html) | Returns an clockwise angle (in degrees), which can be used to rotate a polygon so camera contents are shown in correct orientation.  
[videoVerticallyMirrored](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-videoVerticallyMirrored.html) | Returns if the texture image is vertically flipped.  
### Constructors
Constructor | Description  
---|---  
[WebCamTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-ctor.html) | Create a WebCamTexture.  
### Public Methods
Method | Description  
---|---  
[GetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.GetPixel.html) | Gets the pixel color at coordinates (x, y).  
[GetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.GetPixels.html) | Gets the pixel color data for a mipmap level as Color structs.  
[GetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.GetPixels32.html) | Gets the pixel color data for a mipmap level as Color32 structs.  
[Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.Pause.html) | Pauses the camera.  
[Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.Play.html) | Starts the camera.  
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.Stop.html) | Stops the camera.  
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
