* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer-drawMode.html

#  [SpriteRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html).drawMode
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
[SpriteDrawMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteDrawMode.html) drawMode; 
### Description
The current draw mode of the Sprite Renderer.
When the drawMode is set to [SpriteDrawMode.Sliced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteDrawMode.Sliced.html) or [SpriteDrawMode.Tiled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteDrawMode.Tiled.html), the SpriteRenderer will render the sprite as a 9-slice image.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/9-slice-grid.png) A 9-Slice image is where an image is divided into 9 portion.  
  
The A, C, G and I section sizes will not be affected by the dimension of set by [SpriteRenderer.size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer-size.html).  
  
The B and H section will be repeated horizontally.  
  
The D and F section will be repeated vertically.  
  
The E section will be stretched or repeated both horizontally or vertically.  
  
When set to [SpriteDrawMode.Sliced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteDrawMode.Sliced.html), the B, D, E, F, H section will be stretched to fit the dimension ![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/9-slice-sliced-mode.png)  
  
When set to [SpriteDrawMode.Tiled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteDrawMode.Tiled.html), the B, D, E, F, H section will be repeated to fit the dimension ![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/9-slice-tiled-mode.png)
* * *
