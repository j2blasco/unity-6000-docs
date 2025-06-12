* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxTextureSize.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).maxTextureSize
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
maxTextureSize; 
### Description
Maximum texture size in pixels (Read Only).
The largest texture width and height that your graphics hardware supports.  
  
Unity only supports textures up to a size of 16384, even if `maxTextureSize` returns a larger size.  
  
You can only create a texture with the maximum size if you have enough memory. For example, you need 1 gigabyte of memory to create a texture with a size of 16384, because the amount of data is 4 bytes per pixel × 16384 × 16384. 
* * *
