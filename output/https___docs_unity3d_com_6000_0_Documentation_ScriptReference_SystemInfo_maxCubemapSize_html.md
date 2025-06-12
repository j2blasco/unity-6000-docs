* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxCubemapSize.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).maxCubemapSize
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
maxCubemapSize; 
### Description
Maximum cubemap texture size in pixels (Read Only).
The largest cubemap texture width and height that your graphics hardware supports.  
  
Unity only supports textures up to a size of 16384, even if `maxCubemapSize` returns a larger size.  
  
You can only create a texture with the maximum size if you have enough memory. For example, to create a cubemap with a size of 16384 in an uncompressed format such as [TextureFormat.RGBA32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGBA32.html), you need 6 gigabytes of memory because the amount of data is 4 bytes per pixel × 6 textures × 16384 x 16384. 
* * *
