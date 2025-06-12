* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.GetPixels32.html

#  [WebCamTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html).GetPixels32
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
public Color32[] GetPixels32(Color32[] colors = null); 
### Parameters
Parameter | Description  
---|---  
colors | An optional array to write the pixel data to.  
### Returns
**Color32[]** An array that contains the pixel colors. 
### Description
Gets the pixel color data for a mipmap level as [Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) structs.
This method gets pixel data from the texture in CPU memory. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`.  
  
The array contains the pixels row by row, starting at the bottom left of the texture. The size of the array is the width × height of the texture.   
  
Each pixel is a [Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) struct.  
  
A single call to `GetPixels32` is usually faster than multiple calls to [GetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.GetPixel.html), especially for large textures.  
  
If `GetPixels32` fails, Unity throws an exception. `GetPixels32` might fail if the array contains too much data.  
  
You can optionally pass in an array of [Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) structs to avoid allocating new memory each frame. This can improve performance if you are continuously reading data from the camera. The array must be initialized to the dimensions `width * height` of the texture. If you don't pass an array, Unity will allocate one and return it.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    WebCamTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html) webcamTexture;
    Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html)[] data;  
  
    void Start()
    {
        // Start web cam feed
        webcamTexture = new WebCamTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html)();
        webcamTexture.Play();
        data = new Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html)[webcamTexture.width * webcamTexture.height];
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        webcamTexture.GetPixels32(data);
        // Do processing of data here.
    }
}

```

* * *
