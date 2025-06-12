* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture-ctor.html

# SparseTexture Constructor
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
public SparseTexture(int width, int height, [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) textureFormat, int mipCount, bool linear = false); 
### Parameters
Parameter | Description  
---|---  
width | Texture width in pixels.  
height | Texture height in pixels.  
mipCount | Mipmap count. Pass -1 to create full mipmap chain.  
linear | Whether texture data will be in linear or sRGB color space (default is sRGB).  
textureFormat | Texture Format.  
### Description
Create a sparse texture.
See [SparseTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.html).
* * *
