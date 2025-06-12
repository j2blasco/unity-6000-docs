* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.GetPixel.html

#  [WebCamTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html).GetPixel
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
## Declaration
public [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) GetPixel(int x, int y); 
### Parameters
Parameter | Description  
---|---  
x | The x coordinate of the pixel to get. The range is `0` through the (texture width - 1).  
y | The y coordinate of the pixel to get. The range is `0` through the (texture height - 1).  
### Returns
**Color** The pixel color. 
### Description
Gets the pixel color at coordinates (`x`, `y`).
This method gets pixel data from the texture in CPU memory. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`.  
  
The lower left corner is (0, 0). If the pixel coordinate is outside the texture's dimensions, Unity clamps or repeats it, depending on the texture's [TextureWrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.html).  
  
If you need to get a large block of pixels, it might be faster to use [GetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.GetPixels.html).  
  
**Note:** For depth data based WebCamTexture instances, the depth value (distance in meters) can be accessed using the [Color.r](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-r.html) property. Additional resources: [WebCamTexture.isDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture-isDepth.html).  
  
Additional resources: [GetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.GetPixels32.html), [GetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.GetPixels.html).
* * *
