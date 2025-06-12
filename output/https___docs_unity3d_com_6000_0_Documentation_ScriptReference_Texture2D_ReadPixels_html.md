* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.ReadPixels.html

#  [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).ReadPixels
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
public void ReadPixels([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) source, int destX, int destY, bool recalculateMipMaps = true); 
### Parameters
Parameter | Description  
---|---  
source | The region of the render target to read from.  
destX | The x position in the texture to write the pixels to.  
destY | The y position in the texture to write the pixels to.  
recalculateMipMaps | When the value is `true`, Unity automatically recalculates the mipmap for the texture after it writes the pixel data. Otherwise, Unity doesn't do this automatically.  
### Description
Reads pixels from the current render target and writes them to a texture.
This method copies a rectangular area of pixel colors from the currently active render target on the GPU (for example the screen, a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html), or a [GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html)) and writes them to a texture on the CPU at position (`destX`, `destY`). [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`, and you must call [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) after `ReadPixels` to upload the changed pixels to the GPU.  
  
The lower left corner is (0, 0).  
  
`ReadPixels` is usually slow, because the method waits for the GPU to complete all previous work first. To copy a texture more quickly, use one of the following methods instead: 
  * [AsyncGPUReadback.RequestIntoNativeArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.RequestIntoNativeArray.html) to copy a texture from the GPU to the CPU.
  * [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html), [CommandBuffer.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.CopyTexture.html) or [Graphics.Blit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html) to copy a texture on the GPU only.


The render target and the texture must use the same format, and the format must be supported on the device for both rendering and sampling.  
  
You can automatically update the mipmap when you call [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) instead of setting `recalculateMipMaps` to `true`.  
  
The following code example demonstrates how to use `ReadPixels` in the Built-in Render Pipeline. In Scriptable Render Pipelines such as the Universal Render Pipeline (URP), [Camera.onPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPostRender.html) isn't available, but you can use [RenderPipelineManager.endCameraRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endCameraRendering.html) in a similar way.
```
using UnityEngine;  
  
public class ReadPixelsExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Set Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that has a Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) component and a material that displays a texture
    public Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) screenGrabRenderer;  
  
    private Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) destinationTexture;
    private bool isPerformingScreenGrab;  
  
    void Start()
    {
        // Create a new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) with the width and height of the screen, and cache it for reuse
        destinationTexture = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html), Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html), TextureFormat.RGB24[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGB24.html), false);  
  
        // Make screenGrabRenderer display the texture.
        screenGrabRenderer.material.mainTexture = destinationTexture;  
  
        // Add the onPostRender callback
        Camera.onPostRender[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPostRender.html) += OnPostRenderCallback;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // When the user presses the Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) key, perform the screen grab operation
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            isPerformingScreenGrab = true;
        }
    }  
  
    void OnPostRenderCallback(Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam)
    {
        if (isPerformingScreenGrab)
        {
            // Check whether the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) that just finished rendering is the one you want to take a screen grab from
            if (cam == Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html))
            {
                // Define the parameters for the ReadPixels operation
                Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) regionToReadFrom = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html), Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html));
                int xPosToWriteTo = 0;
                int yPosToWriteTo = 0;
                bool updateMipMapsAutomatically = false;  
  
                // Copy the pixels from the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)'s render target to the texture
                destinationTexture.ReadPixels(regionToReadFrom, xPosToWriteTo, yPosToWriteTo, updateMipMapsAutomatically);  
  
                // Upload texture data to the GPU, so the GPU renders the updated texture
                // Note: This method is costly, and you should call it only when you need to
                // If you do not intend to render the updated texture, there is no need to call this method at this point
                destinationTexture.Apply();  
  
                // Reset the isPerformingScreenGrab state
                isPerformingScreenGrab = false;
            }
        }
    }  
  
    // Remove the onPostRender callback
    void OnDestroy()
    {
        Camera.onPostRender[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPostRender.html) -= OnPostRenderCallback;
    }
}

```

Additional resources: [ImageConversion.EncodeToPNG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToPNG.html).
* * *
