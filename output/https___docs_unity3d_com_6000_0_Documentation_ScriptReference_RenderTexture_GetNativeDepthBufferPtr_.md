* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.GetNativeDepthBufferPtr.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).GetNativeDepthBufferPtr
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html "Go to RenderTexture Component in the Manual")
## Declaration
public IntPtr GetNativeDepthBufferPtr(); 
### Returns
**IntPtr** Pointer to an underlying graphics API depth buffer resource. 
### Description
Retrieve a native (underlying graphics API) pointer to the depth buffer resource.
Use this function to retrieve a pointer/handle corresponding to the depth buffer part of the RenderTexture, as it is represented on the native graphics API level. This can be used to enable depth buffer manipulation from [native code plugins](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html).  
  
Use [Texture.GetNativeTexturePtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.GetNativeTexturePtr.html) to get a native pointer to the color buffer of a render texture, and this function to get to the depth buffer part. For Depth and ShadowMap render texture formats, the two functions return the same resource. The two functions will also return the same resource if anti aliasing is enabled in the project's quality settings.  
  
Note that calling this function when using multi-threaded rendering will synchronize with the rendering thread (a slow operation), so best practice is to set up needed texture pointers only at initialization time.  
  
Additional resources: [Texture.GetNativeTexturePtr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.GetNativeTexturePtr.html), [Native code plugins](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html).
* * *
