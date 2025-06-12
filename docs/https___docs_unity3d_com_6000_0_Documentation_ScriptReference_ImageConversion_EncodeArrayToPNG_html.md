* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeArrayToPNG.html

#  [ImageConversion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.html).EncodeArrayToPNG
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
public static byte[] EncodeArrayToPNG(Array array, [Experimental.Rendering.GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) format, uint width, uint height, uint rowBytes); 
### Parameters
Parameter | Description  
---|---  
array | The byte array to convert.  
format | The pixel format of the image data.  
width | The width of the image data in pixels.  
height | The height of the image data in pixels.  
rowBytes | The length of a single row in bytes. The default is 0, which means Unity calculates the length automatically.  
### Description
Encodes this array into PNG format.
This function returns a byte array which is the PNG file data. You can store the encoded data as a file or send it over the network without further processing.  
  
This function does not work on any compressed format. The encoded PNG data will be either 8bit grayscale, RGB or RGBA (depending on the passed in format). For single-channel red textures ( `R8`, `R16`, `RFloat` and `RHalf` ), the encoded PNG data will be in grayscale. PNG data will not contain gamma correction or color profile information.  
  
This method is thread safe. 
```
// Saves screenshot as PNG file.
using System.Collections;
using System.IO;
using UnityEngine;  
  
public class PNGScreenSaver : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Take a shot immediately
    IEnumerator Start()
    {
        yield return SaveScreenPNG();
    }  
  
    IEnumerator SaveScreenPNG()
    {
        // Read the screen buffer after rendering is complete
        yield return new WaitForEndOfFrame[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html)();  
  
        // Create a texture in RGB24 format the size of the screen
        int width = Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html);
        int height = Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html);
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(width, height, TextureFormat.RGB24[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGB24.html), false);  
  
        // Read the screen contents into the texture
        tex.ReadPixels(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, width, height), 0, 0);
        tex.Apply();  
  
        // Encode the bytes in PNG format
        byte[] bytes = ImageConversion.EncodeArrayToPNG[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeArrayToPNG.html)(tex.GetRawTextureData(), tex.graphicsFormat, (uint)width, (uint)height);
        Object.Destroy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html)(tex);  
  
        // Write the returned byte array to a file in the project folder
        File.WriteAllBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.WriteAllBytes.html)(Application.dataPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-dataPath.html) + "/../SavedScreen.png", bytes);
    }
}

```

Additional resources: [EncodeToPNG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToPNG.html), [EncodeNativeArrayToPNG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeNativeArrayToPNG.html), [EncodeArrayToJPG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeArrayToJPG.html), [EncodeArrayToTGA](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeArrayToTGA.html), [EncodeArrayToEXR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeArrayToEXR.html).
* * *
