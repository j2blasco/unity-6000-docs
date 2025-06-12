* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToPNG.html

#  [ImageConversion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.html).EncodeToPNG
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
public static byte[] EncodeToPNG([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex); 
### Parameters
Parameter | Description  
---|---  
tex | The texture to convert.  
### Description
Encodes this texture into PNG format.
This function returns a byte array which is the PNG file data. You can store the encoded data as a file or send it over the network without further processing.  
  
This function does not work on any compressed format. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`.  
  
The encoded PNG data will be either 8bit grayscale, RGB or RGBA (depending on the passed in format). For single-channel red textures ( `R8`, `R16`, `RFloat` and `RHalf` ), the encoded PNG data will be in grayscale. PNG data will not contain gamma correction or color profile information.
```
// Saves screenshot as PNG file.
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;
using System.IO;  
  
public class PNGUploader : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Take a shot immediately
    IEnumerator Start()
    {
        yield return UploadPNG();
    }  
  
    IEnumerator UploadPNG()
    {
        // We should only read the screen buffer after rendering is complete
        yield return new WaitForEndOfFrame[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html)();  
  
        // Create a texture the size of the screen, RGB24 format
        int width = Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html);
        int height = Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html);
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(width, height, TextureFormat.RGB24[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGB24.html), false);  
  
        // Read screen contents into the texture
        tex.ReadPixels(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, width, height), 0, 0);
        tex.Apply();  
  
        // Encode texture into PNG
        byte[] bytes = ImageConversion.EncodeToPNG[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToPNG.html)(tex);
        Object.Destroy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html)(tex);  
  
        // For testing purposes, also write to a file in the project folder
        // File.WriteAllBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.WriteAllBytes.html)(Application.dataPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-dataPath.html) + "/../SavedScreen.png", bytes);  
  

        // Create a Web Form
        WWWForm[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WWWForm.html) form = new WWWForm[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WWWForm.html)();
        form.AddField("frameCount", Time.frameCount.ToString());
        form.AddBinaryData("fileUpload", bytes);  
  
        // Upload to a cgi script
        var w = UnityWebRequest.Post[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Post.html)("http://localhost/cgi-bin/env.cgi?post", form);
        yield return w.SendWebRequest();  
  
        if (w.result != UnityWebRequest.Result.Success[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.Result.Success.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(w.error);
        }
        else
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Finished Uploading Screenshot");
        }
    }
}

```

Additional resources: [ReadPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.ReadPixels.html), [WaitForEndOfFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html), [LoadImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.LoadImage.html), [EncodeArrayToPNG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeArrayToPNG.html), [EncodeNativeArrayToPNG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeNativeArrayToPNG.html), [EncodeToJPG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToJPG.html), [EncodeToTGA](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToTGA.html), [EncodeToEXR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToEXR.html).
* * *
