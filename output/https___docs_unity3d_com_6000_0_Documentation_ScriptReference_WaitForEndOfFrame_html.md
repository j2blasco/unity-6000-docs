* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html

# WaitForEndOfFrame
class in UnityEngine
/
Inherits from:[YieldInstruction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/YieldInstruction.html)
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Waits until the end of the frame after Unity has rendered every Camera and GUI, just before displaying the frame on screen.
You can use it to read the display into a Texture, encode it as an image file (see [Texture2D.ReadPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.ReadPixels.html) and [Texture2D.Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.EncodeToPNG.html)) and store it on a device.  
  
Switching from the Game view to the Scene view causes [WaitForEndOfFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html) to freeze. It only continues when the application switches back to the Game view. This can only happen when the application is working in the Unity editor.  
  
**Note:** This coroutine is not invoked on the editor in batch mode. For further details please look at the [Command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html) page in the manual.
```
using System.IO;
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Take a shot immediately
    IEnumerator Start()
    {
        UploadPNG();
        yield return null;
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
        byte[] bytes = tex.EncodeToPNG();
        Destroy(tex);  
  
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
            print(w.error);
        else
            print("Finished Uploading Screenshot");
        yield return null;
    }
}

```

```
using UnityEngine;
using System.Collections;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // A script that shows destination alpha channel in the game view.  
  
    Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat;  
  
    void CreateMaterial()
    {
        // Unity has a built-in shader that is useful for drawing
        // simple colored things. In this case, we just want to use
        // a blend mode that inverts destination colors.
        var shader = Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Hidden/Internal-Colored");
        mat = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(shader);
        mat.hideFlags = HideFlags.HideAndDontSave[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideAndDontSave.html);
        // Set blend mode to show destination alpha channel.
        mat.SetInt("_SrcBlend", (int)UnityEngine.Rendering.BlendMode.DstAlpha);
        mat.SetInt("_DstBlend", (int)UnityEngine.Rendering.BlendMode.Zero);
        // Turn off backface culling, depth writes, depth test.
        mat.SetInt("_Cull", (int)UnityEngine.Rendering.CullMode.Off);
        mat.SetInt("_ZWrite", 0);
        mat.SetInt("_ZTest", (int)UnityEngine.Rendering.CompareFunction.Always);
    }  
  
    public IEnumerator Start()
    {
        CreateMaterial();
        while (true)
        {
            // Wait until all rendering + UI is done.
            yield return new WaitForEndOfFrame[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html)();
            // Draw a quad that shows alpha channel.
            GL.PushMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PushMatrix.html)();
            GL.LoadOrtho[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadOrtho.html)();
            mat.SetPass(0);
            GL.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html)(GL.QUADS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.QUADS.html));
            GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0, 0, 0);
            GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(1, 0, 0);
            GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(1, 1, 0);
            GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0, 1, 0);
            GL.End[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html)();
            GL.PopMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PopMatrix.html)();
        }
        yield return null;
    }
}

```

Additional resources: [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html), [WaitForSeconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html), [WaitForFixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForFixedUpdate.html), [WaitForSecondsRealtime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime.html), [WaitUntil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitUntil.html),[WaitWhile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitWhile.html).
### Inherited Members
* * *
