* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-allowThreadedTextureCreation.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).allowThreadedTextureCreation
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
allowThreadedTextureCreation; 
### Description
Allow Unity internals to perform Texture creation on any thread (rather than the dedicated render thread).
When set to true, Unity internals will try to create Textures on a separate worker thread, rather than the dedicated render thread. This results in less hitches during asynchronous loading as it removes some work from the render thread.  
  
When this is set to false, Texture creation occurs on the render thread. Disabling threaded Texture creation can be slightly faster in some cases as it avoids some synchronsation between threads, but may result in hitches with larger Textures. This could be set to false during a non interactive synchronous loading phase to minimise the loading time, then it should be disabled during main gameplay to minimise hitches for any streamed content.  
  
This setting is supported on the following platforms: 
  * Vulkan
  * Metal
  * DX11
  * DX12


For information about support on console platforms, see the platform-specific documentation.  
  
The setting defaults to be true if the platform supports creating Textures on a separate thread. If the platform doesn't support creating Textures on a separate thread Texture.allowThreadedTextureCreation will always return false, even after setting to true.  
  
Note: The C# API's for Texture creation (E.g. new Texture2D) must always be called on the main thread. This setting does not alter that requirement.
* * *
