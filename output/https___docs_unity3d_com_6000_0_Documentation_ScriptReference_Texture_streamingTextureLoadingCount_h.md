* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-streamingTextureLoadingCount.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).streamingTextureLoadingCount
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
streamingTextureLoadingCount; 
### Description
Number of streaming Textures with mipmaps currently loading.
When adding a new camera it can take a few frames to detect which new Textures need to be loaded. Therefore this value can't be relied upon immediately. If any objects move or the camera moves then this value will change so it's not guaranteed to drop to zero. When implementing camera cuts it is recommended you have a minimum time to allow mipmap levels to be calculated and maximum time to wait before doing the cut. This property can be used with a value between the min and max time in order to cut earlier if the mipmaps are loaded in time.  
  
The minimum time is dependent on the number of renderers in the Scene and the number that are processed each frame. A minimum frame delay can be calculated as ([Texture.streamingRendererCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-streamingRendererCount.html) + ([QualitySettings.streamingMipmapsRenderersPerFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsRenderersPerFrame.html)-1)) / [QualitySettings.streamingMipmapsRenderersPerFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsRenderersPerFrame.html). The maximum time should be an acceptable delay to a user. E.g. 0.5 seconds (or 30 frames at 60Hz).  
  
Generally streamingTexturePendingLoadCount is a better choice for camera cut delay as it includes both pending and active loading.  
  
Additional resources: [Texture.streamingTexturePendingLoadCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-streamingTexturePendingLoadCount.html)
* * *
