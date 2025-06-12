* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsRenderersPerFrame.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).streamingMipmapsRenderersPerFrame
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
streamingMipmapsRenderersPerFrame; 
### Description
The number of renderer instances that are processed each frame when calculating which texture mipmap levels should be streamed.
If the number of renderers exceeds this limit, the mipmap levels of the textures associated with those additional renderers are calculated in subsequent frames.  
  
Lower this value to reduce the CPU cost of calculating the optimal mipmap levels. The tradeoff is that a lower value also reduces the rate of texture mipmap computation and the loading of those desired mipmaps.  
  
By default, the initial value is 512, but this can be set in the [Quality](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html) section of the Editor **Project Settings** window, under **Textures** > **Mipmap Streaming**.  
  
Note: Do not change `streamingMipmapsRenderersPerFrame` too frequently at runtime. You should allow enough time between changes for all the renderers to be processed. Updating this value more frequently will lead to unused mips remaining loaded. The following example illustrates how to calculate the number of frames to delay between changes:
```
using System.Collections;
using UnityEngine;
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    int nextUpdateAllowed = 0;
    int _renderersPerFrame;  
  
    // Increase this value when frame rate is high, lower when frame rate drops)
    public int RenderersPerFrame
    {
        get { return QualitySettings.streamingMipmapsRenderersPerFrame[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsRenderersPerFrame.html); }
        set
        {
            _renderersPerFrame = value;
            StopCoroutine("UpdateRenderCount");
            StartCoroutine("UpdateRenderCount");
        }
    }  
  
    IEnumerator UpdateRenderCount()
    {
        while (Time.frameCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-frameCount.html) < nextUpdateAllowed)
            yield return null;  
  
        QualitySettings.streamingMipmapsRenderersPerFrame[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsRenderersPerFrame.html) = _renderersPerFrame;
        int frameDelay = (int)(Texture.streamingRendererCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-streamingRendererCount.html) + (ulong)(_renderersPerFrame - 1)) / _renderersPerFrame;
        nextUpdateAllowed = Time.frameCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-frameCount.html) + frameDelay;  
  
        yield return null;
    }
}

```

Additional resources: [Texture.streamingRendererCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-streamingRendererCount.html).
* * *
