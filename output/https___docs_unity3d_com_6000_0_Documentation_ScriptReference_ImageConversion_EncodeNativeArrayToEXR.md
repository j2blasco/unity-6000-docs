* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeNativeArrayToEXR.html

#  [ImageConversion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.html).EncodeNativeArrayToEXR
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
public static NativeArray<byte> EncodeNativeArrayToEXR(NativeArray<T> input, [Experimental.Rendering.GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) format, uint width, uint height, uint rowBytes, [Texture2D.EXRFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.EXRFlags.html) flags); 
### Parameters
Parameter | Description  
---|---  
input | The native array to convert.  
format | The pixel format of the image data.  
width | The width of the image data in pixels.  
height | The height of the image data in pixels.  
rowBytes | The length of a single row in bytes. The default is 0, which means Unity calculates the length automatically.  
flags | Flags used to control compression and the output format. The default is [Texture2D.EXRFlags.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.EXRFlags.None.html)  
### Description
Encodes this native array into the EXR format.
This function returns a NativeArray<byte> which is the EXR data. You can store the encoded data as a file or send it over the network without further processing.  
  
This function does not work on any compressed format. Although it is best to use this function for HDR texture formats (either 16-bit or 32-bit floats), it can be used with other formats (and the data is converted on the fly). The default output format is uncompressed 16-bit float EXR and can be controlled using the passed in flags. The encoded EXR data will only contain an alpha channel when the passed-in format has one. For single-channel red textures ( `R8`, `R16`, `RFloat` and `RHalf` ), the encoded data will be in grayscale mode.  
  
The native array that this function returns is allocated with the persistent allocator, so this function should only be called from the main thread. 
```
// Saves screenshot as EXR file.
using System.Collections;
using System.IO;
using Unity.Collections;
using UnityEngine;  
  
public class EXRScreenSaver : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Take a shot immediately
    IEnumerator Start()
    {
        yield return SaveScreenEXR();
    }  
  
    IEnumerator SaveScreenEXR()
    {
        // Read the screen buffer after rendering is complete
        yield return new WaitForEndOfFrame[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html)();  
  
        // Create a texture in RGBAFloat format the size of the screen
        int width = Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html);
        int height = Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html);
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(width, height, TextureFormat.RGBAFloat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGBAFloat.html), false);  
  
        // Read the screen contents into the texture
        tex.ReadPixels(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, width, height), 0, 0);
        tex.Apply();  
  
        // Encode the bytes in EXR format
        NativeArray<byte> imageBytes = new NativeArray<byte>(tex.GetRawTextureData(), Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
        var bytes = ImageConversion.EncodeNativeArrayToEXR[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeNativeArrayToEXR.html)(imageBytes, tex.graphicsFormat, (uint)width, (uint)height);
        Object.Destroy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html)(tex);  
  
        // Write the returned byte array to a file in the project folder
        File.WriteAllBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.WriteAllBytes.html)(Application.dataPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-dataPath.html) + "/../SavedScreen.exr", bytes.ToArray());
    }
}

```

Additional resources: [EncodeToEXR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToEXR.html), [EncodeArrayToEXR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeArrayToEXR.html), [EncodeNativeArrayToPNG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeNativeArrayToPNG.html), [EncodeNativeArrayToJPG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeNativeArrayToJPG.html), [EncodeNativeArrayToTGA](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeNativeArrayToTGA.html).
* * *
