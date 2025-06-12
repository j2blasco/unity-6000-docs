* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToJPG.html

#  [ImageConversion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.html).EncodeToJPG
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
public static byte[] EncodeToJPG([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex, int quality); 
## Declaration
public static byte[] EncodeToJPG([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex); 
### Parameters
Parameter | Description  
---|---  
tex | Text texture to convert.  
quality | JPG quality to encode with. The range is 1 through 100. 1 is the lowest quality. The default is 75.  
### Description
Encodes this texture into JPG format.
This function returns a byte array which is the JPG file data. You can store the encoded data as a file or send it over the network without further processing.  
  
This function does not work on any compressed format. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`. The encoded JPG data will be either 8bit grayscale, RGB or RGBA (depending on the passed in format). 
```
// Saves screenshot as JPG file.
using UnityEngine;
using System.Collections;
using System.IO;  
  
public class JPGScreenSaver : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Take a shot immediately
    IEnumerator Start()
    {
        yield return SaveScreenJPG();
    }  
  
    IEnumerator SaveScreenJPG()
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
  
        // Encode the texture in JPG format
        byte[] bytes = ImageConversion.EncodeToJPG[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToJPG.html)(tex);
        Object.Destroy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html)(tex);  
  
        // Write the returned byte array to a file in the project folder
        File.WriteAllBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.WriteAllBytes.html)(Application.dataPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-dataPath.html) + "/../SavedScreen.jpg", bytes);
    }
}

```

Additional resources: [EncodeArrayToJPG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeArrayToJPG.html), [EncodeNativeArrayToJPG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeNativeArrayToJPG.html), [EncodeToPNG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToPNG.html), [EncodeToTGA](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToTGA.html), [EncodeToEXR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToEXR.html).
* * *
